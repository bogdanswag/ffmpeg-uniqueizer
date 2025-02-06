from os import rename

import ffmpeg


def create_aecho(file):
    (
        ffmpeg
        .input(file)
        .output(f'echo_{file}', af='aecho=0.62:0.31:10:0.51,volume=3')
        .run()
    )

    rename(f'echo_{file}', file)
