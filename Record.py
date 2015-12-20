import pyaudio
import wave
import numpy
import pylab


FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()
kol_chunk = 0
energy = 101
def func(x):
    return x**2

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
frames =[]
while True:
    y_list = []
    print "recording..."
    while energy > 100:
        data = stream.read(CHUNK)
        kol_chunk += 1
        sum_chunk = []
        decoded = numpy.fromstring(data, 'Int16')
        for j in decoded:
            sum_chunk.append(func(j))
        energy = sum(sum_chunk)
        y_list.append(energy)
    print "finished recording"
    x_list = list(range(kol_chunk))
    pylab.plot(x_list, y_list)
    pylab.show()
    a = input()


# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

"""
print "recording..."


frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print "finished recording"
"""