# youtube-downloader


``` bash
#Установка библиотеки через менеджер пакетов pip:
sudo -H pip install --upgrade youtube-dl

#Другой способ установки библиотеки youtube-dl:
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl

#Ссылка на используемую библиотеку youtube-dl в скрипте:
https://github.com/rg3/youtube-dl/blob/master/README.md

#Команда для запуска скрипта:
python youtube-downloader.py 

#Настраиваемые параметры внутри скрипта:
'ignoreerrors': True/False - отключить/включить пропуск недоступных видео в плейлисте
'--no-warnings': True/False - отключить/включить игнорирование предупреждений
'--ignore-errors': True/False - отключить/включить игнорирование ошибок
'format': - формат и качество аудио/видео
'outtmpl': - название выходного файла (например: его id, заголовок и.т.п)
ydl.download(['Ссылка на канал, видео или плейлист']) - ссылка на скачиваемое видео

```# parser_youtube
# parser_youtube
