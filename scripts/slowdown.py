from os import remove, rename

import ffmpeg


def slowdown_video(file):
    audio_file = f'forslw_ext_aud_{file[:-4]}.mp3'
    (
        ffmpeg
        .input(file)
        .filter('atempo', 1/1.05)
        .output(audio_file, acodec='mp3')
        .run()
    )

    slowed_file = f'slowed_{file}'
    (
        ffmpeg
        .input(file)
        .filter('setpts', '1.05*PTS')
        .output(slowed_file, vcodec='libx264')
        .run()
    )

    output_file = f'final_{slowed_file}'
    input_video = ffmpeg.input(slowed_file)
    input_audio = ffmpeg.input(audio_file)
    (
        ffmpeg
        .concat(input_video, input_audio, v=1, a=1)
        .output(output_file)
        .run()
    )

    remove(audio_file)
    remove(slowed_file)
    rename(output_file, file)
