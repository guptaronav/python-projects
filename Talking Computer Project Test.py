from gtts import gTTS
from audioplayer import AudioPlayer
from pygame import mixer
while True:
    print("Enter a Sentence")
    words=input()
    tts = gTTS(words)
    tts.save('/tmp/'+words+'.mp3')
    ##pygame.mixer.init()
    ##pygame.mixer.load('/tmp/'+words+'.mp3')
    ##pygame.mixer.music.play(0)
    AudioPlayer('/tmp/'+words+'.mp3').play(block=True)
