# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import smtplib
import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.mail import send_mail
from .forms import ContactUsForm

from fulfillscouts import settings

def home(request):
	if request.method != 'POST':
		form = ContactUsForm()
		return render (request, 'index.html', {'form':form})
		
	form = ContactUsForm(request.POST)

	if form.is_valid():
		data = form.cleaned_data

		f_name = data['f_name']
		email = data['email']
		skype_id = data['skype_id']
		orders = data['orders']
		countries = data['countries']
		product = data['product']
		message = data['message']

		new_message = str('f_name: ' + f_name + '\nemail: ' + email + '\nskype_id: ' + skype_id + '\nnumber of orders: ' + orders + '\nlist of countries: ' + countries + '\nalibaba link: ' + product + '\nmessage: ' + message)

		print(new_message)

		send_mail("NEW QUERY", new_message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], fail_silently=False)
		
		message = "Query Sent Succesfully"

		return HttpResponseRedirect('/', {'message': message})



# def get_order(request):
# 	data = json.load(request)
# 	print("new data arraived:  ", data)
# 	return JsonResponse({'message':'Email sent'})