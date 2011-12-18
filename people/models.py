from django.db import models

class Detail(models.Model):
   email = models.EmailField()
   nickname = models.CharField(max_length=30)
   ip = models.CharField(max_length=20)
   status = models.CharField(max_length=10)

   def __unicode__(self):
      return '%s : %s : %s' % (self.email, self.ip, self.status)




