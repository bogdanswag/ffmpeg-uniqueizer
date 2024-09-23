import ffmpeg
from os import rename

def change_fps(file):
    (
        ffmpeg
        .input(file)
        .filter('fps', fps=60)
        .output(f'60fps_{file}')
        .run()
    )

    rename(f'60fps_{file}', file)
