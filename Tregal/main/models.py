from django.db import models

class CarouselImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='carousel/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about_us/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class MissionStatement(models.Model):
    statement = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.statement[:50]
    
class VisionStatement(models.Model):
    statement = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.statement[:50]

class OurService(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='our_services/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TrendingDestination(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    deadline = models.DateField()
    destination = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='trending_destinations/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class TourPackage(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='tour_packages/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    customer_name = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
    
class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_posts/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class HeaderInfo(models.Model):
    logo = models.ImageField(upload_to='header/')
    navigation_links = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Header Information"

class FooterInfo(models.Model):
    contact_details = models.TextField()
    social_media_links = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Footer Information"
    
class SocialMediaLink(models.Model):
    platform_name = models.CharField(max_length=100)
    url = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.platform_name
    
class ScholarshipInfo(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    origin = models.CharField(max_length=200, blank=True, null=True)
    school_name = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    eligibility_criteria = models.TextField()
    application_process = models.TextField()
    deadline = models.DateField(blank=False, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PartnerInstitution(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()
    logo = models.ImageField(upload_to='partners/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class SpecialOffer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    valid_until = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title