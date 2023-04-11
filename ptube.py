import pytube
url = input("enter url: ")
vid = pytube.YouTube(url)
Yvideo = vid.streams.filter(file_extension="mp4",progressive=True).order_by('resolution').desc()
Yvideo.get_highest_resolution().download("")