import ffmpeg


def convert_format(file):
    (
        ffmpeg
        .input(file)
        .output(f'{file[:-4]}.mov', acodec='copy', vcodec='copy', format='mov')
        .run()
    )
