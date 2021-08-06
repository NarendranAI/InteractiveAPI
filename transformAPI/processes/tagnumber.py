import re


def processTagNumber(txt):
    API = txt
    try:
        a, b = re.findall('bpart_id.*and ', API)
    except:
        return "ERROR: Please check the input API for indentation (or) value", "Not_Found"
    newAPI = API.replace(a, '')
    newAPI = newAPI.replace(b, '')
 
    match = re.search('tagno = \'(.*)\'', txt)

    
    return newAPI, match.group(1)
