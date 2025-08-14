from ulits import read_video, save_video
from trackers import Tracker
import cv2
import numpy as np
from team_assigmner import TeamAssigner
from pllayer_ball_assigner import PlayerBallAssigner
from camera_movement_estimator import CameraMovementEstimator
from view_transformer import ViewTransformer
from speed_and_distance_estimator import SpeedAndDistance_Estimator




def main():
    #read video
    video_frames = read_video('input_video_file/test (14).mp4')

    # Initialize Tracker
    tracker = Tracker("models/best.pt")
    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=True,
                                       stub_path= 'stubs/track_stubs14.pkl')

    # Get object positions
    tracker.add_position_to_tracks(tracks)

    # camera movement estimator
    camera_movement_estimator = CameraMovementEstimator(video_frames[0])
    camera_movement_per_frame = camera_movement_estimator.get_camera_movement(video_frames,
                                                                              read_from_stub=True,
                                                                              stub_path='stubs/camera_movement_stub14.pkl')
    camera_movement_estimator.add_adjust_positions_to_tracks(tracks, camera_movement_per_frame)

    # View Trasnformer
    view_transformer = ViewTransformer()
    view_transformer.add_transformed_position_to_tracks(tracks)

    # Interpolate Ball Positions
    tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])

    # Speed and distance estimator
    speed_and_distance_estimator = SpeedAndDistance_Estimator()
    speed_and_distance_estimator.add_speed_and_distance_to_tracks(tracks)

    # Assign Player Teams
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0],
                                    tracks['players'][0])

    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num],
                                                 track['bbox'],
                                                 player_id)
            tracks['players'][frame_num][player_id]['team'] = team
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

    # Assign ball acquisition
    player_assigner = PlayerBallAssigner()
    team_ball_control = []
    for frame_num, player_track in enumerate(tracks['players']):
        ball_bbox = tracks['ball'][frame_num][1]['bbox']
        assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

        if assigned_player != -1:
            tracks['players'][frame_num][assigned_player]['has_ball'] = True
            team_ball_control.append(tracks['players'][frame_num][assigned_player]['team'])
        else:
            # If no player is assigned the ball, append the previous team or a default value
            if team_ball_control:  # Check if the list is not empty
                team_ball_control.append(team_ball_control[-1])
            else:
                # Default value for the first frame when no player has the ball
                team_ball_control.append(0)  # Assuming team 0 as default; adjust as needed
    team_ball_control = np.array(team_ball_control)


    #draw output
    ##draw object tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks,team_ball_control)

    ## Draw Camera movement
    output_video_frames = camera_movement_estimator.draw_camera_movement(output_video_frames, camera_movement_per_frame)

    ## Draw Speed and Distance
    speed_and_distance_estimator.draw_speed_and_distance(output_video_frames, tracks)

    #save video
    save_video(output_video_frames,"output_videos/output_video14.avi")


if __name__ == "__main__":
    main()