import flet as ft
import flet_audio as fta

def main(page: ft.Page):
    index = 0
    
# PLAYLIST 

    playlist = [
        {
            "title": "Forget-me-not",
            "artist": "Laufey",
            "album": "A Matter of Time",
            "audio": "audio/Forget-Me-Not.webm",
            "cover": "assets/images/Laufey_-_A_Matter_of_Time.png",
        },
        {
            "title": "My Way",
            "artist": "Frank Sinatra",
            "album": "Nothing But The Best",
            "audio": "audio/My Way (2008 Remastered).webm",
            "cover": "images/MY WAY.jpg",
        },
        {
            "title": "pas de deux",
            "artist": "Tchaikovsky",
            "album": "The Nutcracker",
            "audio": "audio/Tchaikovsky - pas de deux.webm",
            "cover": "images/PAS DE DEUX.jpg",
        },
        {
            "title": "Spring",
            "artist": "Vivaldi",
            "album": "The Four Seasons",
            "audio": "audio/spring.webm",
            "cover": "images/THE FOUR SEASONS.jpg",
        },
        {
            "title": "Winter",
            "artist": "Vivaldi",
            "album": "The Four Seasons",
            "audio": "audio/winter.webm",
            "cover": "images/THE FOUR SEASONS.jpg",
        },
    ]

    titleText = ft.Text("Title: ")
    artistText = ft.Text("Artist: ")
    albumText = ft.Text("Album: ")
    positionText = ft.Text("00:00")

    image = ft.Image(src = "", width=200, height=200)

    def updateSongInfo():
        titleText.value = f"Title: {playlist[index]['title']}"
        artistText.value = f"Artist: {playlist[index]['artist']}"
        albumText.value = f"Album: {playlist[index]['album']}"
        image.src = playlist[index]["cover"]
        page.update()

    async def playAudio(e):
        audio.src = playlist[index]["audio"]
        await audio.play()
        updateSongInfo()

    async def pauseAudio(e):
        await audio.pause()

    async def resumeAudio(e):
        await audio.resume()

    async def skipAudio(e):
        nonlocal index
        index = (index + 1) % len(playlist)
        audio.src = playlist[index]["audio"]
        await audio.play()
        updateSongInfo()

    async def getSongPosition(e=None):
        position = await audio.get_current_position()
        positionText.value = f"{position.minutes:02}:{position.seconds:02}"
        page.update()

    def changeVolume(e):
        audio.volume = volumeSlider.value / 100

    audio = fta.Audio(src =  playlist[index]["audio"], on_position_change=getSongPosition)

    playButton = ft.Button("Play", on_click=playAudio)
    pauseButton = ft.Button("Pause", on_click=pauseAudio)
    resumeButton = ft.Button("Resume", on_click=resumeAudio)
    skipButton = ft.Button("Skip", on_click=skipAudio)

    volumeSlider = ft.Slider(min=0, max=100, value=100, divisions=100, on_change=changeVolume)

    page.add(
        image,
        titleText,
        artistText,
        albumText,
        positionText,
        playButton,
        pauseButton,
        resumeButton,
        skipButton,
        volumeSlider,
    )

    updateSongInfo()

ft.run(main=main, assets_dir="assets")