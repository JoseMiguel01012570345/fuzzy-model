#import core
import os
#import entry
class suggestion:
    
    miu_query_per_doc=[]
    list_combination = []
    
    #    def __init__( self, query: entry.entry = None , miu_matrix: core.core = None):   
    def __init__( self):
        
        myQ = [ "not" , "v" , "and" , "(", "v" , "or" ,"(" , "v" ,"and" ,"v" ,")" , ")" ]
        
        self.combinations( 4 , [] )
        
        result = self.evaluate_expresion( myQ , self.list_combination)
        
        print( result )
        
        
        pass
    
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
        
    
os.system("cls")

suggest = suggestion()