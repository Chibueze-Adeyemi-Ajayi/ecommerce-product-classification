import os

from .DeepLearning.DataPipeline import DataPipeline as pipeline
from .DeepLearning.NLP import NLP as _NLP

#/home/devjilo/projects/python/e-commerce-product/myproject/myapp/DeepLearning/dataset/flipkart_fashion_products_dataset.json
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "DeepLearning/dataset/flipkart_fashion_products_dataset.json")
pipeline = pipeline(file_path)
data = []
nlp = []

def beginTraining():
    print("*************Training Initialized**************")
    global data
    data = pipeline.loadData()
    print(data)
    print("***********Data Processing*************")
    data = pipeline.processData()
    print(data)
    global nlp
    nlp = _NLP(data)
    print("**************Splitting dataset*****************")
    X_train, X_test, y_train, y_test = nlp.splitData()
    print("**************Training ML Model*****************")
    nlp.train(X_train, y_train)
    print("Data trained *******************")
    report = nlp.test(X_test, y_test)
    print(report)