from django.db import models

STATUS_CHOICES = [
    ('pick_up','Picked Up'),
    ('delivered', 'Delivered'),
    ('processing', 'Processing'),
    ('verified', 'Verified'),
    ('cancelled','Cancelled'),
    ('ready_to_deliver','Ready to be deliverd'),
    ('transaction_completed','Transaction Completed'),
]

# Create your models here.
class Order(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    phone=models.BigIntegerField()
    order_placed=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    clothtype=models.CharField(max_length=50)
    choose_service=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,default='DEFAULT VALUE')
    order_created=models.DateTimeField(auto_now_add=True)
    price=models.IntegerField(null="True")
  
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField()



#what you want to show in admin panel name or address or anything
#tab should be given after defining function
#alignment should right i.e as below otherwise this won't work
    feedback="Feedback From"
    def __str__(self):
        return self.feedback+" "+self.name