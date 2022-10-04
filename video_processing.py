import os
import random

import cv2
import natsort
from tqdm import tqdm


class VideoProcessing:
    """
    a class for working with video
    """

    def __init__(self, path_video: str, fps_needed: str):
        self.path_video = path_video
        self.fps_needed = fps_needed


    def save_discard_frame_video(self, path_video: str, fps_needed: int):
        """
        saving and discarding frames from video
        :param path_video: the path to the video file
        :param fps_needed: The right number of frames per second
        """
        # create directory for save image
        path_img = f'{path_video[:-4]}_{fps_needed}'
        os.makedirs(path_img, exist_ok=True)


        vidcap = cv2.VideoCapture(path_video)  # start videocapture
        count_frames_video = round(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))  # get count images in video
        fps_video = round(vidcap.get(cv2.CAP_PROP_FPS))  # get count images in video
        range_cut_video = round(fps_video / fps_needed)  # range_cut_video step length for frame selection

        frames = 0  #  number of frame for save
        for count_frame in tqdm(range(count_frames_video)):
            success, image = vidcap.read()  # read images and success from videocapture
            if count_frame % range_cut_video == 0:  # clipping
                frames += 1  # number save image
                cv2.imwrite(f'{path_img}/{frames}.jpg', image)  # save image


    def write_video_from_images(self, path_img: str, fps: int, name_video: str):
        """
        making a video out of images
        :param path_img: the path to the directory with the images
        :param fps: The right fps in video (check self.fps_needed)
        """
        path_img_array = natsort.natsorted(os.listdir(path_img))
        img_array = []
        test_image = random.choice(path_img_array)
        height, width, layers = cv2.imread(os.path.join(path_img, test_image)).shape
        size = (width, height)
        for filename in tqdm(path_img_array):
            img = cv2.imread(os.path.join(path_img, filename))
            img_array.append(img)
        out = cv2.VideoWriter(f'{name_video}.mp4', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()


def run():
    path_video = 'Taylor Swift - willow (Official Music Video).mp4'

a = 0
