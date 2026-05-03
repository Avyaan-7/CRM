from django.shortcuts import render

# Create your views here.
'''
🧠 What actually happens
User visits a URL (like /home)
Django routes it to home(request)
That function:
loads home.html
(optionally injects data)
returns it as a web page
User sees the page in their browser  '''

def home(request):
    return render(request,'home.html',{})
