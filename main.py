import time
import pyautogui as auto
from PIL import ImageGrab
import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import speech_recognition as sr
import wavio

time.sleep(2)

auto.moveTo(100, 160)
auto.moveTo(400, 300)
auto.click("captureBox.png")
time.sleep(2)
auto.click("sadde.png")
time.sleep(3)
auto.click("playaudio.png")

fs= 44100 #rate
seconds =6 #seconds

recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)#recording sound
sd.wait()#wait given time
wavio.write('audio.wav',recording, fs, sampwidth=2) #save as wav


filename = "audio.wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
print(text)

auto.click("textBox.png")
time.sleep(1)
auto.write(text, interval=0.25)
auto.click("verify.png")
