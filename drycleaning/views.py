from django.shortcuts import render
from .models import Order,Contact

# Create your views here.

def index(request):
	return render(request,'index.html')

def orders(request):
	firstname=request.POST["firstname"]
	lastname=request.POST["lastname"]
	email=request.POST["email"]
	phone=request.POST["phone"]
	order_placed=request.POST["order_placed"]
	time=request.POST["time"]
	clothtype=request.POST["clothtype"]
	choose_service=request.POST["choose_service"]
	address=request.POST["address"]

	order_info=Order(firstname=firstname,lastname=lastname,email=email,phone=phone,order_placed=order_placed,
				time=time,clothtype=clothtype,choose_service=choose_service,address=address)
	order_info.save()
	return render(request,'index.html')

def contact(request):
	name=request.POST["name"]
	email=request.POST["email"]
	subject=request.POST["subject"]
	message=request.POST["message"]

	contact_info=Contact(name=name,email=email,subject=subject,message=message)
	contact_info.save()
	return render(request,'index.html')

