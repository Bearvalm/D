import numpy as np
from scipy.spatial.distance import euclidean, correlation
import librosa
import misc
from tkinter import filedialog

from dtw import dtw
from numpy.linalg import norm


hop_size = 2205
n_fft = 4410
delta = 1


def getDataSet(directory):
	files = misc.getAudioFilesFromDisk(directory)
	audioData = {}

	for file in files:
		x, fs = librosa.load('{}/{}'.format(directory, file))
		x *= (delta / max(x))

		mfcc = librosa.feature.mfcc(x, fs)

		audioData[file] = mfcc

	return audioData


directoryLearning = './learning_data/'

directoryTesting = filedialog.askdirectory()

learningDataSet = getDataSet(directoryLearning)
testingDataSet = getDataSet(directoryTesting)


learningNames = ['выполнить', 'создание', 'сохранение', 'удаление', 'отмена',
                 'запуск', 'редактирование', 'переход', 'файла', 'папка']

learningNames += ['переход_файл', 'переход_папка']

resultingData = {}

for testFile, testFeature in testingDataSet.items():
	tempRes = []
	for lrnFile, lrnFeature in learningDataSet.items():
		fileDistance = 0
		dist, cost, acc_cost, path = dtw(testFeature.T, lrnFeature.T, dist=euclidean)

		tempRes.append([dist, lrnFile])

	tmp = {name: [0, 0] for name in learningNames}
	for value, name in tempRes:
		tmp[ name[ : name.rfind('_')] ][0] += value
		tmp[ name[ : name.rfind('_')] ][1] += 1

	tempRes = [[value[0]/float(value[1]), name] for name, value in tmp.items()]

	resultingData[testFile] = min(tempRes)


tempRes = ['{} *** {} == {}'.format(testFile, lrnArgs[1], lrnArgs[0])
           for testFile, lrnArgs in resultingData.items()]
resultingStr = '\n'.join(tempRes)

print(resultingStr)
