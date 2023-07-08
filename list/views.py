from django.shortcuts import render
import os
import json

file_path = os.path.join(os.path.dirname(__file__),'places.json')

with open(file_path,"r") as file:
    data = json.load(file)

# Create your views here.

def listing(request):
    print("data",data)
    return render(request,"list.html",{"data":data})