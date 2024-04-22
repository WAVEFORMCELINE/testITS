import cv2
import numpy as np


def generate_video(text):
    width = 100
    height = 100
    duration = 3
    fps = 60
    total_frames = int(fps * duration)
    dx = 3
    text_color = (255, 255, 255)

    font = cv2.FONT_HERSHEY_COMPLEX
    font_size = 1

    background_color = (0, 0, 0)

    video_writer = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    text_pos = width+dx

    for frame_num in range(total_frames):
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        frame[:] = background_color
        text_pos -= dx

        cv2.putText(frame, text, (text_pos, height // 2), font, font_size, text_color, 2)

        video_writer.write(frame)

    video_writer.release()
    with open("video.mp4", "rb") as f:
        video_data = f.read()
    return video_data