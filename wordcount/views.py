from django.http import HttpResponse
from django.shortcuts import render

import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    count = len(wordlist)

    words = {}
    for word in wordlist:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
        
    sortedwords = sorted(words.items(),key = operator.itemgetter(1),reverse=True)

    

    return render(request,'count.html',{'fulltext':fulltext,'count':count,'sortedwords':sortedwords})


def about(request):
    return render(request,'about.html')