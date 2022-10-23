import os
import random
import shutil

import cv2
import natsort
import imagehash
import pandas as pd
from tqdm import tqdm
from PIL import Image



class VideoProcessing:
    """
    a class for working with video
    """

    def __init__(self, ):
        pass

    def save_discard_frame_video(self, path_video: str, path_for_save_image: str, fps_needed: int = 20):
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
                image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
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


    def dlt_duplicate_img(self, path_imgs, path_img_after_delete):
        """

        :param path_img:
        :param path_img_after_delete:
        :return:
        """
        os.makedirs(path_img_after_delete, exist_ok=True)
        list_files_img = os.listdir(path_imgs)
        list_imagehash = []
        for iterr in tqdm(list_files_img, desc='get image hash'):
            val_hash = imagehash.average_hash(Image.open(f'{path_imgs}/{iterr}'))
            list_imagehash.append(val_hash)
        data = pd.DataFrame(
            {
                'file_name_image': list_files_img,
                'hash_file': list_imagehash
            }
        )
        data = data.drop_duplicates('hash_file', keep='first')
        # создаем список для нужных файлов изображений
        list_files_image_new = data['file_name_image'].values.tolist()
        for img in tqdm(list_files_image_new, desc='copy file after delete duplicate'):
            shutil.copy2(f'{path_imgs}/{img}', path_img_after_delete)

    def multiple_dlt_duplicate_img(self, paths_imgs_dirs, path_after_dlt_dup):
        paths_dir_img = os.listdir(paths_imgs_dirs)
        for path in paths_dir_img:
            self.dlt_duplicate_img(f'{paths_imgs_dirs}/{path}', f'{path_after_dlt_dup}/{path}')


def run():
    project_path = os.path.dirname(os.path.abspath(__file__))
    vid_proc = VideoProcessing()



    path_video = '/home/artemii_vibs/Downloads/IMG_8162.MOV'
    vid_proc.save_discard_frame_video(path_video, '/home/artemii_vibs/Downloads/IMG_8162')

if __name__ == '__main__':
    run()
