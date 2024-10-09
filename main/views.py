from rest_framework import viewsets
from .models import (
    About, FAQ, Our_Clients, Comments, Contacts, Footer,
    Posts, ServiceCategories, Services, OurService, Contact,
    Pricing, PriceList, Teachers, Coworkers
)
from .serializers import (
    AboutSerializer, FAQSerializer, OurClientsSerializer, CommentsSerializer, ContactsSerializer,
    FooterSerializer, PostsSerializer, ServiceCategoriesSerializer, ServicesSerializer,
    OurServiceSerializer, ContactSerializer, PricingSerializer, PriceListSerializer,
    TeachersSerializer, CoworkersSerializer
)


# About ViewSet
class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


# FAQ ViewSet
class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


# Our Clients ViewSet
class OurClientsViewSet(viewsets.ModelViewSet):
    queryset = Our_Clients.objects.all()
    serializer_class = OurClientsSerializer


# Comments ViewSet
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


# Contacts ViewSet
class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


# Footer ViewSet
class FooterViewSet(viewsets.ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer


# Posts ViewSet
class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


# Service Categories ViewSet
class ServiceCategoriesViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategories.objects.all()
    serializer_class = ServiceCategoriesSerializer


# Services ViewSet
class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


# Our Service ViewSet
class OurServiceViewSet(viewsets.ModelViewSet):
    queryset = OurService.objects.all()
    serializer_class = OurServiceSerializer


# Contact ViewSet
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# Pricing ViewSet
class PricingViewSet(viewsets.ModelViewSet):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer


# PriceList ViewSet
class PriceListViewSet(viewsets.ModelViewSet):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer


# Teachers ViewSet
class TeachersViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer


# Coworkers ViewSet
class CoworkersViewSet(viewsets.ModelViewSet):
    queryset = Coworkers.objects.all()
    serializer_class = CoworkersSerializer
