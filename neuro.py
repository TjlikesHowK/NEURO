import librosa
import librosa.display
import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import csv

def extract_data(audio):
	y, sr = librosa.load(audio)

	features = []
	features.append(audio)

	#MFCC
	features.extend(np.mean(e) for e in librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20))
	features.extend(np.std(e) for e in librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20))

	y_harmonic, y_percussive = librosa.effects.hpss(y)
	features.append(np.mean(y_harmonic))
	features.append(np.std(y_harmonic))
	features.append(np.mean(y_percussive))
	features.append(np.std(y_percussive))

	#CENTROID
	features.append(np.mean(librosa.feature.spectral_centroid(y=y, sr=sr).T, axis = 0)[0])     			# mean
	features.append(np.std(librosa.feature.spectral_centroid(y=y,sr=sr).T, axis = 0)[0])       			# std
	features.append(scipy.stats.skew(librosa.feature.spectral_centroid(y=y,sr=sr).T, axis = 0)[0])    	# skew

	#ROLLOFF
	features.append(np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr).T, axis = 0)[0])      			# mean
	features.append(np.std(librosa.feature.spectral_rolloff(y=y, sr=sr).T, axis = 0)[0]) 				# std

	return features


header = ['filename']
header.extend([f'mfcc_mean{i}' for i in range(1, 21)])
header.extend([f'mfcc_std{i}' for i in range(1, 21)])
header.extend(['har_mean', 'har_std', 'perc_mean', 'perc_std', 'cent_mean', 'cent_std', 'cent_skew', 'rolloff_mean', 'rolloff_std', 'label'])

buffer = []
buffer_size = 5000
buffer_counter = 0

with open('dataset4.csv', 'w', newline='') as file:
	writer = csv.writer(file, delimiter=',')
	writer.writerow(header)
	for i in range(28, 33):
		data = extract_data(f"{i+1}.wav")
		if buffer_counter + 1 == buffer_size:
			buffer.append(data)
			writer.writerows(buffer)
			buffer = []
			buffer_counter = 0
		else:
			buffer.append(data)
			buffer_counter += 1
		print(i)
	if buffer:
		writer.writerows(buffer)

