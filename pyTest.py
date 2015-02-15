#!/home/RDOELL/Python26/python.exe
#Change the above to suit your environment
import numpy
import math
import scipy
from scipy.io import wavfile
import pylab
#Generatens a tone wave, based on the given configurations. Returns a numpy array.
def genWave(frequency, samp, duration, amp):
	freqArray = [880, 1760, 2640, 3520, 4400, 5280, 6160, 7040]
	numDatVals = int(round(samp * duration))
	dat = numpy.empty( numDatVals)
	for t in range(0, int(round(samp * duration))):
		dat[t] = int(round(amp * math.cos((t * 2 * scipy.pi * freqArray[frequency])/samp)))
	return dat


#This function takes a given 'byte' (value as character? Perhaps as an integer...) and converts it
#into a 'binary' representation. This basically represents an array from 0 to 7 which holds bools
# which can be read by MSB to get the value
def byteToBin(rawByte):
	#Have this coming in as a character. Convert it to an integer:
	intByte = ord(rawByte)
	retArray = [None]*8
	#Assuming nothing terrible happened, start parsing:
	for i in range(7, -1, -1):
		if((intByte - (2 ** i)) >= 0):
			retArray[i] = True
			intByte -= 2 ** i
		else:
			retArray[i] = False
	return retArray
		

fPath = 'C:\\Python26\\Stuff\\'
fName = 'flagText.txt'
flagFile = open(fPath + fName, 'r')

fData = flagFile.read()


testString = fData

#This section is where we pull in the file which will store the superimposed data. We'll take the length of the sound, divide it by the length of the data, then use that as the generation time
coverName = "SuperPortalPos.wav"
coverRate, coverData = wavfile.read(coverName)
#Now, the sample rate is samples/sec and the number of samples is data.length. So, to get time, just do length/sample rate
#and to get the time per byte, do (length/sample rate) / len(testString)
time = 0.1
print "Time per byte is", time
print "Given sample rate is", coverRate
print 'Length of string is', len(testString)


#Might want to just make a lookup table of these frequencies if we're going to be using them for 
# a battery of different things. Would make a lot more sense then just generating them every time
# we needed them.
# :) I've wanted to code this up for a long time but I've never had an excuse before. Exciting!

#So, freq0 through freq7 represent the frequencies that are used as bits. When they're
#run through the analyzer, there should show up as binary spikes, and can be checked in later. Yes!

sampleRate = 44100
maxAmp = 1000 # Needs to be loud enough to be clear

fileName = "genWav.wav"

waves = [None] * 8
for i in range(0, 8):
	waves[i] = genWave(i, sampleRate, time, maxAmp)
soundData = [None]*len(testString)
count = 0
for l in testString:
	#Get an empty wave to hold the data in
	currWave = numpy.zeros(waves[0].size)
	currBits = byteToBin(l)
	for i in range(0, 8):
		if(currBits[i]):
			currWave += waves[i]
	soundData[count] = currWave
	
	count += 1
finalData = soundData[0]
count = 1
for l in testString[1:]:
	finalData = numpy.append(finalData, soundData[count])
	count += 1
	
#This should be the final superposition
finalData = numpy.append(finalData, numpy.zeros(coverData.size - finalData.size))
finalData = finalData + coverData
wavfile.write(fileName, sampleRate, finalData.astype(numpy.dtype("i2")))
