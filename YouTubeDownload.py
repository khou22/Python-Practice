# http://willdrevo.com/downloading-youtube-and-soundcloud-audio-with-python-and-pandas/
# http://www.renevolution.com/how-to-install-ffmpeg-on-mac-os-x/
# ^ This is required in order to convert file to mp3
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=ZB_45GFCB50'])
