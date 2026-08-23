import tkinter as tk
import vlc
from PIL import Image, ImageTk

# song data used by the music player
song_number = 1
song_info = {
    1: "song - yoshi",
    2: "songgg - yoshi",
    3: "songggg - yoshi",
    4: "song4 - yoshi"
}
songCount = len(song_info)
currentSong = None
isPlaying = False

# prints every song in the playlist - this is the iteration control structure
for number, title in song_info.items():
    print(f"Song {number}: {title}")


def open_player(root):
    # this function builds the music player inside the given window (root)
    # it only runs when called - it does not run on its own
    global currentSong, isPlaying

    win = tk.Frame(root, bg="purple")
    win.grid(row=0, column=0)

    img = Image.open("Yoshify (1).png")
    img = img.resize((250, 250))
    image = ImageTk.PhotoImage(img)

    logo = tk.Label(win, image=image, bg="purple")
    logo.image = image  # keeps a reference so python doesn't delete the image
    logo.grid(row=0, column=1, pady=3)

    songTitleAndArtist = tk.Label(win, text=song_info[song_number], font=("Arial", 24, "bold"), bg="purple", fg="white")
    songTitleAndArtist.grid(row=7, column=1, pady=100)

    # starts playing the first song as soon as the player opens
    currentSong = vlc.MediaPlayer(f"songs/{song_number}.mp3")
    currentSong.play()
    isPlaying = True

    def startStopMusic():
        # this is for the play button so it can start and stop playing the songs
        global isPlaying
        if isPlaying:
            isPlaying = False
            currentSong.set_pause(1)
        else:
            isPlaying = True
            currentSong.set_pause(0)

    def skipCurrentSong():
        # this is to skip the song thats currently playing
        global currentSong, song_number
        currentSong.stop()
        if song_number == songCount:
            song_number = 1
        else:
            song_number = song_number + 1
        currentSong = vlc.MediaPlayer(f"songs/{song_number}.mp3")
        # getting the song from the vlc media
        currentSong.play()
        songTitleAndArtist.config(text=song_info[song_number])

    def previousSong():
        global currentSong, song_number
        currentSong.stop()
        if song_number == 1:
            song_number = songCount
        else:
            song_number = song_number - 1

        currentSong = vlc.MediaPlayer(f"songs/{song_number}.mp3")
        currentSong.play()
        songTitleAndArtist.config(text=song_info[song_number])

    def changeVolume(value):
        # this line sets the volume to the value the slider gives it
        currentSong.audio_set_volume(int(value))

    startBtn = tk.Button(win, text="Play/Pause", fg="red", command=startStopMusic)
    startBtn.grid(row=4, column=1, padx=5)

    nextBtn = tk.Button(win, text="Skip track", fg="red", command=skipCurrentSong)
    nextBtn.grid(row=4, column=2, padx=5)

    prevBtn = tk.Button(win, text="Previous track", fg="red", command=previousSong)
    prevBtn.grid(row=4, column=0, padx=5)

    volumeLabel = tk.Label(win, text="Volume", bg="purple", fg="white")
    volumeLabel.grid(row=2, column=1, padx=5)

    volumeSlider = tk.Scale(win, from_=0, to=100, orient="horizontal", length=200, command=changeVolume, bg="purple", fg="white")
    volumeSlider.grid(row=1, column=1, padx=5)

    win.mainloop
