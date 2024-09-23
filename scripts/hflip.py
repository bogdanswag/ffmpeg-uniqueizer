import ffmpeg
from os import rename, remove

def hflip_video(file):
    audio_file = f'audio_file.mp3'
    (
        ffmpeg
        .input(file)
        .output(audio_file, acodec='mp3')
        .run()
    )

    hflipped_file = f'hflipped_{file}'
    (
        ffmpeg
        .input(file)
        .hflip()
        .output(hflipped_file)
        .run()
    )

    output_file = f'final_{hflipped_file}'
    input_video = ffmpeg.input(hflipped_file)
    input_audio = ffmpeg.input(audio_file)

    (
        ffmpeg
        .concat(input_video, input_audio, v=1, a=1)
        .output(output_file)
        .run()
    )

    remove(audio_file)
    remove(hflipped_file)
    rename(output_file, file)
