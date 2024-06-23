import sys
from pymediainfo import MediaInfo
import ffmpeg
import os
from pathlib import Path

def extract_frames(video_path):
    video_name = video_path.split('/')[-1]
    video_name = video_name.split('\\')[-1]
    
    video_dir = video_path.replace(video_name, '')
    #print(video_dir)
    #sys.exit()
    
    media_info = MediaInfo.parse(video_path)
    frame_rate = -1
    for track in media_info.tracks:
        if track.track_type == 'Video':
            frame_rate = int(float(track.frame_rate))
            
    if frame_rate == -1:
        print("Error: Could not get frame rate!")
        sys.exit()

    cwd = os.getcwd()
    new_folder_path = os.path.join(video_dir, Path(video_name).stem)
    #get rid of the trailing .mp4
    
    
    #fps_str = f"1/{frame_rate}"
    #print(fps_str)
    #sys.exit()
    
    #print(new_folder_path)
    
    os.mkdir(new_folder_path)
    
    
    
    
    #split frames
    (
        ffmpeg
        .input(video_path)
        .filter('fps', fps = frame_rate)
        .output(new_folder_path + '/%d.png', start_number=0)
        .overwrite_output()
        .run()
        
    )




if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python make_frames.py <video_path> ")
        sys.exit()
    video_path = sys.argv[1]
    extract_frames(video_path)