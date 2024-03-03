import core
import os
import entry
class suggestion:
    
    miu_query_per_doc=[]
    
    def __init__( self, query: entry.entry = None , miu_matrix: core.core = None):
        pass
    
    def combinations( self , num: int , combination: list , list_combination: list ):
            
        if num == 0:
            
            list_combination.append(combination)
            print(combination)    
            return
        
        combination.append(1)
        
        self.combinations( num-1 , combination ,list_combination )
        
        combination.pop()
        
        combination.append(0)

        self.combinations( num - 1 , combination ,list_combination)
    
        combination.pop()
        
        return list_combination

    
    
    
os.system("cls")

suggest = suggestion()