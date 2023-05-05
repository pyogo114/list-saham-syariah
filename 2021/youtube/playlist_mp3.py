from pytube import YouTube,Playlist

#NAME = ""
#URLVIDEOPERTAMA = "https://www.youtube.com/watch?v=VVhNsl9afKM&list=PLlK0gGuioshBxyBg4TzEtKETkzOfv4mvB"

NAME = "Sheikh_Mahmoud_Al_Hussary"
URLVIDEOPERTAMA = "https://www.youtube.com/watch?v=VTuUAsROx_s&list=PLlK0gGuioshC8I1zJZb4-vWJwSV9yNV_o"

p = Playlist(URLVIDEOPERTAMA)
print(f'Downloading: {p.title}')

i = 1
for video in p.videos:
    if i<10 :
        angka = "0"+ str(i)
    else:
        angka = str(i)

    audio = video.streams.get_audio_only()
    judul = video.title.replace(" " , "-")
    judul = judul.replace("'" , "")
    judul = judul.replace('"' , '')
    judul = judul.replace(":" , "")
    judul = judul.replace("#" , "")
    judul = judul.replace("|" , "")
    
    print(f"{angka}-{judul}.mp3")
    
    audio.download(filename =f"{angka}-{judul}.mp3")
    i += 1

print("Selesai!")
  
    