#I have created this file - Sanukaji
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse("Home")
 
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext = request.GET.get('text',"Default")
    removepunc = request.GET.get('removepunc','off')
    allcaps = request.GET.get('allcaps','off')
    removenewlines = request.GET.get('removenewlines','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    charcount = request.GET.get('charcount','off')


   
    #Analyze the text
    if removepunc == 'on':
        punctuations ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif allcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose':'UPPERCASE','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " "  and  djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Remover','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

        
    elif removenewlines =='on':
        analyzed = ""
        for char in djtext:
            if char != '\n':
                analyzed = analyzed+char
        params = {'purpose':'Remove NewLines','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif charcount == 'on':
        count=0
        for char in djtext:
            count = count +1
        analyzed = 'The number of character is '+str(count)
        params = {'purpose':'Characters Counts','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
        
    
    else:
        return HttpResponse("Error")
