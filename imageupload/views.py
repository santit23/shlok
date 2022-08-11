from tkinter import Image
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import *
from .models import Images

# Create your views here.
def Images_image_view(request):

	if request.method == 'POST':
		form = HotelForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = HotelForm()
	return render(request, 'image_upload.html', {'form' : form})


def success(request):
	return HttpResponse('successfully uploaded')


def display_uploaded_images(request):
    if request.method == 'GET':
        Image_list = Images.objects.all()
		
        return render(request, 'display_uploaded_images.html',{'uploaded_images':Image_list})


# class ImageDisplay(DetailView):
#     model = Images
#     template_name = 'display_uploaded_images.html'
#     context_object_name = 'emp'