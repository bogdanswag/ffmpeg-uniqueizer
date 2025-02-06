from os import rename

import ffmpeg


def change_bitrate(file):
    output_file = f"changedbitrate_{file}"

    def get_bitrate(file):
        probe = ffmpeg.probe(file)

        video_stream = next(
            (stream for stream in probe["streams"] if stream["codec_type"] == "video"),
            None,
        )
        audio_stream = next(
            (stream for stream in probe["streams"] if stream["codec_type"] == "audio"),
            None,
        )

        video_bitrate = (
            int(video_stream["bit_rate"])
            if video_stream and "bit_rate" in video_stream
            else None
        )
        audio_bitrate = (
            int(audio_stream["bit_rate"])
            if audio_stream and "bit_rate" in audio_stream
            else None
        )

        return video_bitrate, audio_bitrate

    video_bitrate, audio_bitrate = get_bitrate(file)

    if video_bitrate:
        new_video_bitrate = int(video_bitrate * 1.10)
        new_video_bitrate_str = f"{new_video_bitrate // 1000}k"
    else:
        new_video_bitrate_str = None

    if audio_bitrate:
        new_audio_bitrate = int(audio_bitrate * 3)
        new_audio_bitrate_str = f"{new_audio_bitrate // 1000}k"
    else:
        new_audio_bitrate_str = None

    (
        ffmpeg.input(file)
        .output(
            output_file,
            video_bitrate=new_video_bitrate_str,
            audio_bitrate=new_audio_bitrate_str,
            acodec="aac",
        )
        .run()
    )

    rename(output_file, file)
