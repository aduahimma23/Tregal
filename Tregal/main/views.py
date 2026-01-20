from django.shortcuts import render
from .models import *

def home(request):
    carousel_images = CarouselImage.objects.all()
    header_info = HeaderInfo.objects.first()
    tour_packages = TourPackage.objects.all()
    trending_destinations = TrendingDestination.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all()
    blog_posts = BlogPost.objects.all()
    gallery_images = GalleryImage.objects.all()

    context = {
        'carousel_images': carousel_images,
        'header_info': header_info,
        'tour_packages': tour_packages,
        'trending_destinations': trending_destinations,
        'testimonials': testimonials,
        'faqs': faqs,
        'blog_posts': blog_posts,
        'gallery_images': gallery_images,
    }
    
    return render(request, 'main/index.html', context)

def about(request):
    about_us = AboutUs.objects.first()
    vision_statement = VisionStatement.objects.first()
    mission_statement = MissionStatement.objects.first()
    our_services = OurService.objects.all()
    partners = PartnerInstitution.objects.all()

    context = {
        "about_us": about_us,
        "vision_statement": vision_statement,
        "mission_statement": mission_statement,
        "our_services": our_services,
        "partners": partners,
    }

    return render(request, 'main/about_us.html', context)

def contact(request):
    contact_info = ContactInfo.objects.first()

    context = {
        "contact_info": contact_info,
    }

    return render(request, 'main/contact_us.html', context)

def services(request):
    our_services = OurService.objects.all()

    context = {
        "our_services": our_services,
    }

    return render(request, 'main/services.html', context)