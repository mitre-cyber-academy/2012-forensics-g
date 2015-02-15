#!/home/RDOELL/Python26/python.exe
#UPDATED 6/26/12

from PIL import Image
import numpy 
import math
import sys
import os

fPath = 'C:\\Python26\\Stuff\\'
fName = 'genWav.wav'

soundFile = open(fPath + fName, 'rb')


redList = []
greenList = []
blueList = []

statInfo = os.stat(fPath + fName)

count = 0
fData =[]

fData = soundFile.read()
size = len(fData)
print "Size is", size

fDims = numpy.sqrt(size / 3.0)
#fDims represents the side length. Therefore, the size of each color list is going
#to be equal to fDims ** 2.

fDims = int(math.ceil(fDims))
colorLen = fDims ** 2
dataImage = Image.new("RGB", (fDims, fDims), (0,0,0))
#Now, we want to have an offset in our linear data of size equal to
#fDims ** 2.
redList = fData[0:colorLen]
greenList = fData[colorLen: colorLen * 2]
blueList = fData[colorLen * 2:]
print "red size:", len(redList)
print "green size:", len(greenList)
print "blue size:", len(blueList)

if(len(blueList) < len(redList)):
	for i in range(0, len(redList) - len(blueList)):
		blueList += 'A'

print "red size:", len(redList)
print "green size:", len(greenList)
print "blue size:", len(blueList)

rgbData = [None] * colorLen
print len(range(0, colorLen))
print "size of rgbData =", len(rgbData)
print "colorLen size =", colorLen
for i in range(0, colorLen):
	rgbData[i] = (ord(redList[i]), 
			ord(greenList[i]), 
			   ord(blueList[i]))
	

dataImage.putdata(rgbData)
dataImage.save('newChallenging.bmp')
