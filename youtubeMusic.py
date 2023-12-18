from pytube import YouTube
import moviepy.editor as mp
import os

au = ["https://www.youtube.com/watch?v=Hcc8iDJ89us", "https://www.youtube.com/watch?v=iIaj7qY5Yvs",
	  "https://www.youtube.com/watch?v=kULpMcVOy5I", "https://www.youtube.com/watch?v=zwL1AR_WfNE",
	  "https://www.youtube.com/watch?v=7wFEQeR4kNM"]

def youtubeMusic(url: str, ind: int):
	"""
	Функция скачивает аудиодорожку с youtube видео.
	"""
	audio = YouTube(url)

	audio.streams.get_audio_only().download("C:/Users/tjlik/Desktop")

	title = audio.streams[0].title

	audio = mp.AudioFileClip(f"C:/Users/tjlik/Desktop/{title}.mp4")

	audio.write_audiofile(f"C:/Users/tjlik/Desktop/{ind+29}.wav")

	os.remove(f"C:/Users/tjlik/Desktop/{title}.mp4")

for i in range(len(au)):
	youtubeMusic(au[i], i)