from django.shortcuts import render
from django.http import  HttpResponse
from .models import services
# Create your views here.
def index(request):
    services1=services()
    services1.id=0
    services1.name='Fast'
    services1.description='Fast Services to all customers'

    services2=services()
    services2.id=1
    services2.name='Reliable'
    services2.description='Reliable Services to all customers'

    services3=services()
    services3.id=2
    services3.name='Secure'
    services3.description='Secure Services to all customers'

    services4=services()
    services4.id=3
    services4.name='Trusted'
    services4.description='Trusted Services to all customers'

    services5=services()
    services5.id=4
    services5.name='Easy to Use'
    services5.description='Easy to use to all customers'

    services6=services()
    services6.id=5
    services6.name='Affordable'
    services6.description='Affordable Services to all customers'

    services7=services()
    services7.id=5
    services7.name='Trusted'
    services7.description='Tusted Services to all customers'

   
    # context={
    #     'name':'Nihal',
    #     'age':'23',
    #     'Nationality':'indian'
        
    # }
    service=[services1,services2,services3,services4,services5,services6,services7]

    return render(request,'index.html',{"services":service})

def nextpage(request):
    # words = request.POST['Value']
    # num_of_words=len(words.split())
    return render (request,'portfolio-details.html')