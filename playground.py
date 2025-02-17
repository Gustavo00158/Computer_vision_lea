from video_processing.video_processing_fuctions import \
    Video  # essa biblioteca vai importar todos as funções(métodos) do arquivo video_processing_fuctions e classe video

path_file = "video/beam.avi"


Video = Video(path_file) #aqui vamos passar o valor da variavel pro outro arquivo 

vetor_flatten_2d = Video.upload_video_3D_4_2D() #aqui a função so abre o video 


"essa variavel 'vetor_flatten_2d' que deve ser passado como parametro das outras funções, chamem todas as outras funções"
