import tok as token
import os
import bisect

class core:
     
    miu_matrix=[] 
    list_words_database=[]
    database_hased = []
    
    def __init__(self , docs,titles):
        
        # _______________TOKENIZE DOCS________________________
        
        doc_tokenized=[]
        
        for doc in docs: 
            
            tok=token.Tok(doc)
            
            doc_tokenized.append(tok.doc_tokenized)
        
        # _____________________________________________________
        # __________Calculate Miu Matrix_______________________
        
        list_words = self.list_words(doc_tokenized)
        self.list_words_database =  list_words # tuple
        
        cij = self.correlaction_matrix(doc_tokenized,list_words  )
        
        self.miu_matrix = self.miu(cij,list_words,doc_tokenized,titles)
        
        # _____________________________________________________
        
        pass
    
    def miu( self , cij , list_words , database , titles ):
        
        miu_matrix=[]
        
        for index , word1 in enumerate(list_words,start=0):
        
            row=[]
            for title,doc in enumerate(database,start=0):
                
                pi_miu=1
                for index1 , word in enumerate(list_words,start=0):
                    
                    found = bisect.bisect_left(doc, word)

                    if found != len(doc) and doc[found] == word:

                        pi_miu *= 1 - cij[index][index1][2]     
                
                myMiu = miu_word_doc( word1 , doc , (1 - pi_miu), titles[title] ) 
            
                row.append( myMiu )            
            
            miu_matrix.append(row)        
                
        return miu_matrix
    
    def correlaction_matrix(self , doc_tokenized ,list_words): # matrix correlaction
        
        ni=self.ni(doc_tokenized,list_words)
        ni_l=self.ni_nl(doc_tokenized,list_words,ni)
        
        c_matrix=[]
        
        for index1,word1 in enumerate(list_words,start=0):
            
            row=[]
            for index2,word2 in enumerate(list_words,start=0):
                
                if word1 == word2:
                    row.append([word1,word2,1.0])
                    continue
                
                a  =  ni[index1][1]
                b  =  ni[index2][1]
                ab =  ni_l[index1][index2]
            
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
        
        index = bisect.bisect_left( ni, word )

        if index != len(ni) and ni[index] == word:

                return word[1]
        
        return "NaN"
    
    def list_words(self , database):
        
        super_doc=[]
        list_words_hashed = []
        
        for doc in database: # list of all words repeated            
                for word in doc:
                    if super_doc.count(word[1]) >=1 :
                        pass
                    else:
                        super_doc.append(word[1])
        
        for item in super_doc:
            
            hash_value = hash(item)
            list_words_hashed.append((hash_value,item))

        return sorted(list_words_hashed, key=lambda x: x[0])
    
    def ni(self , database , list_words): # number of documents in where appears the world ki
        
        word_frecuency=[]
        
        for word in list_words:
            frecuency=0
            
            for doc in database:
                
                index = bisect.bisect_left(doc, word)

                if index != len(doc) and doc[index] == word:
                
                    frecuency += 1
                                            
            word_frecuency.append([word,frecuency])
        
        return word_frecuency
    
    def ni_nl(self , database , list_words , nii): # number of document in where appears the term ki and the term kl
        
        ni_nl=[]
        for word in range(len(list_words)):
            
            row = []
            for  word2 in range(len(list_words)):
        
                frecuency=0
                if nii[word2][1] == 1 or nii[word][1] == 1:
                        
                        if list_words[word] == list_words[word2]:
                            row.append(1)        
                            
                            continue
                        else:    
                            row.append(0)        
                            
                            continue
                else:
                    
                    if list_words[word] == list_words[word2]:
                        row.append(nii[word][1])        
                        
                        continue
                    
                    for doc in database:
                            
                        index = bisect.bisect_left(doc, list_words[word])
                        index1 = bisect.bisect_left(doc, list_words[word2])
                        
                        if index != len(doc) and doc[index] == word  and index1 != len(doc) and doc[index1] == word2 :
                        
                            frecuency += 1
                
                row.append(frecuency)
            
            ni_nl.append(row)

        return ni_nl  

class miu_word_doc:
    
    word = ""
    doc  = ""
    miu  = 0
    title= ""
    
    def __init__( self, word ,doc ,miu,title):
        
        self.word=word
        self.miu=miu
        self.doc=doc
        self.title = title
