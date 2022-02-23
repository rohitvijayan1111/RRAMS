#import tkinter
#import pyaudio
import wavio
import sounddevice as device
import pydub
from pydub.playback import play
from scipy.io.wavfile import read
import numpy
import math
import statistics


def record():
    fs = 44100  # sampling frequency sometimes it is 44800
    record_time = 10
    recording = device.rec(int(record_time * fs), samplerate=fs, channels=1)

    print("Recording..")
    device.wait()
    print("Recordind over")
    a = input("Enter the name of the file to be stored") + ".wav"
    wavio.write(a, recording, fs, sampwidth=2)
    return a

b=record()
"""

song = pydub.AudioSegment.from_wav("amma.wav")
play(song)

samprate,wavdata=read("amma.wav")
chunks=numpy.array_split(wavdata,wavdata.size/(samprate/2))

dbs=[20*math.log10((statistics.mean(chunk**2)))for chunk in chunks]
print(dbs)
"""







