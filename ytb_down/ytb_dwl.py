import youtube_dl
import time
def ytb():
    link_ytb = input('Type the Youtube URL: ')

    ytb_dl = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
    }
    try:
        print('Downloading...\n')
        time.sleep(1)
        with youtube_dl.YoutubeDL(ytb_dl) as ydl:
            ydl.download([link_ytb])
        print('\nMP3 Download Finished!')
    except:
        print("We can't download this audio. Sorry ;(")
ytb()