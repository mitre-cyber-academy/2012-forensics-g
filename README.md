MITRE STEM CTF Summer 2012
Forensics 500 – Multi-Level Steganography
Flag: MCA-00E438E8

Description of challenge:
Participants are provided with an RGB bitmap (bmp) file. The file appears to be made of pseudo-random noise. The participants will have to determine that data is encoded by red, green and blue values, one byte per color. They are arranged from the first third of the relevant data arranged as the red values from left to right, top to bottom, then blue and green. The hint for this is the RIFF plaintext which shows up in the next layer of steganography (this is just built in, not added separately). Once the data is concatenated properly, some junk data guarded by a few ‘A,’s will need to be trimmed out. A hex editor or appropriate C program can do this easily. The example code uses Python and PIL (the Python Imaging Library). The hex editor used was HxD Hex editor.

Once the next file is revealed, a wave (.wav) file, it can be played. At first, it sounds like a poorly done techno remix of the Portal 2 song, ‘Want You Gone.’ Upon further consideration, the quietness of the song and the oddly in-time bloops and beeps can be determined to be data overlayed on top of the song. The principal of this encoding is based on Fourier synthesis of frequencies. To uncover the embedded message, a user should perform a Fourier transform. The example decoding code was written using Matlab, but an equivalent approach using numpy and scipy should be viable (switched to Matlab because of odd memory errors). When looking at using a plot of the FFT, given 4410 points per ‘byte,’ (0.1s at 44100 Hz sample rate), distinct spikes in the graph can be seen at regular intervals. These spikes can be translated into bytes – presence (or lack thereof) represent binary bits. The lower frequencies correspond to less significant bits. When combined, then converted using ASCII, a plaintext document is revealed.

In the case that participants assumed that the flag would be embedded at either the beginning or the end of the document, dummy flags are hidden in those locations. Additionally, false flags are placed throughout the document in the case that participants are simply trolling through the bytes looking for flags of the style ‘MCA-HEXDIGIT.’ The actual flag is embedded in the text of the document, using mis-capitalized words (as in ‘I wAlked across the street’), l33t-sp33k (as in ‘through the dusty a3ther’) and numbers used in odd places, such as punctuation (as in ‘She wouldn’t do that1’). Upon extraction using this more typical steganography, the flag will be revealed and the challenge completed.

Files included:

Generation – 
* flagText.txt
  * This contains a little story about the recent fires with the data embedded in it.
* pyTest.py 
  * Change fPath, fName and coverName to the appropriate values for your setup, in addition to the #! path at the top. The first two represent the path to the file to be embedded. The last represents the file that is being overlayed onto. It should be noted that any data to be overlayed must have less bytes than the cover song has 0.1s segments at 44100 Hz.
* SuperPortalPos.wav
  * A softened, mono, wav version of ‘Want You Gone’ for purposes of overlay
* imager.py
  * This file generates the image from the input files. These are specified using fPath and fName, as before. The output file is ‘Challenging.bmp’ (specified at the end of the file)
Decoding – 

* imgDecoder.py
  * This script takes an image file (specified in fPath and fName) and outputs a wav file (fClear). This simply reverses the operation defined in imager.py
* Decoder.m
  * This decodes the music file at filePath + fileName. It has pre-programmed the frequencies used in generation, in addition to the length of the bytes and the sample rate. It will print out the decoded text string. It uses threshold values for the byte peaks obtained through manual iterative testing.

Challenge

* forensics500.bmp
  * This is the aforementioned challenge BMP.
