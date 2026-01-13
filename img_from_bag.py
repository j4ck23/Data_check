import pyrealsense2 as rs
import cv2
import os
import numpy as np

def extract_rgb_from_bag(bag_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_device_from_file(bag_path, repeat_playback=False)
    config.enable_stream(rs.stream.color)

    pipeline.start(config)

    playback = pipeline.get_active_profile().get_device().as_playback()
    playback.set_real_time(False)

    last_sec = -1
    frame_id = 0

    try:
        while True:
            frames = pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            if not color_frame:
                continue

            timestamp_sec = int(color_frame.get_timestamp() / 1000)

            if timestamp_sec != last_sec:
                color_image = np.asanyarray(color_frame.get_data())
                color_image = cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR)

                filename = os.path.join(output_dir, f"rgb_{frame_id:04d}.jpg")
                cv2.imwrite(filename, color_image)
                print(f"Saved {filename}")

                last_sec = timestamp_sec
                frame_id += 1
    except RuntimeError:
        # End of bag
        pass

    pipeline.stop()
