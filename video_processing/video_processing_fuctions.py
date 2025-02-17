import cv2
import numpy as np


class Video:
    def __init__(self, video):
        self.video = video
        self.video_vetor = None
        self.fps = None
        self.height = None
        self.width = None
        self.frames_gray = None 
        self.video_vetor_2D = None
        
        
        
        
    def upload_video_3D_4_2D(self):
        cap = cv2.VideoCapture(self.video)
        self.frames_gray = []

        self.fps = cap.get(cv2.CAP_PROP_FPS)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            self.frames_gray.append(gray_frame)

        cap.release()

        # Verifica se há frames carregados
        if len(self.frames_gray) > 0:
            self.height, self.width = self.frames_gray[0].shape  #
            print('Shape do vídeo: Height, width= ({},{})'.format(self.height, self.width))
        self.video_vetor = np.array(self.frames_gray)
        print("lenth vetor_frame_2d: shape {}".format(self.video_vetor.shape))
        self.video_vetor_2D = self.video_vetor.reshape(self.height * self.width, -1)
        
        print('flattening vector video{}'.format(self.video_vetor_2D.shape))

        return self.video_vetor_2D


        
        