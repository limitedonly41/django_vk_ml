import pandas as pd
import requests
import numpy as np
import csv
import time
import datetime
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 
from sklearn.ensemble import ExtraTreesClassifier 
from sklearn.metrics import accuracy_score
import pickle

loaded_model = pickle.load(open('model.sav', 'rb'))

def predict(feature_df):
    # feature_df = pd.DataFrame(feature_dict, index=[0])
    return loaded_model.predict(feature_df)
