import ffmpeg
from hashlib import md5
from time import localtime

def change_name(file):
    prefix = md5(str(localtime()).encode('utf-8')).hexdigest()
    (
        ffmpeg
        .input(file)
        .output(f'{prefix}_{file}')
        .run()
    )
