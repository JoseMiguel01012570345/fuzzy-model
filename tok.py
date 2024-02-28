from nltk.corpus import stopwords
import os

os.system("cls")

try:
    import ir_datasets
except:
    os.system("pip install ir-datasets")

try:
    import nltk
except:
    os.system("pip install nltk")
    import nltk
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')
    
try:
    import spacy
    spacy.load("en_core_web_sm")
except:
    os.system("pip install spacy")
    os.system("python -m spacy download en_core_web_sm")

try:
    import nlp
except:
    os.system("pip install nlp")

class Tok:

    doc_tokenized = []
    query_tokeinized=[]
    
    def __init__(self , text):
        
        self.doc_tokenized=self.tokenization_spacy( text)
        self.doc_tokenized=self.remove_noise_spacy( self.doc_tokenized)
        self.doc_tokenized=self.remove_stopwords_spacy(self.doc_tokenized)
        
        pass

    def tokenization_spacy(self , texts):
        nlp = spacy.load('en_core_web_sm')
        return [[token for token in nlp(doc)] for doc in texts]

    def remove_noise_spacy(self, tokenized_docs):

        return [[token for token in doc if token.is_alpha] for doc in tokenized_docs]
    
    def remove_stopwords_spacy(self,tokenized_docs):
  
        stopwords = spacy.lang.en.stop_words.STOP_WORDS
  
        return [
            [token for token in doc if token.text not in stopwords] for doc in tokenized_docs
        ]


doc=["A small group of politicians believed strongly that the fact that Saddam Hussien remained in power after the first Gulf War was a signal of weakness to the rest of the world, one that invited attacks and terrorism. Shortly after taking power with George Bush in 2000 and after the attack on 9/11, they were able to use the terrorist attacks to justify war with Iraq on this basis and exaggerated threats of the development of weapons of mass destruction. The military strength of the U.S. and the brutality of Saddam's regime led them to imagine that the military and political victory would be relatively easy."]
tok=Tok(doc)
print(tok.doc_tokenized)