import tok as token
import os

class core:
     
    miu_matrix=[] 
    
    def __init__(self , docs):
        
        doc_tokenized=[]
        
        for doc in docs:
            tok=token.Tok(doc)
            doc_tokenized.append(tok.doc_tokenized)
            
        print(doc_tokenized)
        list_words = self.list_words(doc_tokenized)
        cij        = self.correlaction_matrix(doc_tokenized,list_words)
    
        self.miu(cij,list_words,doc_tokenized)
        
        pass
    
    def miu( self , cij , list_words , database ):
        
        miu_matrix=[]
        
        for index , word1 in enumerate(list_words,start=0):
        
            row=[]
            for doc in database:
            
                for token in doc:
                    
                    pi_miu=1
                    for index1 , word in enumerate(list_words,start=0):
            
                        if  token.count(word) >=1 :
                            
                            pi_miu *= 1 - cij[index][index1][2]     
                
                row.append( 1 - pi_miu )            
            
            print(row)
            miu_matrix.append        
                
        pass
    
    def correlaction_matrix(self , doc_tokenized ,list_words): # matrix correlaction
        
        ni=self.ni(doc_tokenized,list_words)
        ni_l=self.ni_nl(doc_tokenized,list_words,ni)
        
        c_matrix=[]
        
        for word1 in list_words:
            
            row=[]
            for word2 in list_words:
                
                if word1 == word2:
                    row.append([word1,word2,1.0])
                    continue
                
                a  =  self.search_in_ni(ni,word1)
                b  =  self.search_in_ni(ni , word2)
                ab =  self.search_in_ni_nl(ni_l,word1,word2)
                
                if a != "NaN" and b != "NaN" and ab != "NaN" :
                    
                    cij= ab /  (a + b - ab )
                    row.append( [ word1 , word2 , cij] )
            
            c_matrix.append(row)
            
        return c_matrix
    
    def search_in_ni_nl( self , ni_nl , word1 ,word2 ):
        
        for triple in ni_nl:
            
            if triple[0] == word1:
                
                if triple[1]==word2:
                    return triple[2]
                
                for triple1 in ni_nl:
                    
                    if  triple1[0] == word1 and triple1[1] == word2:
                        return triple1[2]
                
                    
            elif triple[0] == word2:
                
                if triple[1]==word1:
                    return triple[2]
                
                for triple1 in ni_nl:
                    
                    if  triple1[0] == word2 and triple1[1] == word1:
                        return triple1[2]
                
        return "NaN"
    
    def search_in_ni( self , ni , word ):
        
        for pair in ni:
            
            if pair[0] == word:
                return pair[1]
        
        return "NaN"
    
    def list_words(self , database):
        
        super_doc=[]
        for docs in database: # list of all words repeated
            for doc in docs:
                for word in doc:
                    if super_doc.count(word) >=1 :
                        pass
                    else:
                        super_doc.append(word)
        
        return super_doc  
    
    def ni(self , database , list_words): # number of documents in where appears the world ki
        
        word_frecuency=[]
        
        for word in list_words:
            frecuency=0
            
            for doc in database:
                
                for token in doc:
                    
                    if  token.count(word) >=1 :
                        frecuency += 1
                                            
            word_frecuency.append([word,frecuency])
        
        return word_frecuency
    
    def ni_nl(self , database , list_words , nii): # number of document in where appears the term ki and the term kl
        
        ni_nl=[]
        for word in range(len(list_words)):
            
            for  word2 in range(len(list_words)):
        
                frecuency=0
                if nii[word2][1] == 1 or nii[word][1] == 1:
                        
                        if list_words[word] == list_words[word2]:
                            ni_nl.append([ list_words[word],list_words[word2],1])        
                            
                            continue
                        else:    
                            ni_nl.append([ list_words[word],list_words[word2],0])        
                            
                            continue

                else:
                    
                    if list_words[word] == list_words[word2]:
                        ni_nl.append([ list_words[word],list_words[word2],nii[word][1]])        
                        
                        continue
                    
                    for doc in database:
                        
                        for token in doc:
                            
                            if  token.count( list_words[word] ) >= 1 and token.count( list_words[word2] ) >= 1 :
                                frecuency += 1
                    
                ni_nl.append([ list_words[word],list_words[word2],frecuency])

        return ni_nl  

os.system("cls")

docs = [ ["A B C"] , ["A B"] , ["A X"] , ["A Q"] , ["D F"] , ["B X"] ]

cor=core(docs)

