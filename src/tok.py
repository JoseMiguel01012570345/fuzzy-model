from nltk.corpus import stopwords
import spacy
import nltk

class Tok:

    doc_tokenized = []
    doc_hashed_tokenized = []
    
    def __init__(self , text = " " , title = "" ):
        
        self.doc_tokenized=self.tokenization_spacy( text)
        self.doc_tokenized=self.remove_noise_spacy( self.doc_tokenized )
        self.doc_tokenized = self.remove_stopwords_spacy(self.doc_tokenized)
        
        pass

    def tokenization_spacy(self , texts):
        
        global tokenized_docs
        tokenized_docs = [nltk.tokenize.word_tokenize(doc) for doc in texts]
        
        result=[]
        
        word=""
        for item in tokenized_docs:
            
            if len(item) > 0 :
                if item[0] != " " :
                    if item[0] != "" :
                
                        word += item[0]
            
            elif word != "":
                result.append(word)
                word=""
        
        return result

    def remove_noise_spacy(self, tokenized_doc):
        
        result =[]  
        for token in tokenized_doc:
                if str(token).isalpha:
                    result.append(token)
        
        return result
    
    def remove_stopwords_spacy(self,tokenized_doc):
        
        stopwords = set(nltk.corpus.stopwords.words('english'))

        result =[]  
        
        for token in tokenized_doc:
            
                if token not in stopwords:
                    
                    token = str.lower(token)
                    hash_value = hash(token)
                    result.append((hash_value,token))

        return (sorted(result, key=lambda x: x[0]))
    
