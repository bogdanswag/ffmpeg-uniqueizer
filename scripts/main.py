import shutil
import ffmpeg
from accelerate import accelerate_file
from blur import blur_file
from changeacodec import change_acodec
from changebitrate import change_bitrate
from changename import change_name
from changeresolution import change_resolution
from convertformat import convert_format
from createaecho import create_aecho
from createnoise import create_noise
from darken import darken_video
from filters import use_filters
from fps import change_fps
from hflip import hflip_video
from metadata import change_metadata
from slowdown import slowdown_video
from trim import trim_video

def process_file(input_path):
    input_path_copy = f'original_{input_path}'
    shutil.copy2(input_path, input_path_copy)

    #accelerate_file(input_path)
    blur_file(input_path)
    change_acodec(input_path)
    change_bitrate(input_path)
    change_resolution(input_path)
    create_aecho(input_path)
    create_noise(input_path)
    #darken_video(input_path)
    use_filters(input_path)
    hflip_video(input_path)
    change_metadata(input_path)
    trim_video(input_path)
    slowdown_video(input_path)

    convert_format(input_path)
    change_name(f'{input_path[:-4]}.mov')

if __name__ == '__main__':
    input_path = input("Enter filename path: ")
    process_file(input_path)
