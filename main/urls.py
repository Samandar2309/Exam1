from django.urls import path
from .views import (
    AboutViewSet,
    FAQViewSet,
    OurClientsViewSet,
    CommentsViewSet,
    ContactsViewSet,
    FooterViewSet,
    PostsViewSet,
    ServiceCategoriesViewSet,
    ServicesViewSet,
    OurServiceViewSet,
    ContactViewSet,
    PricingViewSet,
    PriceListViewSet,
    TeachersViewSet,
    CoworkersViewSet,
)

urlpatterns = [
    # About URLs
    path('about/', AboutViewSet.as_view({'get': 'list', 'post': 'create'}), name='about-list'),
    path('about/<int:pk>/', AboutViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='about-detail'),

    # FAQ URLs
    path('faqs/', FAQViewSet.as_view({'get': 'list', 'post': 'create'}), name='faq-list'),
    path('faqs/<int:pk>/', FAQViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='faq-detail'),

    # Our Clients URLs
    path('our-clients/', OurClientsViewSet.as_view({'get': 'list', 'post': 'create'}), name='our-clients-list'),
    path('our-clients/<int:pk>/', OurClientsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='our-clients-detail'),

    # Comments URLs
    path('comments/', CommentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='comments-list'),
    path('comments/<int:pk>/', CommentsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comments-detail'),

    # Contacts URLs
    path('contacts/', ContactsViewSet.as_view({'get': 'list', 'post': 'create'}), name='contacts-list'),
    path('contacts/<int:pk>/', ContactsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='contacts-detail'),

    # Footer URLs
    path('footer/', FooterViewSet.as_view({'get': 'list', 'post': 'create'}), name='footer-list'),
    path('footer/<int:pk>/', FooterViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='footer-detail'),

    # Posts URLs
    path('posts/', PostsViewSet.as_view({'get': 'list', 'post': 'create'}), name='posts-list'),
    path('posts/<int:pk>/', PostsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='posts-detail'),

    # Service Categories URLs
    path('service-categories/', ServiceCategoriesViewSet.as_view({'get': 'list', 'post': 'create'}), name='service-categories-list'),
    path('service-categories/<int:pk>/', ServiceCategoriesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='service-categories-detail'),

    # Services URLs
    path('services/', ServicesViewSet.as_view({'get': 'list', 'post': 'create'}), name='services-list'),
    path('services/<int:pk>/', ServicesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='services-detail'),

    # Our Service URLs
    path('our-service/', OurServiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='our-service-list'),
    path('our-service/<int:pk>/', OurServiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='our-service-detail'),

    # Contact URLs
    path('contact/', ContactViewSet.as_view({'get': 'list', 'post': 'create'}), name='contact-list'),
    path('contact/<int:pk>/', ContactViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='contact-detail'),

    # Pricing URLs
    path('pricing/', PricingViewSet.as_view({'get': 'list', 'post': 'create'}), name='pricing-list'),
    path('pricing/<int:pk>/', PricingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='pricing-detail'),

    # PriceList URLs
    path('price-list/', PriceListViewSet.as_view({'get': 'list', 'post': 'create'}), name='price-list-list'),
    path('price-list/<int:pk>/', PriceListViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='price-list-detail'),

    # Teachers URLs
    path('teachers/', TeachersViewSet.as_view({'get': 'list', 'post': 'create'}), name='teachers-list'),
    path('teachers/<int:pk>/', TeachersViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='teachers-detail'),

    # Coworkers URLs
    path('coworkers/', CoworkersViewSet.as_view({'get': 'list', 'post': 'create'}), name='coworkers-list'),
    path('coworkers/<int:pk>/', CoworkersViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='coworkers-detail'),
]
