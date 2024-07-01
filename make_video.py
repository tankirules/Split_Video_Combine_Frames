import subprocess
import sys
import os
from subprocess import check_output
#import cv2  
#from PIL import Image  
from pymediainfo import MediaInfo
#from ffprobe import FFProbe
import ffmpeg
import glob
from natsort import natsorted

ffmpeg_path = "E:\\SCHOOL STUFF\\CODING\\PYTHON\\Make_frames_video\\ffmpeg\\bin\\ffmpeg.exe"


#TODO: put this on the frame extracting python file
def extract_audio(video, video_path, folder):
    
    # subprocess.run([ffmpeg_path, "-i", video, "-f", "mp3", "-ab", "192000", "-vn", "audio.mp3"])
    with open("test.log", "w", buffering=1) as f:
        process = subprocess.Popen([ffmpeg_path, "-i", video_path, "-f", "mp3", "-ab", "192000", "-vn", video + "_audio.mp3"], stdout=subprocess.PIPE)
        #f.write("Extracting audio\n")
        
        # for line in process.stdout:
        #     f.write(line.decode("utf-8"))   
        
        for c in iter(lambda: process.stdout.read(1), b""):
            sys.stdout.buffer.write(c)
            #TODO: FOR SOME REASON I CANT GET IT TO WRITE TO FILE
            f.write(c.decode("utf-8"))
        #out = subprocess.check_output([ffmpeg_path, "-i", video, "-f", "mp3", "-ab", "192000", "-vn", "audio.mp3"],stderr=subprocess.STDOUT)  
        #print(out.decode('utf-8'))             
        #f.write(out.decode("utf-8"))

    print('Audio Extraction Complete!')

def make_video(video_name, video_path, folder, output_folder):
    extract_audio(video_name, video_path, folder)
    
    #get the frame rate of the video
    media_info = MediaInfo.parse(video_path)
    frame_rate = -1
    for track in media_info.tracks:
        if track.track_type == 'Video':
            frame_rate = int(float(track.frame_rate))
            
    if frame_rate == -1:
        print("Error: Could not get frame rate!")
        sys.exit()
    
    
    frame_time = 1 / frame_rate
    #get all files in folder

    files = natsorted(glob.glob(folder + '/*.png'))
    #print(files)

    
    with open('files.txt', 'w') as f:
        for item in files:
            item = item.replace('\\', '/')
            f.write('file ' + item + '\n')
            f.write('duration ' + str(frame_time) + '\n')
    
    #sys.exit()
    audio = ffmpeg.input(video_name + '_audio.mp3')
    #forwardslash = folder.replace('\\', '/')
    
    # files = ffmpeg.input('files.txt', framerate=frame_rate)
    # video = ffmpeg.concat(files, 'unsafe')
    
    video = ffmpeg.input('files.txt', format='concat', safe=0)
    out_vid_nam = video_name + '_combined.mp4'
    output_path = os.path.join(output_folder, out_vid_nam)
    ffmpeg.concat(video, audio, v=1, a=1).output(output_path).run()
    # (
    #     ffmpeg
    #     .input(folder + '/*.*', pattern_type='glob', framerate=frame_rate)
    #     .input(video_name + '_audio.mp3')
    #     .output(video_name + '_censored.mp4')
    #     .run(capture_stdout=True)
    # )
    
   
    #delete audio file
    os.remove(video_name + '_audio.mp3') 
    
   


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python make_video.py <video_path> <folder to images> <output_folder>")
        sys.exit
    video_path = sys.argv[1]
    
    #get path
    #handle forward or backslashes because windows lul
    video_name = video_path.split('/')[-1]
    video_name = video_name.split('\\')[-1]
    print(video_name)
    
    folder = sys.argv[2]
    output_folder = sys.argv[3]
    make_video(video_name, video_path, folder, output_folder)

