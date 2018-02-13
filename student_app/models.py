from django.db import models

# Create your models here.
class School(models.Model):
    RATING = (
        (1,  '1'),
        (2,  '2'),
        (3,  '3'),
        (4,  '4'),
        (5,  '5'),
    )
    name = models.CharField(verbose_name="School Name",max_length = 50,null=False,blank=False)
    address = models.TextField("Address",null=True,blank=True)
    rating = models.IntegerField("Rating",max_length=1,null=False,choices=RATING,blank=False)
    email = models.EmailField("EmailID",null=False,unique=True)
    contact_no = models.BigIntegerField("Contact No.",max_length=10,null=True,blank=True)
    website = models.CharField("Website",max_length=50,null=True,blank=True)
    enabled = models.BooleanField("Is active",default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
		return self.name

class Student(models.Model):
    STANDARD = (
       
        (5,  '5'),
        (6,  '6'),
        (7,  '7'),
        (8,  '8'),
        (9,  '9'),
        (10, '10'),
    )
    school = models.ForeignKey(School)
    first_name = models.CharField("First Name",max_length=50,null=False,blank=False)
    last_name = models.CharField("Last Name",max_length=50,null=False,blank=False)
    #profile_image = models.ImageField(max_length=255,upload_to="")
    email = models.EmailField("EmailID",null=False,unique=True,blank=False)
    residence_address =  models.TextField("Residence Add.",null=True,blank=True)
    standard = models.IntegerField("Standard",max_length=1,null=False,blank=False,choices=STANDARD)
    roll_no = models.PositiveIntegerField("Roll No.",null=False,blank=False)
    fees = models.PositiveIntegerField("Fees",null=False,blank=False)
    enabled = models.BooleanField("Is active",default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
		return self.first_name


