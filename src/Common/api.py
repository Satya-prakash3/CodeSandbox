from django.shortcuts import render
from Common.models import BaseModel


def index(request):
    print("Hello")
    print(BaseModel())
    return render(request=request, template_name="base.html")
