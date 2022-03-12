import itertools
import schedule
import time
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from celery.schedules import crontab
from celery.task import periodic_task
from django.template.defaultfilters import slugify
# Create your models here.
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

class CustomAccountManager(BaseUserManager):
    def create_superuser(self,email,user_name,first_name,password,**other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'superuser must be assigned to is_staff=True'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'superuser must be assigned to is_superuser=True'
            )
        return self.create_user(email,user_name,first_name,password, **other_fields)
    def create_user(self,email,user_name,first_name,password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        email=self.normalize_email(email)
        user=self.model(email=email,user_name=user_name,
            first_name=first_name,**other_fields
        )
        user.set_password(password)
        user.save()
        return user

class NewUsermodel(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(_('email address'),unique=True)
    user_name=models.CharField(max_length=150,unique=True)
    first_name=models.CharField(max_length=150,blank=True)
    start_date=models.DateTimeField(default=timezone.now)
    about=models.TextField(_(
        'about'),max_length=500,blank=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    objects=CustomAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['user_name','first_name']

    def __str__(self):
        return self.user_name

class Krarecords(models.Model):
    names = models.CharField(max_length=120,null=True)
    profession = models.CharField(max_length=120)
    idno = models.IntegerField(max_length=20,null=True)
    dob= models.DateField(null=True)
    box = models.CharField(max_length=120, null=True)
    county = models.CharField(max_length=120, null=True)
    town = models.CharField(max_length=20, null=True)
    mobile = models.IntegerField(null=True)
    email=models.EmailField( null=True,blank=True)
    datesend = models.DateField(null=True)
    datecompleted = models.DateField(null=True)


    def _str_(self):
        return self.names

    @property
    def kratotal(self):
        allrecords = Krarecords.objects.all().count
        return allrecords

    @property
    def jobtotal(self):
        allrecords = Jobrequest.objects.all().count
        return allrecords

    @property
    def atotal(self):
        allrecords = Article.objects.all().count
        return allrecords




class Jobrequest(models.Model):
    names = models.CharField(max_length=120,null=True)
    idno = models.IntegerField(max_length=20,null=True,blank=True)
    message = models.TextField( null=True,blank=True)
    mobile = models.IntegerField(null=True)
    jobtype = models.CharField(max_length=120, null=True)
    datecompleted = models.DateField(null=True)
    datesend = models.DateField(null=True)


    def _str_(self):
        return self.names


class Returns(models.Model):
    names = models.CharField(max_length=120,null=True)
    yourpin = models.CharField(max_length=120, null=True)
    employerpin = models.CharField(max_length=120, null=True)
    email = models.CharField(max_length=120, null=True)
    mobile = models.IntegerField(null=True)
    p9form = models.ImageField(null=True, blank=True, upload_to="images")
    datesend = models.DateField(null=True)
    datecompleted = models.DateField(null=True)



    def _str_(self):
        return self.names


class Article(models.Model):
    title = models.CharField(max_length=120,null=True)
    slug = models.SlugField(default='')
    body = models.TextField( null=True,blank=True)
    photo = models.ImageField(null=True, blank= True, upload_to="images")
    author = models.CharField(max_length=120, null=True)
    dateposted=models.DateField( blank=True)

    def _str_(self):
        return self.title



    # method for sending email
@receiver(post_save, sender=Jobrequest)
def send_email(sender, instance, **kwargs):
    subject = 'NEW JOB REQUEST'
    message = f'customer details {instance.names,instance.idno,instance.message,instance.mobile,instance.jobtype}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['muthokajoseph10@gmail.com',]
    send_mail(subject, message, email_from, recipient_list)
    print('this is succesful')


@receiver(post_save, sender=Returns)
def send_email(sender, instance, **kwargs):
    subject = 'NEW RETURNS JOB REQUEST'
    message = f'customer details {instance.names,instance.yourpin,instance.employerpin,instance.email,instance.p9form,instance.mobile}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['muthokajoseph10@gmail.com',]
    send_mail(subject, message, email_from, recipient_list)
    print('this is succesful')


@receiver(post_save, sender=Krarecords)
def send_email(sender, instance, **kwargs):
    subject = 'NEW KRA JOB REQUEST'
    message = f'customer details {instance.names,instance.idno,instance.dob,instance.mobile,instance.county,instance.town}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['muthokajoseph10@gmail.com',]
    send_mail(subject, message, email_from, recipient_list)

# method for sending kra file return email
def every_friday():
    print("This is run every Friday  at 23:20")
    allrecords = Krarecords.objects.filter(datecompleted__isnull=False).count()
    d1 = timezone.now().date()
    i = 0
    while (i < allrecords):
        d2 = Krarecords.objects.filter(datecompleted__isnull=False).only('datecompleted')[i]
        diff =d1-d2.datecompleted
        datenumber=diff.days
        if(datenumber>365):
            # send email
            subject = 'FILE RETURN REMINDER'
            message = f'Hello customer,Its now a year since you filled KRA Returns. Avoid being penalted by sending a Kra returns request to us'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [d2.email, ]
            send_mail(subject, message, email_from, recipient_list)
        i += 1

schedule.every().saturday.at("00:30").do(every_friday)
