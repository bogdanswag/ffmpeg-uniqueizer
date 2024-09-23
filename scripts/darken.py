import ffmpeg
from os import rename

def darken_video(file):
    brightness = -0.07

    output_file = f'darkened_{file}'
    (
        ffmpeg
        .input(file)
        .output(output_file, vf=f'eq=brightness={brightness}')
        .run()
    )

    rename(output_file, file)
