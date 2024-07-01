# Python Video Splitting/Creation

Simple python scripts to split a video into individual frames,  
and to create a video from frames (requires original video for audio)



## Prerequisites
You must have ffmpeg.exe in the same directory as the python scripts, or have it in your PATH.  
You can download ffmpeg [here](https://ffmpeg.org/) . 
You must have python3 installed.   
Tested on python 3.10.5.

## Installation

Clone the repository, and install the requirements.
```bash
pip install requirements.txt
```

## Usage
### Splitting a Video into Frames:
```
python3 make_frames.py <path_to_video>
```
This will create a folder with the same name as the video, in the same folder as the video.  
The folder will contain sequentially numbered frames.
### Combining frames into Video:
```
python3 make_video.py <video_path> <folder_to_images> <output_folder>
```
The original video is needed to extract the audio for the final output. This will create a video named  
"original_video_combined.mp4" in the output folder specified.

## Example commands
```
python3 make_frames.py "C:\Users\Admin\Downloads\video.mp4"
```
This will create a folder named "video" in C:\Users\Admin\Downloads\.

```
python3 make_video.py "C:\Users\Admin\Downloads\video.mp4" "C:\Users\Admin\Downloads\images" "C:\Users\Admin\Downloads\output"
```
Video.mp4 is the original video, images is a folder containing sequentially numbered images, and "output" will be the folder  
Containing the output video.




## TroubleShooting
Make an issue here on github and I'll try my best to help you.
If you see any error complaining about media info, try installing it from [here](https://mediaarea.net/en/MediaInfo/Download)  
(Or just search up MediaInfo)


## License

[MIT](https://choosealicense.com/licenses/mit/)