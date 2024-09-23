import ffmpeg
from os import rename, remove

def blur_file(file):

    audio_file = f'audio_file.mp3'
    (
        ffmpeg
        .input(file)
        .output(audio_file, acodec='mp3')
        .run()
    )

    blured_file = f'blured_{file}'
    (
        ffmpeg
        .input(file)
        .filter('boxblur', luma_radius=0.5, luma_power=1.05)
        .output(blured_file)
        .run()
    )

    output_file = f'final_{blured_file}'
    input_video = ffmpeg.input(blured_file)
    input_audio = ffmpeg.input(audio_file)
    (
        ffmpeg
        .concat(input_video, input_audio, v=1, a=1)
        .output(output_file)
        .run()
    )

    remove(audio_file)
    remove(blured_file)
    rename(output_file, file)
