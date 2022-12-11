from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from .models import user_register, admin_register
from .views import userRegistration, user_signin, adminRegistration, admin_signin, user_register
from .views import logging 
logger = logging.getLogger('idento')
from django.contrib.auth.signals import user_logged_in, user_login_failed, user_logged_out


# @receiver(pre_save, sender= user_register)
# def pre_login(sender, instance, created, **kwargs):
#     if created:
#         user_register.objects.get()
#         logger.info(f'######################################User: {instance.username}  logged in about to start')
#         logger.info(instance.username)
#         print(f'######################################User: {instance.username}  logged in about to start')
  

@receiver(post_save, sender= user_register)
def post_login(sender, created, instance, **kwargs):
    if instance.verify == False:
        
        logger.info(f'######################################## New request has been raised for username: {instance.username} So, sending otp to provided email: {instance.email} for further verification')
        print(f'######################################## New request has been raised for username: {instance.username} So, sending otp to provided email: {instance.email} for further verification')

    else:
        logger.info(f'new user with username: {instance.username} is created successfully')  
        print(f'new user with username: {instance.username} is created successfully')    



