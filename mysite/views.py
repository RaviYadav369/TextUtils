#user creat file
from django.http import HttpResponse
from django.shortcuts import render
#
# def index(request):
#     return HttpResponse("hello")

def index(request):
    return render(request,'index2.html')

def analyse(request):
     # print(request.GET.get('text','default'))

     djtext = request.POST.get('text', 'default')
     removepunc=request.POST.get('punc','off')
     captial_char=request.POST.get('capatial','off')
     newline_char=request.POST.get('newline','off')
     extra_char=request.POST.get('extra','off')
     count_char=request.POST.get('count','off')

     if removepunc == "on":
        punctuation= '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analysed = ""
        for char in djtext:
            if char not in punctuation:
                 analysed = analysed + char
        params = {'purpose': 'Removed Punctuation', 'analysed_text': analysed}
        djtext=analysed
     if captial_char == 'on':
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        params = {'purpose': 'Removed Punctuation', 'analysed_text': analysed}
        djtext = analysed
     if newline_char=='on':
        analysed=""
        for char in djtext:
            if char !='\n' and char!="\r":
                analysed=analysed+char
        params = {'purpose': 'Removed Punctuation', 'analysed_text': analysed}
        djtext = analysed

     if extra_char == 'on':
        analysed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index - 1] == " "):
                analysed = analysed + char
        params = {'purpose': 'Removed Punctuation', 'analysed_text': analysed}
        djtext = analysed
     if removepunc!='on' and extra_char!='on' and newline_char!='on' and captial_char!='on':
         return HttpResponse("Please Select any option")
     return render(request,'analyse.html',params)

