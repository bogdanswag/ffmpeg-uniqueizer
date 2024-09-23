import ffmpeg
from os import rename
from random import randint

def change_metadata(file):
    output_file = f"changed_metadata_{file}"

    metadata = {
        "title": f"title_metadata_changed{randint(1,1000)}",
        "artist": f"artist_metadata_changed{randint(1,1000)}",
        "comment": "stay fly"
    }

    (
        ffmpeg
        .input(file)
        .output(output_file, **{
            'metadata': f"title={metadata['title']}",
            'metadata': f"artist={metadata['artist']}",
            'metadata': f"comment={metadata['comment']}"
        }, c="copy")
        .run()
    )

    rename(output_file, file)
