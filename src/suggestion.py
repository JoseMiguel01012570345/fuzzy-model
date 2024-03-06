import core
import os
import entry
class suggestion:
    
    miu_query_per_doc=[]
    list_combination = []
    
    def __init__( self, query: entry.entry, miu_matrix: core.core, query_to_show ):   
        
        list_words = miu_matrix.list_words_database # list of the words in database
        
        numb_variables = query.number_variables # number of variable
        
        query_simplied = query.query_simplied # query simplied
        
        query_v =query.query_v
        
        matrix_docs = miu_matrix.miu_matrix # miu matrix for searching
        
        if numb_variables <= 23: # more than 23 variables takes more than a second for a model to answer
            
            self.list_combination = []
        
            list_combinations =  self.combinations(numb_variables,[]) # all combinations for the query
            
            good_combinations =  self.evaluate_expresion(query_v,list_combinations) # combinations that results in 1
            
            list_query_words =   self.list_query_words(query_simplied)
        
            doc_socored = self.miu_query_per_doc(list_query_words,matrix_docs,good_combinations,list_words)

            filtered_doc = self.filter_doc(doc_socored)
        
            self.print_doc(filtered_doc,query_to_show)
            
        else:
            
            # code for the min-max effort

            pass
        
        
        pass
    
    # ______________________________Query_Evaluation______________________
    
    def combinations( self , num: int , combination: list ):
            
        if num == 0:
            
            row=[]
            for item in combination:
                row.append(item)
                
            self.list_combination.append(row)    
            return
        
        combination.append(1)
        
        self.combinations( num-1 , combination)
        
        combination.pop()
        
        combination.append(0)

        self.combinations( num - 1 , combination)
    
        combination.pop()
        
        return self.list_combination

    def evaluate_expresion( self , query , list_combinations ):
        
        result=[]

        for combination in list_combinations:
            
            new_query = self.remplace_values(query,combination)
            r = self.evaluate(query=new_query)
            
            if r == 1 or r == True :
                result.append(combination)
            
        return result
    
    def remplace_values( self , query , combination ):
        
        num_variable = 0
        new_query=[]
        
        for variable in  query:
            
            if variable == "v":
                  
                new_query.append(combination[num_variable])
                
                num_variable += 1
              
            else:
                new_query.append(variable)
        
        return new_query
    
    def evaluate( self , query , pointer = 0 ):
        
        stack=[]
        index=pointer
        
        while index < len(query) :
            
            if query[index] == "(":
                
                stack_aux = self.evaluate( query , index + 1 )
                
                for i in stack_aux[0]:
                    stack.append(i) 
                
                index = stack_aux[1]           

            elif query[index] == ")":
                
                stack = [self.boolean_expression(stack)]
                
                return (stack,index )
            
            else:
                stack.append(query[index])
                
            index += 1
                
        if len(stack) != 1:
        
            result = self.boolean_expression(stack)
        
            return result
        
        else:
            return stack[0]      
        
    def boolean_expression( self , expression):
        
        result=0
        i = 0
        evaluated = False
        stack=[expression[0]]
        pointer=0
        
        while i < len(expression):
            
            if expression[i] == "or" and expression[ i + 1 ] == "not" :
                
                exp = self.solve_not_expression(expression[i+1:])
                
                result = exp[0]
                
                result =  int(stack[pointer]) or result
                
                stack.append(result)
                pointer += 1
               
                i += exp[1] + 2
                
                evaluated = True
                
                continue
            
            elif expression[i] == "or" and expression[ i + 1 ] != "not" :
                
                
                result =  int(stack[pointer]) or int(expression[i+1])
                
                stack.append(result)
                pointer += 1
                
                i+=2
                
                evaluated = True
                
                continue
            
            if expression[i] == "and" and expression[ i + 1 ] == "not" :
                
                exp = self.solve_not_expression(expression[i+1:])
                
                result = exp[0]
                
                result =  int(stack[pointer]) and result
                
                stack.append(result)
                pointer += 1
                
                i += exp[1] + 2
                
                evaluated = True
                
                continue
            
            elif expression[i] == "and" and expression[ i + 1 ] != "not" :
                
                result =  int(stack[pointer]) and int(expression[i+1])
                
                i+=2
                
                stack.append(result)
                pointer += 1
                
                evaluated = True
                
                continue
                
            elif expression[ i ] == "not" :
            
                exp = self.solve_not_expression(expression[i+1:])
                
                result = not exp[0]
                
                stack.append(result)
                pointer += 1
                
                i += exp[1] + 2
            
                evaluated = True
            
                continue
            
            i += 1
            
        if not evaluated :
            
            result = expression[0]
        
        return result
    
    def solve_not_expression( self , expression ):
        
        result=0
        num_not=0
        
        for item in expression:
            
            if item == "not":
               num_not += 1

            else:
                result = int(item)
                break
                
        if num_not % 2 == 0:
            
            return (  result , num_not )
        else:
            
            return ( not result , num_not )
    
    def query_word( self , query_simplied):
        
        keywords=["or","and","not","(",")"]
        list_query_words=[]
        
        for item in query_simplied:
            
            memebership = True
            
            for kw in keywords:
                
                if kw == item:
                    
                    memebership = False
                    break        
            
            if memebership:
                list_query_words.append(item)        
              
        return list_query_words
    
    #____________________________________________________________________
    
    def list_query_words( self , query_simplied:list ):
        
        keyword=["(",")","or","and","not", " ",""]
        list_words_query = []
        
        for word in query_simplied:
            
            if word not in keyword:
                list_words_query.append(word)
                    
        return list_words_query
        
    def miu_query_per_doc(self , list_query_words: entry.entry.query_simplied , matrix_doc: core.core.miu_matrix , good_combinations ,list_words ):
        
        list_index_per_query_word = self.query_word_index_in_database(list_words,list_query_words)
        
        list_ki_miu_kij=[]
        num_docs=0
        for index in list_index_per_query_word: # pick all miu_ij such that i is the query term and j is the document
            
            miu_ki = matrix_doc[index]
            num_docs= len(miu_ki)
            
            miu_kij=[]
            
            for doc in miu_ki:
            
                miu_kij.append([doc.miu,doc.title])
            
            list_ki_miu_kij.append(miu_kij)
        
        doc_scored=[]
        for i in range(num_docs): # score all documents
            
            miu_qj=1
            doc=""
            for combination in good_combinations: 
                
                result=1
                for j in range(len(list_index_per_query_word)):
                    
                    doc = list_ki_miu_kij[j][i][1]
                    if combination[j] == 1:
                        result *= list_ki_miu_kij[j][i][0]
                    else:
                        result *= 1 - list_ki_miu_kij[j][i][0]

                miu_qj *= 1 - result
            
            doc_score = 1 - miu_qj
            
            doc_scored.append([ doc_score , doc ])
        
        return sorted(doc_scored,key=lambda x : x[0])
    
    def filter_doc(self, ranked_docs):
        
        filtered_docs=[]
        for scored_doc in ranked_docs:
            
            doc = scored_doc
            filtered_docs.append(doc)
        
        return filtered_docs
    
    def print_doc( self , docs , query ):
        
        import os
        
        os.system("cls")
        
        if len(docs) == 0:
            
            print("\033[1;31;43m >>>> SORRY THERE IS NOTHING TO SHOW :( , TRY AGAIN \033[0;37m")
            return
            
        docs = docs[::-1]
        
        print(f"\033[1;32m QUERY >> {query} ")
        for index,doc in enumerate(docs,start=0):
            
            print(f"\033[1;34m                            DOCUEMNT {index}.                           ")
            print(f"\033[4;36m {doc}")
        

    def query_word_index_in_database( self , list_words , list_query_words ):
        
        list_index_per_word = []
        for query_word in list_query_words:
            
            index = self.search_word_in_database(list_words,query_word)
            
            if index != "NaN":
                
                list_index_per_word.append( index )
        
        return list_index_per_word
    
    def search_word_in_database( self , list_word , target):
        
        for index,word in enumerate(list_word,start=0):
            
            if word[1] == target:
                return index
        
        return "NaN"