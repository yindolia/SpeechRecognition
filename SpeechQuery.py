import os
#from os import environ, path
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

import pyaudio
import wave
import audioop
from collections import deque
import time
import math


class SpeechQuery:
	def __init__(self):
		self.CHUNKSIZE= 1024
		self.FORMAT= pyaudio.pyInt16
		self.RATE = 16000
		self.MODELDIR = "/home/ysingh2/AudioScience/sphinx/pocketsphinx/model"
		self.DATADIR = "/home/ysingh2/AudioScience/sphinx/pocketsphinx/test/data/librivox"(
		
		config = Decoder.default_config()
		config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
		config.set_string('-lm', path.join(MODELDIR, 'en-us/en-us.lm.bin'))
		config.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))


		self.decoder = Decoder(config)



	def micSetting(self,sample_size):
		#for getting average sound intensity
		print ("getting mic intensity")
		normRecord= pyaudio.PyAudio()
		normStream = normRecord.open(format= FORMAT, channels= 1, rate= RATE, input = True, frames_per_buffer = CHUNKSIZE)
		normSound= [math.sqrt(abs(audioop.avg(stream.read(CHUNKSIZE),4)))
				   for x in range(sample_size)]
		avgSound = sorted(normSound, reverse = True)
		NormalIntensity = sum(normSound[:int(sample_size * 0.2) / int (sample_size * 0.2)])
		print ("Average intensity is ", NormalIntensity)
		stream.close()
		record.terminate()

		if NormalIntensity < 3000:
			THRESHOLD = 3500
			print("Mic Intensity low, advised to use another mic")
		else:
			THRESHOLD = NormalIntensity+ 100

		return record, 

	def saveWav(self,data, record):
		filename = str(int(time.time()))

		data = ''.join(data)
		signal = wave.open(filename+ '.wav', 'wb')
		signal.setchannels(1)
		signal.setsampwidth(record.get_sample_size(pyaudio.paInt16))
		signal.setframerate(RATE)
		signal.writeframes(data)
		signal.close()
		return filename +'.wav'


	def decodeRecord(self, file):
		self.decoder.start_utt()
		stream = open(path.join(DATADIR, file), 'rb')

		while True:
		  buf = stream.read(self.CHUNKSIZE)
		  if buf:
		    self.decoder.process_raw(buf, False, False)
		  else:
		    break

		decoder.end_utt()
		print ('Best hypothesis segments: ', [seg.word for seg in self.decoder.seg()])
		return [seg.word for seg in self.decoder.seg()]
		
	def runProgram(self):
		self.micSetting(50)
		wf = wave.open
		audRecord= pyaudio.PyAudio()
		audStream = audRecord.open(format= FORMAT, channels= 1, rate= RATE, input = True, frames_per_buffer = CHUNKSIZE)
		print ("Recording")
		while True:
			data = audStream.read(CHUNK)
    		frames.append(data)
		print "finished recording"
			
		recordedSoundFile= saveWav(data, audStream)
		audioDecode= decodeRecord(recordedSoundFile)

		audStream.close()
		audRecord.terminate()

if __name__ == '__main__':
	sq = SpeechQuery()
	sq.runProgram()