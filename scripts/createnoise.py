from os import remove, rename
from os.path import exists

import ffmpeg


def create_noise(file):
    audio_file = "extracted_audio.mp3"
    noised_video = f"noised_{file}"
    output_file = "final_output.mp4"

    try:
        (ffmpeg.input(file).output(audio_file, acodec="mp3").run())
    except ffmpeg.Error:
        print(f"No audio stream found in {file}, skipping audio extraction.")
        audio_file = None

    (
        ffmpeg.input(file)
        .filter("noise", alls="20", allf="t+u")
        .output(noised_video, vcodec="libx264", acodec="copy")
        .run()
    )

    input_video = ffmpeg.input(noised_video)

    if audio_file:
        input_audio = ffmpeg.input(audio_file)
        (ffmpeg.concat(input_video, input_audio, v=1, a=1).output(output_file).run())
        remove(audio_file)
    else:
        rename(noised_video, output_file)

    if exists(noised_video):
        remove(noised_video)
    rename(output_file, file)
