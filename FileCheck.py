# File Check Program 
import os


def main():
	convertedDir = os.listdir(os.getcwd() + "\\output\\mp3")
	sourceDir = os.listdir(os.getcwd() + "\\output\\source")
	for count1 in range(0, len(sourceDir)):
		for count2 in range(0, len(convertedDir)):
			sString = (sourceDir[count1])[0:-4]
			cString = (convertedDir[count2])[0:-4]
			if (sString == cString):
				sourceDir[count1] = "empty"
				convertedDir[count2] = "empty"
			pass
		pass
	pass
	print("Error on source files:")
	for count1 in range(0, len(sourceDir)):
		if (sourceDir[count1] != "empty"):
			print(sourceDir[count1])
		pass
	print("Error on converted files:")
	for count1 in range(0, len(convertedDir)):
		if (convertedDir[count1] != "empty"):
			print(convertedDir[count1])

main()