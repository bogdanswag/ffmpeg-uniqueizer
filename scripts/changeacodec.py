import ffmpeg
from os import rename

def change_acodec(file):

    audio_codec = input('\nEnter audiocodec (default aac): ')
    output_file = f'changedacodec_{file}'

    (
        ffmpeg
        .input(file)
        .output(output_file, acodec=audio_codec)
        .run()
    )

    rename(output_file, file)
