# AutoConvertServer v0.2
# By: thatging3rkid

import os
import time
import logging
import threading
import subprocess

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

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
		logging.debug("sleeping")
		time.sleep(15)
	else:
		s = threading.Semaphore(numThreads)
		for dirCount in range(len(inputDir)):
			t = threading.Thread(target=convertThread, args=(dirCount, s))
			threads.append(t)
			t.start()
				
# Function that is threaded that makes the VLC call
def convertThread(index , s):
	logging.debug("in queue")
	with s:
		logging.debug("starting")			
		currentFile = inputDir[index]
		newFile =  currentFile[0: -4] + ".mp3"
		inFile = "\"" + cd + "\\input\\" + currentFile + "\""
		outFileMP = "\"" + cd + "\\output\\mp3\\" + newFile + "\""
		outFileSc = "\"" + cd + "\\output\\source\\" + currentFile + "\""
		callSuccess = subprocess.call("" + vlcDir + "vlc.exe --play-and-exit -I dummy --dummy-quiet " + inFile + " --sout=#transcode{" + \
			"acodec=mp3,vcodec=dummy}:standard{access=file,mux=raw,dst=" + outFileMP + "}")
		logging.debug("in thread")
		os.system("move " + inFile + " " + outFileSc)
	pass				


inputDir = os.listdir("" + os.getcwd() + "\\input")

main()
#make infinite loop in final revision