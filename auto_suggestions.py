import re


class AutoSuggetions:

    def get_auto_suggestions(input1, input2):
        
        suggestions = []
        
        if "*" in input2:

            if input2[0] != "*":          
                input2 = "^" + input2     
                
            if input2[-1] != "*":         
                input2 = input2 + "$"     
                
            input2 = input2.replace("*", ".*")  
            
      
        regex = re.compile(input2)
        
        for word in input1:
            if regex.search(word):
                suggestions.append(word)

        return suggestions
    
if __name__ == "__main__":
   
   
    input1 = ['take', 'make', 'check', 'ackec', 'cake' ]
    input2 = "*k"

    print(AutoSuggetions.get_auto_suggestions(input1, input2))