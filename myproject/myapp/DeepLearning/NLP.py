import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score

class NLP:
    
    def __init__(self, data):
        self.data = data
        self.knn = KNeighborsClassifier(n_neighbors=5)
        
    def splitData (self):
        return train_test_split(self.data["Description"], self.data["sub_category"], test_size=.25)
    
    def train (self, X_train, y_train):
        X_train = np.stack(X_train)
        self.knn.fit(X_train, y_train)
        
    def test (self, X_test, y_test):
        X_test = np.stack(X_test)
        pred = self.knn.predict(X_test)
        return classification_report(y_test, pred)
    
    def classify (self, vector):
        vector = np.stack([vector])
        return self.knn.predict(vector)
    
    def getAccuracy (self, clf):
        return accuracy_score(clf)