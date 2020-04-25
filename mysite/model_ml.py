import joblib 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
from sklearn import tree
# We use 30 trees only because that seems to give best accuracy after some trial and error
# (although it varies because of randomness becuase of not fixing seed for split)
clf = RandomForestClassifier(n_estimators=30)


def train():
    df = pd.read_csv("output_19_04.csv")

    # Remove strings out of features since the features should only contain numbers, and booleans
    features = df[[
        "IsCity",
        "IsProfile",
        "IsLinks",
        "FriendCount",
        "PhotoCount",
        "PagesCount",
        "FollowersCount",
        "AlbumsCount",
        "VideosCount",
        "AudiosCount",
        "OfflineDays",
        "HasPhoto",
        "Site",
        "Career",
        "Education",
        "following_followers_ratio",
        "following_photos_ratio",
        "followers_photos_ratio"
        ]]
    label = df["rating"]

    # split the dataset
    features_train, features_test, label_train, label_test = train_test_split(
            features, label, test_size=0.30, random_state=0)

    # Apply Random Forest Classifier
    clf.fit(features_train, label_train)

    # Test it
    label_prediction = clf.predict(features_test)
    acc = metrics.accuracy_score(label_test, label_prediction)
    
    tn, fp, fn, tp = metrics.confusion_matrix(label_test, label_prediction).ravel()
    # print("False Positive rate: ", fp / (tn + fp + fn + tp))
    return acc
# Load the model from the file 
  
# Use the loaded model to make predictions 
def predict(feature_dict):
    feature_df = pd.DataFrame(feature_dict, index=[0])
    result = str(clf.predict(feature_df)).strip('[]')
    result = int(result) 
    return result
