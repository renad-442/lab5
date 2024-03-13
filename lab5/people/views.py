from django.shortcuts import render, redirect
from .models import Person
people = []

def add_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        person =Person(username=username,password=password)
        person.save()
        people.append(person)
        return redirect('/')
    return render(request, 'people/add_person.html')

def people_list(request):
    return render(request, 'people/people_list.html', {'people': people})
