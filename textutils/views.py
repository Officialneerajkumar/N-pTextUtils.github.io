# i have created this file.
from django.http import HttpResponse
from django.shortcuts import render
# personal navigator
#def index(request):
#        return HttpResponse('''<h1>Hello Neeraj bhai</h1>
#                      <a href="https://www.youtube.com"> Welcome in youtube gyani baba </a> <br>
#                        <a href="https://www.facebook.com"> Welcome in facebook baba </a> <br>
#                        <a href="https://www.instagram.com"> Welcome in instagram baba </a> <br>
#                        <a href="https://www.hackerrank.com"> Welcome in hackerrank coding baba </a> <br>
#                        ''')



def index(request):
    return render (request,'index.html')
#PROJECT WORK start
def aboutUs(request):
    return render(request,'aboutUs.html')
def help(request):
    return render(request,'help.html')


#project work End
def analyze(request):
    # get the Text
    djtext = request.GET.get('text','default')
    # check checkbox value
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraSpaceRemover = request.GET.get('extraSpaceRemover', 'off')
    CharacterCounter = request.GET.get('CharacterCounter', 'off')
    print(removepunc)
    print(djtext)
    # analyze the text
    if removepunc == "on":
        punctuations = '''~`!@#$%^&*()_-=+;:'",.<>/?{}[]\|'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove punctuations', 'analyze_text' : analyzed}
        djtext=analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change into upper Case', 'analyze_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Line', 'analyze_text': analyzed}
        djtext = analyzed
    if extraSpaceRemover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Remove the Extra Space', 'analyze_text': analyzed}

    #elif CharacterCounter == "on":
    #    valueTocount = input("enter your value to find out")
    #    analyzed = djtext.count(valueTocount)
    #    params = {'purpose': 'Remove the Extra Space', 'analyze_text': analyzed}
    #    return render(request, 'analyze.html', params)
    if (removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraSpaceRemover!='on'):
        return HttpResponse("please select atleast one operation !")

    return render(request,'analyze.html' , params)

# project work



#def removepunc(request):
    # get the Text
#    djtext = request.GET.get('text','default')
#    print(djtext)
    # analyze the text
#    return HttpResponse('''removepunc <br> <a href="/"> Back Button</a>''')
#def capitalizefirst(request):
#    return HttpResponse('''capitalize first <br> <a href="/"> Back Button</a> ''')
#def newlineremover(request):
#    return HttpResponse('''new  line remover <br> <a href="/"> Back Button</a>''')
#def spaceremover(request):
#    return HttpResponse('''space remover <br> <a href="/"> Back Button</a>''')
#def charcount(request):
#    return HttpResponse('''char count <br><a href="/"> Back Button</a>''')
