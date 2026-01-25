from django.shortcuts import render, get_object_or_404
from .models import *

def home(request):
    carousel_images = CarouselImage.objects.order_by('-date_added')[:3]  
    header_info = HeaderInfo.objects.first()
    tour_packages = TourPackage.objects.order_by('-date_added')[:3]
    trending_destinations = TrendingDestination.objects.order_by('-date_added')[:3]
    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all()
    blog_posts = BlogPost.objects.all()
    gallery_images = GalleryImage.objects.all()
    partners = PartnerInstitution.objects.all()

    context = {
        'carousel_images': carousel_images,
        'header_info': header_info,
        'tour_packages': tour_packages,
        'trending_destinations': trending_destinations,
        'testimonials': testimonials,
        'faqs': faqs,
        'blog_posts': blog_posts,
        'gallery_images': gallery_images,
        'partners': partners,
    }
    
    return render(request, 'main/index.html', context)

def about(request):
    about_us = AboutUs.objects.all()
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

def contact_info_view(request):
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

def tour_packages(request): 
    tour_packages = TourPackage.objects.all().order_by('-date_added')
    trending = TrendingDestination.objects.all().order_by('-date_added')[:3]

    context = { 
        "tour_packages": tour_packages,
        "trending": trending 
    }

    return render(request, 'main/tour.html', context)


def scholarships(request):
    scholarships = ScholarshipInfo.objects.all().order_by('-date_added')

    context = { 
        "scholarships": scholarships
        }

    return render(request, 'main/scholarship.html', context)

def mission(request):
    mission_statement = MissionStatement.objects.first()
    vision_statement = VisionStatement.objects.first()

    context = { 
        "mission_statement": mission_statement,
        "vision_statement": vision_statement
        }

    return render(request, 'main/mission.html', context)

def special_offers(request):
    offers = SpecialOffer.objects.all().order_by('-valid_until')

    context = { 
        "offers": offers
        }

    return render(request, 'main/special_offer.html', context)