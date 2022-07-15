import moviepy.editor as mp


def change_audio(video_path):
    audio = mp.AudioFileClip('data/media/amor.mp3')
    video = mp.VideoFileClip(video_path)
    final_video = video.set_audio(audio)
    final_video.write_videofile("data/media/tmp_out.mp4")
    return True
