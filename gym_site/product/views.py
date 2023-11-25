from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from product.models import CommentForm, Comment


# Create your views here.
def index(request):
    return HttpResponse("Hello")

def addcomment(request,id):
   url = request.META.get('HTTP_REFERER')  # get last url
   #return HttpResponse(url)
   if request.method == 'POST':  # check post
      form = CommentForm(request.POST)
      if form.is_valid():
         data = Comment()  # create relation with model
         data.user = form.cleaned_data['user']
         data.email = form.cleaned_data['email']
         data.comment = form.cleaned_data['comment']
         # data.ip = request.META.get('REMOTE_ADDR')
         # data.product_id=id
         current_user= request.user
         data.user_id=current_user.id

         data.save() 
         messages.success(request, "Your review has been sent. Thank you for your interest.")
         
         return HttpResponseRedirect(url)

   return HttpResponseRedirect(url)