import os
import ir_datasets
import snippet_extraction as snippet
import core
import entry
import suggestion

# os.system("pip install spacy")
# os.system("python -m spacy download en_core_web_sm")
# os.system("pip install nlp")
# os.system("cls")

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

os.system("cls")
myCore = core.core(documents)

query = "hello world cuba mama"
while True:
    
    myEntry = entry.entry(query)
    suggested_docs = suggestion.suggestion( myEntry , myCore )

    print("input your query: ")
    query = input()
