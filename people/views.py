# Create your views here.
from django.shortcuts import redirect, render_to_response
from models import *

def redir(request, **kwargs):
   #get the user from the DB
   nick = kwargs.get('nick', '')
   try:
      detail = Detail.objects.get(nickname=nick)
   except Detail.DoesNotExist:
      return render_to_response('404.html',{})

   #if user exists, then
   #if user wishes to be online, redirect
   if detail.status == 'online':
      path = kwargs.get('path_hence', '') 
      return redirect('http://%s/%s' % (detail.ip, path))
   #else 404
   return render_to_response('404.html',{})
      
