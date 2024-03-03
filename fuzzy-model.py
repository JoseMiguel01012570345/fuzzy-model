from fuzzywuzzy import fuzz
import os
import ir_datasets
import snippet_extraction as snippet
import tok as token

os.system("pip install spacy")
os.system("python -m spacy download en_core_web_sm")
os.system("pip install nlp")

dataset = ir_datasets.load("antique")

# ---------------------------------------loading database--->>>

documents=[]
try:
    
    for doc in dataset.docs_iter():
        
        with open('./database/'+ snippet.snippet(doc[1]) , 'w') as f:
            f.write(doc[1])
            documents.append(doc[1])
        
            
except  Exception as e:
    print("an error has ocurred: ",e)


dataset = ir_datasets.load("antique/test")

i=0
query_test=[]
for query in dataset.queries_iter():    
    i+=1
    with open('./queries/'+ str(i) , 'w') as f:
            f.write(query[1])
            query_test.append(query[1])  

# ___________________________________________________________________________________
