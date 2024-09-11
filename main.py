from moviepy.editor import VideoFileClip, concatenate_videoclips

# Funciones para las transiciones
def apply_transition(clip1, clip2, transition):
    if transition == 'fade':
        # Transición de desvanecimiento (1 segundo)
        return concatenate_videoclips([clip1.crossfadeout(1), clip2.crossfadein(1)], method="compose")
    elif transition == 'slide':
        # Transición de deslizamiento (simple efecto para ilustrar)
        return concatenate_videoclips([clip1, clip2.set_start(clip1.duration).fx(vfx.slide_in, 1, 'left')], method="compose")
    else:
        # Si no hay transición, simplemente concatenar los videos
        return concatenate_videoclips([clip1, clip2])

# Leer el archivo 'estructura.txt'
def leer_estructura(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read().strip()
        elementos = contenido.split(', ')
        return elementos

# Procesar la estructura y aplicar las transiciones
def procesar_videos_y_transiciones(estructura):
    clips = []
    for i in range(0, len(estructura), 2):
        # Cargar el video
        video = VideoFileClip(estructura[i])
        
        # Si hay otro video después, aplicar la transición
        if i + 2 < len(estructura):
            transicion = estructura[i + 1]
            video_siguiente = VideoFileClip(estructura[i + 2])
            video = apply_transition(video, video_siguiente, transicion)
        
        clips.append(video)
    
    # Concatenar todos los clips procesados
    video_final = concatenate_videoclips(clips, method="compose")
    return video_final

# Función principal
def main():
    # Leer la estructura del archivo
    estructura = leer_estructura('estructura.txt')

    # Procesar los videos y transiciones
    video_final = procesar_videos_y_transiciones(estructura)

    # Guardar el video final
    video_final.write_videofile("acabado/video_final.mp4", fps=24)

if __name__ == '__main__':
    main()
