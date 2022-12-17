#pip install pytube
import pytube
link = input("link: ")
yt= pytube.YouTube(link)
yt.streams.first().download()
print('Downloaded, link')