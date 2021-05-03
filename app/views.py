from django.shortcuts import render

def home(request):
 return render(request,'app/index.html')

def contact(request):
 return render(request,'app/contact.html')

def service(request):
 return render(request,'app/service.html')


def about(request):
 return render(request,'app/about.html')
 
def blog(request):
 return render(request,'app/blog.html')
