%%
clear
clc
sampleRate = 44100; % Sample rate of recording
filePath = 'C:\Python26\Stuff\'; %Path of directory
fileName = 'genWav.wav'; % Name of file to decode
timeStep = 1 / sampleRate;
L = sampleRate / 10;
%These are the frequencies that are plotted against, and will be constant
f = sampleRate / 2 * linspace(0, 1, L / 2 + 1);
%frequencies:
freqArray = [880, 1760, 2640, 3520, 4400, 5280, 6160, 7040];
%Let's get a mapping of the array indices for the frequencies - 
% Basically, these are what we'll key into to check if the spike exists
indArr = 1:8;
for in = 1:8
    tempInd = find(f == freqArray(in));
    indArr(in) = tempInd;
end

%Now, let's read in the whole file:
data = wavread([filePath fileName]);
%We want to segregate the data into chunks, based on L (the number of
%points)

%The number of chunks is = total points / L:
chunks = floor(size(data, 1) / L);
fprintf('Processing %f chunks\n', chunks);

fprintf('Size of data = %d\n', size(data, 1));
ourString = '';
for currChunk = 1:(chunks - 1)
   Y = fft(data(currChunk * L: (currChunk + 1)* L), L);
   newFF = 2 * abs(Y(1:L/2 + 1)); 
   placeHolder = zeros(1, 8);
   for freqInd = 1:8
       if(newFF(indArr(freqInd)) > 100)
           placeHolder(freqInd) = 1;      
       end
   end
   ourString = [ourString char(bi2de(placeHolder))];
end
ourString
