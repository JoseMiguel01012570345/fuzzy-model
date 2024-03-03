from nltk.corpus import stopwords
import os
import spacy
import nlp
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
    
    # def flat_list(self , words):
        
    #     import numpy as np
        
    #     # Load Spacy model
    #     nlp = spacy.load("en_core_web_sm")

    #     # Calculate cumulative lengths
    #     lengths = np.cumsum([0] + list(map(len, words)))

    #     # Flatten the list
    #     flat_words = [item for sublist in words for item in sublist]

    #     FLAT_WORDS = [nlp.make_doc() for word in flat_words]

    #     # Create a Spacy Doc
    #     doc = spacy.tokens.Doc(nlp.vocab, words=FLAT_WORDS)

    #     # Initialize the output list
    #     lemmatized = []

    #     # Iterate over spans and lemmatize tokens
    #     for index in range(1, len(lengths)):
    #         span = doc[lengths[index - 1]:lengths[index]]
    #         lemmatized.append([token.lemma_ for token in span])
            
    #     return lemmatized
    
    def remove_stopwords_spacy(self,tokenized_docs):
  
        stopwords = spacy.lang.en.stop_words.STOP_WORDS
  
        return [
            [token.text for token in doc if token.text not in stopwords] for doc in tokenized_docs
        ]