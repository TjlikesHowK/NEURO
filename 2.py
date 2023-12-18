import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import librosa
import os
import pathlib

import scipy.optimize as opt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier 

import csv

data = pd.read_csv('dataset3.csv')
y = data['label'].values
x = data[['mfcc_mean2', 'mfcc_mean3', 'mfcc_mean4', 
		'mfcc_mean5', 'mfcc_mean6', 'mfcc_mean7', 'mfcc_mean8', 'mfcc_mean9',
		'mfcc_mean10', 'mfcc_mean11', 'mfcc_mean12', 'mfcc_mean13',
		'mfcc_mean14', 'mfcc_mean15', 'mfcc_mean16', 'mfcc_mean17',
		'mfcc_mean18', 'mfcc_mean19', 'mfcc_mean20', 'mfcc_std1', 'mfcc_std2',
		'mfcc_std3', 'mfcc_std4', 'mfcc_std5', 'mfcc_std6', 'mfcc_std7',
		'mfcc_std8', 'mfcc_std9', 'mfcc_std10', 'mfcc_std11', 'mfcc_std12',
		'mfcc_std13', 'mfcc_std14', 'mfcc_std15', 'mfcc_std16', 'mfcc_std17',
		'mfcc_std18', 'mfcc_std19', 'mfcc_std20', 'har_mean', 'har_std', 'perc_mean', 
		'perc_std', 'cent_mean', 'cent_std', 'cent_skew', 'rolloff_mean', 'rolloff_std']]

X = preprocessing.StandardScaler().fit(x).transform(x)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=27)

clf = svm.SVC(kernel='rbf')   					# core - RBF (радиальная базисная функция)
clf.fit(X_train, y_train)     					
y_pred = clf.predict(X_test) 					

print("Prediction:", y_pred)
print("Real Value:", y_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)*100}%")
print(f"Precision: {precision_score(y_test, y_pred)*100}%")
print(f"Recall: {recall_score(y_test, y_pred)*100}%")
print(f"f1-score: {f1_score(y_test, y_pred)*100}%")
print('CONFUSION_MATRIX :')
print(confusion_matrix(y_test,y_pred))

print()

classifier = KNeighborsClassifier(n_neighbors=6)   #k = 4
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

print("Prediction:", y_pred)
print("Real Value:", y_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)*100}%")
print(f"Precision: {precision_score(y_test, y_pred)*100}%")
print(f"Recall: {recall_score(y_test, y_pred)*100}%")
print(f"f1-score: {f1_score(y_test, y_pred)*100}%")
print('CONFUSION_MATRIX :')
print(confusion_matrix(y_test,y_pred))
  
print()

# gini
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth=3, min_samples_leaf=5) 
clf_gini.fit(X_train, y_train) 
y_pred = clf_gini.predict(X_test)

print("Prediction:", y_pred)
print("Real Value:", y_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)*100}%")
print(f"Precision: {precision_score(y_test, y_pred)*100}%")
print(f"Recall: {recall_score(y_test, y_pred)*100}%")
print(f"f1-score: {f1_score(y_test, y_pred)*100}%")
print('CONFUSION_MATRIX :')
print(confusion_matrix(y_test,y_pred))

#entopry
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100, max_depth = 3, min_samples_leaf = 5) 
clf_entropy.fit(X_train, y_train)
y_pred = clf_entropy.predict(X_test)

print()
print("Prediction:", y_pred)
print("Real Value:", y_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)*100}%")
print(f"Precision: {precision_score(y_test, y_pred)*100}%")
print(f"Recall: {recall_score(y_test, y_pred)*100}%")
print(f"f1-score: {f1_score(y_test, y_pred)*100}%")
print('CONFUSION_MATRIX :')
print(confusion_matrix(y_test,y_pred))