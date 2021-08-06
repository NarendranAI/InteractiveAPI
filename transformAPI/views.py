from django.shortcuts import render
from .processes import tagnumber  

# Create your views here.
def home(request):
    return render(request,'base.html')

def tagNumber(request):
    x=request.POST
    if request.POST.get('InputAPI'):
        IP=request.POST.get('InputAPI') 
        OP,TN=tagnumber.processTagNumber(IP) 
          
    else:
        IP="" 
        OP=""
        TN=""
        
    return render(request,'tagNumber.html',{'I':IP,'O':OP,'T':TN,'x':x})
 
def receivedDate(request):
    return render(request,'receivedDate.html')
        
def parentCompany(request):
    return render(request,'parentCompany.html')