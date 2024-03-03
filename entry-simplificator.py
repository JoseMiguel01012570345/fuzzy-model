import os

class entry:
    
    def __init__( self , query ):

        query_simplified = self.query_to_array(query)        
        query_simplified = self.init_parser(query_simplified)
        bracket_location = self.bracket_checker(query_simplified)
        
        
        print(bracket_location)
        
        pass
    
    def query_to_array( self , query ):
        
        import re

        # Regular expression pattern to split by spaces, "or", "and", "not"

        pattern = r"(\(|\)|or|and|nor)"

        # Split the string using the pattern
        result = re.split(pattern, query)

        # Remove empty strings from the result (if any)
        result = [word for word in result if word != " " and word != "" ]

        return result
    
    def init_parser(self , query_array ):
        
        for item in range(len(query_array)):
            
            if  query_array[item] != "not" and \
                query_array[item] != "and" and \
                query_array[item] != "or"  and \
                query_array[item] != "("   and \
                query_array[item] != ")":
            
                    query_array[item] = "E"         
            
        return query_array
    
    def bracket_checker(self,query_array): # returns a bracket location array or false if there is missmatch
       
        bracket_open=0;
        bracket_closed=0
        bracket_location=[]
        
        i=0
        for token in range(len(query_array)):
           
            if query_array[token] == "(":
               
               bracket_open += 1
               bracket_location.append(token)
            
            if query_array[token] == ")":
                
                bracket_closed   += 1
                bracket_location.append(token)
            
            if bracket_closed > bracket_open:
                return False
         
        if bracket_open != bracket_closed:
            return False 
       
        return bracket_location

    def expression_parser( self ,query_simplied , bracket_location ,i):
        
        s="( ( E ) or ( E ) ) and ( E )"
        new_query
        if bracket_location[i] < bracket_location[-i]:
        
            new_query = self.expression_parser( query_simplied , i + 1 )
            
        else: 
            return ""
        
        s=""
        
        for element in query_simplied[bracket_location[i] + 1 : bracket_location[ i+1 ]]:
            
            s += query_simplied[element] 
            
        s += new_query
        
        if bracket_location[ i + 1 ] + 1 < len(query_simplied):
        
            for element in query_simplied [ bracket_location[i+1] + 1 : bracket_location[i+2] - 1 ]:
                

                
                        
                
                pass 
        
        else:
            return ""
                
        
        return True
    
    def expression_production():
        pass
    
    
    
    def check_syntaxis( self , query ):
        
        for i in range(len(query)):
            
            if  query[i] == "or" or query[i] == "and" : 
                
                try:
                    
                    query[i-1] == "E"
                    
                    if query [i+1] == "E":
                        query[i]="E"                
                    
                    elif query[i+1] == "not" and query[i+2] == "E":                        
                        query[i] = "E"    
                            
                except:
                    return False
            
            if query[i] == "not" and  query[i+1] == "E" :

                    query[i] = "E"    
    
        for item in query:
            
            if item != "E":
                return False
            
        return query
        

os.system("cls")

ent=entry("( ( machine learning and not malanga ) or python) and sistema" )
