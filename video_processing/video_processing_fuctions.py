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
        
        print('flattening vector video {}'.format(self.video_vetor_2D.shape))

        return self.video_vetor_2D
    
    '''nesse caso a variavel "video_vetor_2d" é feito por colunas sendo igual ao numero de frame e cada frame é achatado para uma dimensão'''
        
    def make_video_mp4(self, video_vetor):
        '''criem um algoritmo que receba esse video_vetor e transforme ele em um video
        aqui nesse "return None" substitui o video em si, para ele retornar o video feito em mp4'''
        return None
        
        
    def rotate_90(self, video_vetor_2d, video_name = 'rotate_90'):
        '''nesse caso e como na de 180 graus. Assim que rotacionarem o frame, vcs vao chamar a função make_video_mp4(video_vetor_2D) pra gerar esse video final
                aqui nesse "return None" substitui o video em si, para ele retornar o video feito em mp4'''    
        return None
    
    def rotate_180(self, video_vetor_2d, video_name = 'rotate_180'):
        '''Assim que rotacionarem o frame, vcs vao chamar a função make_video_mp4(video_vetor_2D) pra gerar esse video final
                aqui nesse "return None" substitui o video em si, para ele retornar o video feito em mp4'''
    
        return None    
    
    def crop_video(self, video_vetor_2d, initial_time, final_time, video_name = 'crop_video'):
        '''Assim que fizerem o crop, vcs vao chamar a função make_video_mp4(video_vetor_2D) pra gerar esse video final
                aqui nesse "return None" substitui o video em si, para ele retornar o video feito em mp4'''    
        return None
    
    def plot_histogram(self, video_vetor_2d, video_name = 'plot_histogram_video'):
        '''nesse caso, voces devem criar uma plotagem animada e salvar essa plotagem como um video mp4 utilizando alguma bilbioteca que ajude'''    
        return None
    
    def plot_image_frame_3d(self, video_vetor_2d, ):
        '''nesse caso, voces devem pegar o primeiro frame e fazer a plotagem em 3d para mostrar uma imagem se comporta como sinal
        nao precisam baixar esse plot, usem somente o "plt.show()" '''    
        return None