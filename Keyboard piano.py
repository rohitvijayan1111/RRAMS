import numpy
import tkinter
import time
from scipy.io.wavfile import write
sample = 44000

def waves(freq,duration = 0.5):
        amplitude = 4100
        t = numpy.linspace(0, duration, int(sample*duration))
        wave = amplitude * numpy.sin(2 * numpy.pi * freq * t)
        return wave

def notes():
        octaves = ["C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "A", "a", "B", "b"]
        bfreq = 261.63
        notefreq = {}
        for i in range(len(octaves)):
                notefreq[octaves[i]] = bfreq*pow(2,(i/12))
        notefreq[""] = 0
        return notefreq

def songs(music):
        notefreq = notes()
        song = []
        for note in music.split('-'):
                x = waves(notefreq[note])
                song.append(x)
        song = numpy.concatenate(song)
        return song.astype(numpy.int16)

def main():
        music = "E-e-E-e-E-e-E-G-C-D-E-F-f-F-f-F-E-E-e-e-E-D-D-E-D-G-E-E-e-e-e-e-E-G-C-D-E-F-f-F-f-F-E-e-E-e-G-C-F-D-C"#To be inputted using mayank's code
        data1 = songs(music)
        name = input("Enter name of song file")
        name = name+".wav"
        print(name, "is downloaded in your pc..!!")
        write(name, sample, data1.astype(numpy.int16))


main()
