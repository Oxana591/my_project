from django.shortcuts import render
from django.http import HttpResponseRedirect
from school.models import Student

# Create your views here.

def uch_find(request):
    pupil=Student.objects.all()
    msg='Усі учні класу!'
    if request.method=='POST':
        post_lastname=request.POST.get('find')
        pupil=Student.objects.filter(lastname=post_lastname)
        msg='Знайдено!'
    if len(pupil)==0:
        msg='не знайдено'
    return render(request,'school/uch_find/index.html',{'pupil':pupil,'msg':msg})
    
    

def uch_add(request):
    pupil=Student.objects.all()
    msg=''
    if request.method=='POST':
        person=Student()
        person.lastname=request.POST.get('lastname')
        person.name=request.POST.get('name')
        person.post=request.POST.get('post')
        person.save()
        msg=f'{person.lastname} {person.name} {person.post} - додано!'
        #mag=str(person['lastname'])+' '+str(person['name'])+' '+str(person['post'])+' - додано!'
    return render(request,'school/uch_add/index.html',{'pupil':pupil,'msg':msg})