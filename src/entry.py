import os
    
class entry:
    
    query_simplied=[]
    number_variables = 0
    query_v=[]
    
    def __init__( self , query ):

        query_simplified = self.query_to_array(query)        
        result = self.init_parser(query_simplified)
        
        query_E=result[0]
        self.query_v=result[1]
        self.number_variables = result[2]
        
        query_parsed     = self.expression_parser(query_E)
        
        if query_parsed:
            self.query_simplied = query_simplified
        else:
            print("please check your query")
            
        pass
    
    def query_to_array( self , query ):
        
        import re
        
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
        
        for item in result:
            
            is_kw=False
            for kw in keyword:
                
                if kw == item:
                    
                    result2.append(item.lower())
                    add_and = False
                    is_kw =True
                
            if add_and:
                
                result2.append("and")
                result2.append(item.lower())

            elif not is_kw :
                add_and = True
                result2.append(item.lower())
                
        return result2
    
    def init_parser(self , query_array ):
        
        number_variables = 0
        query_v = []
        query_E = []
        for item in range(len(query_array)):
            
            if  query_array[item] != "not" and \
                query_array[item] != "and" and \
                query_array[item] != "or"  and \
                query_array[item] != "("   and \
                query_array[item] != ")":
            
                    query_E.append( "E" )
                    query_v.append( "v" )
                    number_variables  += 1
                    continue
            
            query_v.append(query_array[item])
            query_E.append(query_array[item])
            
        return (query_E , query_v , number_variables)
    
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