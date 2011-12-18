from django.http import HttpResponse, HttpResponseRedirect
from google.appengine.api import users
from people.models import *
from django.shortcuts import render_to_response, redirect
from settings import MY_NAME, MY_EMAIL
import logging
def home(request):
   user = users.get_current_user()
   if user:
      try:
         detail = Detail.objects.get(email=user.email())
     
      except Detail.DoesNotExist:
      
         try:
            caddr = request.META['HTTP_X_FORWARDED_FOR']
         except KeyError:
            caddr = request.META['REMOTE_ADDR']
            
         detail = Detail( email = user.email(),
                          nickname = user.nickname(),
                          ip = caddr,
                          status = 'offline'
                        )
         detail.save()
         logging.info('Account for %s created.' % detail.email)

      logging.info('%s accessing home' % detail.email)
      return render_to_response('home.html',{'details':detail})    
   
   login_url = users.create_login_url(request.build_absolute_uri())

   return render_to_response('index.html', {'login_url':login_url, 'zieben_url': request.build_absolute_uri('/')})
   

def toggle_status(request):
   user = users.get_current_user()
   if user:
      try:
         detail = Detail.objects.get(email=user.email())
      except Detail.DoesNotExist:
         return redirect('/')

      detail.status = 'offline' if detail.status == 'online' else 'online'
      detail.save()
      logging.info('%s is now %s.' % (detail.email, detail.status))
      #return render_to_response('home.html', {'details':detail})
      return redirect('/')
   
   return HttpResponseRedirect(users.create_login_url(request.build_absolute_uri('/')))

def update_ip(request):
   user = users.get_current_user()
   if user:
      try:
         detail = Detail.objects.get(email=user.email())
      except Detail.DoesNotExist:
         return redirect('/')
      
      try:
         ip = request.META['HTTP_X_FORWARDED_FOR']
      except KeyError:
         ip = request.META['REMOTE_ADDR']

      detail.ip = ip
      detail.save()
      #return render_to_response('home.html', {'details':detail, 'messages':['IP successfully updated.']})
      return redirect('/', {'messages':['IP Updated']})
   
   return HttpResponseRedirect(users.create_login_url(request.build_absolute_uri('/')))

def logout(request):
   return HttpResponseRedirect(users.create_logout_url(request.build_absolute_uri('/')))

def about(request):
   zieben_url = request.build_absolute_uri('/')
   email = MY_EMAIL.replace('@', ' [at] ').replace('.', ' [dot] ')
   user = users.get_current_user()
   user_nick = user.nickname() if user else 'your.google.nick'
   return render_to_response('about.html', {'name':MY_NAME, 
                                            'email':email, 
                                            'zieben_url': zieben_url,
                                            'about_page': True,
                                            'user_nick': user_nick
                                            })

    


