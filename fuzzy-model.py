from fuzzywuzzy import fuzz
import os
import ir_datasets
from datamaestro import prepare_dataset
import snippet_extraction as snippet

os.system("cls")
dataset = ir_datasets.load("antique")

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
for query in dataset.queries_iter():    
    i+=1
    with open('./queries/'+ str(i) , 'w') as f:
            f.write(query[1])
        


# ----------------------------------------------------------------->>>>>>>>>

# And we have a query
print("Enter a query:")
query = input()

while query !="":
    # We can use fuzzy string matching to retrieve the document that best matches our query
    scores = [(doc, fuzz.token_set_ratio(query, doc)) for doc in documents]

    # Sort the documents by their score in descending order
    scores.sort(key=lambda x: x[1], reverse=True)

    # Print the best match
    if len(scores) > 0:
        print(f"The document that best matches the query is: '{ snippet.snippet(scores[0][0]) }' with a score of {scores[0][1]}")
    else:
        print("sorry there is no answer for your request")
    
    print("Enter a query:")
    query=input()
