import pandas as pn
import spacy as sp

class DataPipeline:
    
    def __init__(self, path):
        self.path = path
        self.nlp = sp.load("en_core_web_md")
        
    def addPath(self, path):
        self.path = path
        
    def loadData(self):
        self.pn = pn.read_json(self.path)#[0:50]
        self.pn.fillna("N/A", inplace=True)
        return self.pn
    
    def processText(self, text):
        doc = self.nlp(text); output = []
        for token in doc:
            if token.is_stop or token.is_punct:
                continue
            else:
                output.append(str(token))
        return " ".join(output)
    
    def textToVec (self, text):
        doc = self.nlp(text)
        return doc.vector
    
    def processData(self): 
        self.pn["Description"] = self.pn["description"].apply(lambda data: self.textToVec(self.processText(data)))
        return self.pn