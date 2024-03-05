import os
    
class entry:
    
    query_simplied=[]
    number_variables = 0
    query_array_variable=[]
    
    def __init__( self , query ):

        query_simplified = self.query_to_array(query)        
        print("query_simplified:",query_simplified)
        result = self.init_parser(query_simplified)
        
        self.number_variables = result[2]
        self.query_array_variable=result[1]
        query_simplified=result[0]
        
        query_parsed     = self.expression_parser(query_simplified)
        
        if query_parsed:
            query_simplified = self.query_simplied
            
        pass
    
    def query_to_array( self , query ):
        
        import re

        # Regular expression pattern to split by spaces, "or", "and", "not"
        
        # Split the string using the pattern
        result = re.split(" ", query)
        
        # Remove empty strings from the result (if any)

        result = [word for word in result if word != " " and word != "" ]
        
        result2=[]
        keyword=["(",")","or","and","not", " ",""]
        
        if result[0] in keyword:
        
            add_and = True
        else:
            add_and = False
        
        for i , item in enumerate(result,start=0):
            
            for kw in keyword:
                
                if kw == item:
                    
                    result2.append(item)
                    add_and = False
                
            if add_and:
                
                result2.append("and")
                result2.append(item)

            else:
                add_and = True
                result2.append(item)
                
        return result2
    
    def init_parser(self , query_array ):
        
        number_variables = 0
        query_array_variable=[]
        for item in range(len(query_array)):
            
            if  query_array[item] != "not" and \
                query_array[item] != "and" and \
                query_array[item] != "or"  and \
                query_array[item] != "("   and \
                query_array[item] != ")":
            
                    query_array[item] = "E"
                    query_array_variable.append( "v" )
                    number_variables  += 1
            
            query_array_variable.append(query_array[item])
            
        return (query_array , query_array_variable , number_variables)
    
    def expression_parser( self ,query_simplied):
        
        stack=[]
        for item in query_simplied:
        
            stack.append(item)
            stack = self.production(stack)

        try:
            if len(stack) == 1 and stack[0] == "E" :
                return True
        except:
            pass
        
        return False
        
    def production(self , stack ):
        
        new_query=self.production_engine(stack=stack)
        
        while new_query[1]:
            new_query=self.production_engine(stack=new_query[0])
        
        return new_query[0]
    
    def production_engine( self , stack ):
        
        new_query=[]
        
        productions = ["EandE" , "EorE" , "notE" , "(E)" ]
        
        new_expression=False
        i=0
        while i < len(stack):
            
            q=""
            if i + 2 < len(stack):
                q  += stack[i]
                q  += stack[i+1]
                q  += stack[i+2]
            
            q1=""
            if i + 1 < len(stack):
                q1 += stack[i]
                q1  += stack[i+1]
            
            parsed = False
            for p in productions:
                
                if p == q or q1 == p :
                    new_query.append("E")
                    i+=2
                    parsed = True
                    new_expression = True
                    break
            
            if not parsed:
                new_query.append(stack[i])
                
            i+=1
        
        return (new_query,new_expression)
