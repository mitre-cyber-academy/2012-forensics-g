#!/home/RDOELL/Python26/python.exe

from PIL import Image
#fPath = 'C:\\Python26\\Stuff\\'
fPath = 'C:\\Documents and Settings\\rdoell\\Desktop\\Forensics500_RDoell\\'
#fName = 'Challenging.bmp'
fName = 'newChallenging.bmp'
fClear = 'Clearer.wav'


dataImg = Image.open(fPath + fName)


redList = []
greenList = []
blueList = []

count = 0
for i in list(dataImg.getdata()):
	redTemp, greenTemp, blueTemp = i
	redList.append(redTemp)
	greenList.append(greenTemp)
	blueList.append(blueTemp)
	count += 1

finalData = redList
finalData.extend(greenList)
finalData.extend(blueList)
fClearer = open(fPath + fClear, 'wb')
for byte in finalData:
	fClearer.write(chr(int(byte)) + "")

fClearer.close()
