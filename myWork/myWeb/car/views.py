from multiprocessing import context
from pyexpat import model
from django.shortcuts import render
from car.models import car,car_foto
# Create your views here.
def car_view(request):
    car_id=car.objects.all()
    if request.method=='GET':
        n=request.GET.get('n')
        car_img=car_foto.objects.filter(foto_id=n)
    
    """for i in car_img:
        foto.append(i.foto)"""
    context={
        'car':car_id,'car_img':car_img,}
    return render(request,'car/main/index.html',context=context)
