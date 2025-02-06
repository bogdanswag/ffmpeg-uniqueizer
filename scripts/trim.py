from os import rename

import ffmpeg


def trim_video(file):
    seconds = 1 # or int(input('Enter number of seconds to trim: '))
    output_file = f'trimmed_{file}'

    probe = ffmpeg.probe(file)
    duration = float(probe['format']['duration'])

    start_time = max(0, duration - seconds)

    (
        ffmpeg
        .input(file, t=start_time)
        .output(output_file)
        .run()
    )

    rename(output_file, file)
