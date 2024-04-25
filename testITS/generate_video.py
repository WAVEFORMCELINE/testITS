import cv2
import numpy as np
from logs.models import QueryLog

def calculate_pos(frame_num, total_frames, width, text):
    k = len(text) * 20
    rightleft = (total_frames - frame_num) / total_frames
    run = rightleft * (width + k) - k
    return round(run)


def generate_video(text):
    width = 100
    height = 100
    duration = 3
    fps = 60
    total_frames = int(fps * duration)
    text_color = (255, 255, 255)

    font = cv2.FONT_HERSHEY_COMPLEX
    font_size = 1

    background_color = (0, 0, 0)

    video_writer = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))


    for frame_num in range(total_frames):
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        frame[:] = background_color
        cv2.putText(frame, text, (calculate_pos(frame_num, total_frames, width, text), height // 2), font, font_size, text_color, 2)
        video_writer.write(frame)

    video_writer.release()
    with open("video.mp4", "rb") as f:
        video_data = f.read()

    query = f"Бегущая строка: {text}"
    QueryLog.objects.create(query=query)

    return video_data