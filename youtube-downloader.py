from __future__ import unicode_literals
import youtube_dl

def youtube_dl_hook(d):
    if d['status'] == 'finished':
        print('Загрузка ролика завершена ...')

ydl_opts = {

    'verbose': True,
    'skip_download': True,
    'ignoreerrors': True,
    'writethumbnail': True,
    '--no-warnings': True,
    '--ignore-errors ': True, 
    '--list-thumbnails': True,
    'format': 'best[ext=mp4]',
    'outtmpl': '%(title)s.%(ext)s',
    'noplaylist' : False,
    'progress_hooks': [youtube_dl_hook],
    'postprocessors': [
            {'key': 'EmbedThumbnail',
    	     'already_have_thumbnail': False,
	    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=xyAQtPiKOfA']) 

