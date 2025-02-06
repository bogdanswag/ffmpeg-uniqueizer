from os import rename

import ffmpeg


def use_filters(file):
    brightness = 0.05 # 0 --> 1
    contrast = 1.1 # 0 ... 1 ... 2
    gamma = 0.95 # 0 ... 1 ... 2
    saturation = 1.1 # 0 ... 1 ... 2
    hue = 5 # 0 --> 100

    output_file = f'filtered_{file}'
    (
        ffmpeg
        .input(file)
        .output(output_file, vf=f'eq=brightness={brightness}:contrast={contrast}:gamma={gamma}:saturation={saturation},hue=h={hue}')
        .run()
    )

    rename(output_file, file)
