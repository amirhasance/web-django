from django.shortcuts import render

# Create your views here.
def mainpage(request ):
    return render(request,template_name= 'mainpage.html')

def login(request):

    return render (request  = request , template_name=  "login.html")


def testF(request):
    return render(request = request , template_name= "tsting.html" , context= dictt)

def signup(request):
    return render(request =request , template_name="SignUp.html")