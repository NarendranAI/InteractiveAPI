
import re

def processTagNumber(x):
    try:
        
        res=re.search("search.*?tagno = \'[0-9]*?\'\"",x)
        tagno=re.search("tagno = \'(.*)\'",res[0])
        # print(res[0])
        # print(tagno.group(1))
        newtxt=x.replace(res[0],"search_criteria=\"tagno = \'{}\'\"".format(tagno.group(1)))
        return newtxt, tagno.group(1)
    
    except:
        # print("ERROR")
        return "Please check the Input API","NA"
