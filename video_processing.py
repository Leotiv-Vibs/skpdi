import os
import random

import cv2
import natsort
from tqdm import tqdm


class VideoProcessing:
    """
    a class for working with video
    """

    def __init__(self, ):
        pass

    def save_discard_frame_video(self, path_video: str, path_for_save_image: str, fps_needed: int):
        """
        saving and discarding frames from video
        :param path_video: the path to the video file
        :param fps_needed: The right number of frames per second
        """
        # create directory for save image
        path_img = f'{path_for_save_image}/{path_video.split("/")[-1][:-4]}_{fps_needed}'
        os.makedirs(path_img, exist_ok=True)

        vidcap = cv2.VideoCapture(path_video)  # start videocapture
        count_frames_video = round(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))  # get count images in video
        fps_video = round(vidcap.get(cv2.CAP_PROP_FPS))  # get count images in video
        range_cut_video = round(fps_video / fps_needed)  # range_cut_video step length for frame selection

        frames = 0  # number of frame for save
        for count_frame in tqdm(range(count_frames_video), desc='save and discard frame video'):
            success, image = vidcap.read()  # read images and success from videocapture
            if count_frame % range_cut_video == 0:  # clipping
                frames += 1  # number save image
                cv2.imwrite(f'{path_img}/{frames}.jpg', image)  # save image

    def write_video_from_images(self, path_img: str, fps: int, name_video: str):
        """
        making a video out of images
        :param path_img: the path to the directory with the images
        :param fps: The right fps in video (check self.fps_needed)
        :param name_video: name for save video
        """
        path_img_array = natsort.natsorted(os.listdir(path_img))  # sorted list with image name
        test_image = random.choice(path_img_array)
        height, width, layers = cv2.imread(os.path.join(path_img, test_image)).shape
        size = (width, height)  # params for init VideoWriter
        out = cv2.VideoWriter(f'{name_video}.mp4', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

        for filename in tqdm(path_img_array, desc='write video from list image'):
            img = cv2.imread(os.path.join(path_img, filename))
            out.write(img)

        out.release()

    def multiple_video_discard_save(self, path_dir_video: str, path_for_save_image: str, fps_needed: int = 5):
        os.makedirs(path_for_save_image, exist_ok=True)
        names_video = os.listdir(path_dir_video)
        for name in names_video:
            path_video = f'{path_dir_video}/{name}'
            self.save_discard_frame_video(path_video, path_for_save_image, fps_needed)


def run():
    project_path = os.path.dirname(os.path.abspath(__file__))
    path_videos = f'{project_path}/videos'
    path_for_save_image = f'{project_path}/images_from_video'

    vid_proc = VideoProcessing()
    vid_proc.multiple_video_discard_save(path_videos, path_for_save_image)


if __name__ == '__main__':
    run()
