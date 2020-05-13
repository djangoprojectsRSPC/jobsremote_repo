import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','JobPortalProject.settings')
django.setup()

from testapp.models import *
from faker import Faker
from random import *
fake=Faker()

def phnogen():
    d1=randint(7,9)
    num=str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team Lead','Software Engineer'))
        feligibility = fake.random_element(elements=('MCA','BE','PHD','MTech'))
        faddress = fake.address()
        femail = fake.email()
        fphno = phnogen()
        hydjobs_record=HydJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phno=fphno)


        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team Lead','Software Engineer'))
        feligibility = fake.random_element(elements=('MCA','BE','PHD','MTech'))
        faddress = fake.address()
        femail = fake.email()
        fphno = phnogen()
        blorejobs_record=BloreJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phno=fphno)


        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team Lead','Software Engineer'))
        feligibility = fake.random_element(elements=('MCA','BE','PHD','MTech'))
        faddress = fake.address()
        femail = fake.email()
        fphno = phnogen()
        punejobs_record=PuneJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phno=fphno)


        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team Lead','Software Engineer'))
        feligibility = fake.random_element(elements=('MCA','BE','PHD','MTech'))
        faddress = fake.address()
        femail = fake.email()
        fphno = phnogen()
        chennaijobs_record=ChennaiJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phno=fphno)

populate(10)
