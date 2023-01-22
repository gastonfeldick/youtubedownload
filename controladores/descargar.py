from pytube import YouTube

yt=YouTube("https://www.youtube.com/watch?v=qvBos9LTAZQ&t=1929s&ab_channel=ElTofas")

audio=yt.streams.get_audio_only()
audio.download(filename="ROCK NACIONAL ARGENTINO - ENGANCHADO.mp3")
