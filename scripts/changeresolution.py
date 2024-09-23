import ffmpeg
from os import rename

def change_resolution(file):
    audio_file = f'audio_file.mp3'
    (
        ffmpeg
        .input(file)
        .output(audio_file, acodec='mp3')
        .run()
    )

    probe = ffmpeg.probe(file, cmd='ffprobe')
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    width = int(video_stream['width'])
    height = int(video_stream['height'])

    input_video = ffmpeg.input(file)
    input_audio = ffmpeg.input(audio_file)

    (
        ffmpeg
        .concat(input_video, input_audio, v=1, a=1)
        .crop(width, height, width-10, height-10)
        .output(f'resized_{file}')
        .run()
    )

    rename(f'resized_{file}', file)
