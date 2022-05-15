import argparse
import cv2
from pathlib import Path
import random

parser = argparse.ArgumentParser()

parser.add_argument("--video", required=True)
parser.add_argument("--sample", default=10, type=int)

def frame_random_sampling(video_path, sample_num):
    video_path = Path(video_path)

    cap = cv2.VideoCapture(str(video_path))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    random.seed(0)
    sampled = random.sample(range(frame_count), sample_num)
    print(sampled)

    cnt = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break

        if cnt in sampled:
            image_path = video_path.parent / (video_path.stem + f"_{cnt}" +".jpg")
            print(str(image_path))

            cv2.imwrite(str(image_path), frame)

        cnt += 1

    cap.release()

if __name__ == "__main__":
    print("main")
    args = parser.parse_args()
    print(args.video, args.sample)
    frame_random_sampling(args.video, args.sample)
