from django.db import models
from accounts.models import User,UserProfile
from accounts.utils import *

# Create your models here.
class Vendor(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, related_name='userprofile', on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=50)
    vendor_license = models.ImageField( upload_to='vendor/license')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name

    def save(self,*args,**kwargs):
        if self.pk is not None:
            #update
            orig = Vendor.objects.get(pk=self.pk)
            if orig.is_approved != self.is_approved:
                context = {
                        'user':self.user,
                        'is_approved':self.is_approved
                        }
                email_template = "accounts/emails/admin_approval_email.html"
                if self.is_approved == True:
                    #send notification mail
                    email_subject = "Congratulations! Your restaurant has been approved."
                    
                    send_notification(email_subject,email_template,context)
                else:
                    email_subject = "We are sorry! you are not eligible for publishing your food menu on our marketplace."
                    send_notification(email_subject,email_template,context)
        return super(Vendor,self).save(*args,**kwargs)
