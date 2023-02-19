from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from  . import fib
import json

def fib_handler(request: HttpRequest):
	if request.method.upper() == "POST":
		return __fib_handler_post(request)
	
	return __fib_handler_get(request)

def __fib_handler_get(request: HttpRequest):
	order = int(request.GET.get('order'))
	num = fib.get_fib_num(order)
	return HttpResponse(num)

def __fib_handler_post(request: HttpRequest):
	data = json.loads(request.body)
	# print(str(data))
	order = int(data["order"])
	num = fib.get_fib_num(order)
	data["value"] = num
	return JsonResponse(data)

# https://www.youtube.com/watch?v=fbIFdWj8PsY