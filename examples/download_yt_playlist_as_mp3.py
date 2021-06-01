import os

from pytube import Playlist, YouTube

playlist_url = input("Playlist url: ")

playlist = Playlist(playlist_url)

for video in playlist:
    youtube = YouTube(video)

    print(f'\nDownloading - {youtube.title}')

    save_dir = 'downloaded_musics'

    out_file = youtube.streams.get_by_itag('251').download(save_dir)

    out_file_name, _ = os.path.splitext(out_file)

    new_file = f'{out_file_name}.mp3'

    os.rename(out_file, new_file)
