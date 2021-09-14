#I have created this file - Sanukaji
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse("Home")
 
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text',"Default")
    removepunc = request.POST.get('removepunc','off')
    allcaps = request.POST.get('allcaps','off')
    removenewlines = request.POST.get('removenewlines','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')

    #Analyze the text
    if removepunc == 'on':
        punctuations ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        
    elif allcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose':'UPPERCASE','analyzed_text':analyzed}
        djtext = analyzed

    elif extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " "  and  djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Remover','analyzed_text':analyzed}
        djtext = analyzed

        
    elif removenewlines =='on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != "\r":
                analyzed = analyzed+char
        params = {'purpose':'Remove NewLines','analyzed_text':analyzed}
        djtext = analyzed
    elif charcount == 'on':
        count=0
        for char in djtext:
            count = count +1
        analyzed = 'The number of character is '+str(count)
        params = {'purpose':'Characters Counts','analyzed_text':analyzed}
        djtext=analyzed
        
    
    if (charcount != 'on' and removenewlines !="on" and extraspaceremover !="on" and allcaps !="on" and removepunc != "on"):
        return HttpResponse("Please select any operation")
    
    return render(request,'analyze.html',params)
