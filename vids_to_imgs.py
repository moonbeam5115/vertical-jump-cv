import os
import cv2

class VidHandler():
    '''
    Vid Handler Class providing functionality to turn videos to images and place them in a specific folder
    '''

    def __init__(self, vid_path, img_path):

        self.vid_path = vid_path
        self.img_path = img_path

    def video_to_image(self):

        # Loop through each video in path
        for idx, video_file in enumerate(os.listdir(self.vid_path)):
            print(video_file)
            vid_directory = self.img_path + '/' + 'vid' + '_' + '{}'.format(idx + 1)
            os.mkdir(vid_directory)
            video_cap = cv2.VideoCapture(self.vid_path + '/' + video_file)

            count = 0
            # Read in each frame and save it
            while(video_cap.isOpened()):
                try:
                    success, image = video_cap.read()
                    cv2.imwrite(vid_directory + '/' + 'img' + '_' + '{}'.format(count + 1) + '.jpg', image)
                    count += 1
                except:
                    break

def main():
    vpath = 'jump_videos'
    ipath = 'imgs'

    vid_handler_obj = VidHandler(vpath, ipath)
    vid_handler_obj.video_to_image()


if __name__ == '__main__':
    main()