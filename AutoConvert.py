# AutoConvert for VLC. Automatically parses through directory and converts to .mp3s (for the moment)
#
# Made by thatging3rkid
import os
from subprocess import call

def main():
    print("AutoConvert v1.0")
    print("By thatging3rkid, 9/28/2015\n\n")
    # Get Current Directory
    cd = os.getcwd()
    index = -1
    while True:
        # Selects file
        cdFiles = os.listdir(cd + "\\input")
        index += 1
        if (len(cdFiles) == 0) or (len(cdFiles) == index):
            break
        currentFile = cdFiles[index]
        newFile =  currentFile[0: -4] + ".mp3"
        # Debugging
        # print(cd + "\n" + currentFile + "\n" + newFile)
        inFile = "\"" + cd + "\\input\\" + currentFile + "\""
        print(inFile)
        outFile = "\"" + cd + "\\output\\" + newFile + "\""
        x = call("\"C:\\Program Files\\VideoLan\\VLC\\vlc.exe\" --play-and-exit " + inFile + " --sout=#transcode{" + \
            "acodec=mp3,vcodec=dummy}:standard{access=file,mux=raw,dst=" + outFile + "}")
        print("Success" if x == 0 else "Fail")

main()
print("Directory complete!")