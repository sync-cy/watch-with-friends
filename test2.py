import pyaudio
import wave
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 512
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "recordedFile.wav"

# length of data to read.
chunk = 1024

# validation. If a wave file hasn't been specified, exit.

'''
************************************************************************
      This is the start of the "minimum needed to read a wave"
************************************************************************
'''
# open the file for reading.
wf = wave.open(WAVE_OUTPUT_FILENAME,'rb')

# create an audio object
p = pyaudio.PyAudio()

# open stream based on the wave object which has been input.
stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# read data (based on the chunk size)
data = wf.readframes(CHUNK)

# play stream (looping from beginning of file to the end)
while data:
    # writing to the stream is what *actually* plays the sound.
    stream.write(data)
    data = wf.readframes(CHUNK)


# cleanup stuff.
wf.close()
stream.close()    
p.terminate()
