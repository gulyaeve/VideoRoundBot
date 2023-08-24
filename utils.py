import ffmpeg


async def make_round_video(path: str):
    new_video_path = f"{path.split('.')[0]}_round.mp4"

    video = ffmpeg.input(path)
    audio = video.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
    probe = ffmpeg.probe(path)

    width = probe['streams'][0]['width']
    height = probe['streams'][0]['height']
    if height > width:
        x = 0
        y = (height - width) / 2
        size = width
    elif width > height:
        x = (width - height) / 2
        y = 0
        size = height
    else:
        x = 0
        y = 0
        size = height

    # logging.info(f"{probe['streams'][0]['width']} {probe['streams'][0]['height']}")

    new_video = ffmpeg.crop(video, x, y, size, size)
    new_video = ffmpeg.filter(new_video, 'scale', 400, -1)
    output = ffmpeg.output(audio, new_video, filename=new_video_path)
    ffmpeg.run(output)
    return new_video_path

