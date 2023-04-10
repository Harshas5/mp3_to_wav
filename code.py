from os import path
from pydub import AudioSegment

mp3_file="Argument_1.mp3"
wav_file="Argument_2.wav"
sound = AudioSegment.from_mp3(mp3_file)
sound.export(wav_file, format="wav")