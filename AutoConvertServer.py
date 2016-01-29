# AutoConvertServer v0.1
# By: thatging3rkid

import os
import time
import threading
import subprocess

# Some global pre-defs
global threads
threads = []
global inputDir
numThreads = 2
vlcDir = "" + os.getcwd() + "\\vlc\\"
cd = os.getcwd()


# Main function
def main():
	if (len(inputDir) == 0):
		time.sleep(60)
		print("sleeping")
	else:
		s = threading.Semaphore(numThreads)
		for dirCount in range(len(inputDir)):
			t = threading.Thread(target=convertThread, args=(dirCount, s))
			threads.append(t)
			t.start()
				


# Function that is threaded that makes the VLC call
def convertThread(index , s):
	print("in queue")
	with s:
		print("starting")			
		currentFile = inputDir[index]
		newFile =  currentFile[0: -4] + ".mp3"
		inFile = "\"" + cd + "\\input\\" + currentFile + "\""
		outFileMP = "\"" + cd + "\\output\\mp3\\" + newFile + "\""
		outFileSc = "\"" + cd + "\\output\\source\\" + currentFile + "\""
		callSuccess = subprocess.call("" + vlcDir + "vlc.exe --play-and-exit -I dummy --dummy-quiet " + inFile + " --sout=#transcode{" + \
			"acodec=mp3,vcodec=dummy}:standard{access=file,mux=raw,dst=" + outFileMP + "}")
		print("in thread")
		os.system("move " + inFile + " " + outFileSc)
	pass

while True:
	inputDir = os.listdir("" + os.getcwd() + "\\input")
	main()
