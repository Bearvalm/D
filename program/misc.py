import os


def getAudioFilesFromDisk(directory, extensions={'ogg', 'mp3', 'aac' 'ac3', 'wav'}):
	files = os.listdir(directory)
	filterFunction = lambda x: any([x.endswith(extension) for extension in extensions])
	audioFiles = list(filter(filterFunction, files))
	return audioFiles

