import cv2
import os

def split_one_frame_per_second(video_path, dest_folder):
    # Try to open the video
    vidcap = cv2.VideoCapture(video_path)
    if not vidcap.isOpened():
        print(f"Error: Could not open video '{video_path}'")
        return

    # Create destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Get the total duration of the video in seconds
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    frame_count = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = frame_count / fps if fps > 0 else 0

    print(f"Video opened: {duration:.2f} seconds, {fps:.2f} fps, {int(frame_count)} frames")

    count = 0
    while True:
        # Jump to the timestamp (in milliseconds)
        vidcap.set(cv2.CAP_PROP_POS_MSEC, count * 1000)
        success, frame = vidcap.read()

        if not success or frame is None:
            break  # end of video

        # Save frame as JPEG
        filename = os.path.join(dest_folder, f"frame_{count:04d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")

        count += 1
        if count > duration:
            break

    vidcap.release()
