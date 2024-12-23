import subprocess
import pkg_resources
import os
import glob
from tqdm import tqdm

REQUIRED_PACKAGES = [
    'opencv-python',
    'tqdm'
]

for package in REQUIRED_PACKAGES:
    try:
        dist = pkg_resources.get_distribution(package)
        print('{} ({}) is installed'.format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        print('{} is NOT installed'.format(package))
        subprocess.call(['pip', 'install', package])

import cv2

def extract_frames(video_path, dir_path):
    # The video filename with extension
    video_name = os.path.basename(video_path)

    # Start capturing the feed
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Could not open video file {video_path}. Please check the file format.")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    i = 0

    with tqdm(total=total_frames, desc=video_name, ncols=80) as pbar:
        while (cap.isOpened()):
            # Get the frame
            ret, frame = cap.read()
            if ret == False:
                break

            # Save the results in the directory path
            # Include the video filename and frame number in the image filename
            # Strip the video extension for the output image filename
            cv2.imwrite(os.path.join(dir_path, f'{os.path.splitext(video_name)[0]}_frame{i}.png'), frame)
            i += 1
            pbar.update(1)

             # Stop extracting frames after 10 images
            if i >= 10:
                break

    cap.release()
    cv2.destroyAllWindows()

# Directory containing the videos
input_dir = "./input/deepfake/FakeVideo-FakeAudio"

# Directory where we are  going to store the frames
output_dir = "./output/FakeVideo-FakeAudio"

# Create output directories if they don't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get a list of all video files in the input directory
video_extensions = ["*.mp4", "*.avi", "*.mkv", "*.mov", "*.flv", "*.wmv"]
video_paths = []
for input_dir_path in [input_dir]:
    paths = [glob.glob(os.path.join(input_dir_path, ext)) for ext in video_extensions]
    paths = [item for sublist in paths for item in sublist]
    video_paths.extend(paths)

if not video_paths:
    print("No video files found in the input directory.")
    exit(1)

# Extract frames for each video file
for video_path, output_folder in zip(video_paths, [output_dir] * len(video_paths)):
    extract_frames(video_path, output_folder)