from django.shortcuts import render
from django.http import HttpResponse
from .forms import contactform

def contact(request):

    if request.method =='POST':
        form = contactform(request.POST)
        if form.is_valid():
            rollno=form.cleaned_data['rollno']
            name= form.cleaned_data['name']

            print(name,rollno)
            fo = open("user_datails.csv", "w")
            fo.write(rollno)
            fo.write(",")
            fo.write(name)
            fo.write("\n")
            fo.close()


    form = contactform()
    return render(request,'form.html',{'form':form})



