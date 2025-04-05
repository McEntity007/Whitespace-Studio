from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name 



# State Model
class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# City Model
class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# User Model
class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='upic', blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    address = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Product Category Model
class ProductCategory(models.Model):
    name = models.CharField(max_length=70)
    image = models.ImageField(upload_to='catimg')

    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    material_type = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products')
    STATUS_LIST = [('Available', 'Available'), ('Out of Stock', 'Out of Stock')]
    status = models.CharField(choices=STATUS_LIST, max_length=20)

    def __str__(self):
        return self.name


# Product Images Model
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return f"Image of {self.product.name}"


# Product Inquiry Model
class ProductInquiry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qty = models.IntegerField()
    budget = models.FloatField()
    message = models.TextField()
    STATUS_LIST = [('Pending', 'Pending'), ('Resolved', 'Resolved')]
    status = models.CharField(choices=STATUS_LIST, max_length=20, default='Pending')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inquiry by {self.user.name} for {self.product.name}"


# Design Category Model
class DesignCategory(models.Model):
    name = models.CharField(max_length=70)
    image = models.ImageField(upload_to='designscat')

    def __str__(self):
        return self.name


# Design Model
class Design(models.Model):
    category = models.ForeignKey(DesignCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='designimg')
    designer_name = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100)
    material = models.CharField(max_length=200)
    estimated_cost = models.FloatField()
    STATUS_LIST = [('Available', 'Available'), ('Unavailable', 'Unavailable')]
    status = models.CharField(choices=STATUS_LIST, max_length=20)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Design Images Model
class DesignImage(models.Model):
    design = models.ForeignKey(Design, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='designs')

    def __str__(self):
        return f"Image of {self.design.title}"


# Design Inquiry Model
class DesignInquiry(models.Model):
    design = models.ForeignKey(Design, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.FloatField()
    timeline = models.CharField(max_length=100)
    preferred_materials = models.CharField(max_length=200)
    special_request = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inquiry by {self.user.name} for {self.design.title}"


# Contact Model 
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name 



# Feedback Model
class Feedback(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.BigIntegerField()
    feedback_message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name








