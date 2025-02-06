from os import remove, rename

import ffmpeg


def accelerate_file(file):
    audio_file = "audio_file.mp3"
    (ffmpeg.input(file).filter("atempo", 1.05).output(audio_file, acodec="mp3").run())

    accelerated_file = f"accelerated_{file}"
    (
        ffmpeg.input(file)
        .filter("setpts", "0.95238*PTS")
        .output(accelerated_file, vcodec="libx264")
        .run()
    )

    output_file = f"final_{accelerated_file}"
    input_video = ffmpeg.input(accelerated_file)
    input_audio = ffmpeg.input(audio_file)
    (ffmpeg.concat(input_video, input_audio, v=1, a=1).output(output_file).run())

    remove(audio_file)
    remove(accelerated_file)
    rename(output_file, file)
