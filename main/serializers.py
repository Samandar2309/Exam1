from rest_framework import serializers
from unicodedata import category

from .models import (
    About, FAQ, Our_Clients, Comments, Contacts, Footer,
    Posts, ServiceCategories, Services, OurService, Contact,
    Pricing, PriceList, Teachers, Coworkers
)

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['title', 'description']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['title', 'question', 'answer']


class OurClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_Clients
        fields = ['title']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['name', 'profession', 'text']


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class FooterSerializer(serializers.ModelSerializer):
    contact = ContactsSerializer(read_only=True)

    class Meta:
        model = Footer
        fields = ['contact_id', 'title', 'contact']  # 'contact' maydonini qo'shdik


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['title', 'description']


class ServiceCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategories
        fields = ['name']


class ServicesSerializer(serializers.ModelSerializer):
    category = ServiceCategoriesSerializer()

    class Meta:
        model = Services
        fields = ['name', 'description', 'detail_info', 'read_link', 'category']


class OurServiceSerializer(serializers.ModelSerializer):
    category = ServiceCategoriesSerializer(read_only=True)  # ServiceCategoriesSerializer ni qo'shish

    class Meta:
        model = OurService
        fields = ['title', 'description', 'category']


class ContactSerializer(serializers.ModelSerializer):
    category = ServiceCategoriesSerializer()

    class Meta:
        model = Contact
        fields = ['comments', 'category']

    def create(self, validated_data):
        category_data = validated_data.pop("category")
        category_instance = ServiceCategories.objects.create(**category_data)
        contact_instance = Contact.objects.create(category=category_instance, **validated_data)
        return contact_instance
class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = ['price', 'description', 'order', 'sub_description']


class PriceListSerializer(serializers.ModelSerializer):
    pricing = PricingSerializer(many=True)

    class Meta:
        model = PriceList
        fields = ['title', 'description', 'pricing']


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['name', 'profession']


class CoworkersSerializer(serializers.ModelSerializer):
    teacher_id = serializers.IntegerField(write_only=True)  # Teacher ID ni qabul qilish
    teacher = TeachersSerializer(read_only=True)  # Teacher ma'lumotlarini olish

    class Meta:
        model = Coworkers
        fields = ['title', 'teacher_id', 'teacher']  # teacher_id maydonini qo'shish

    def create(self, validated_data):
        teacher_id = validated_data.pop('teacher_id')  # teacher_id ni olib tashlash
        coworker = Coworkers.objects.create(teacher_id=teacher_id,
                                            **validated_data)  # teacher_id bilan Coworker yaratish
        return coworker

class TranslatedAboutSerializer(AboutSerializer):
    class Meta(AboutSerializer.Meta):
        fields = [f"{field}_uz" for field in AboutSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in AboutSerializer.Meta.fields] + \
                 [f"{field}_en" for field in AboutSerializer.Meta.fields]


class TranslatedFAQSerializer(FAQSerializer):
    class Meta(FAQSerializer.Meta):
        fields = [f"{field}_uz" for field in FAQSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in FAQSerializer.Meta.fields] + \
                 [f"{field}_en" for field in FAQSerializer.Meta.fields]


class TranslatedOurClientsSerializer(OurClientsSerializer):
    class Meta(OurClientsSerializer.Meta):
        fields = [f"{field}_uz" for field in OurClientsSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in OurClientsSerializer.Meta.fields] + \
                 [f"{field}_en" for field in OurClientsSerializer.Meta.fields]


class TranslatedCommentsSerializer(CommentsSerializer):
    class Meta(CommentsSerializer.Meta):
        fields = [f"{field}_uz" for field in CommentsSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in CommentsSerializer.Meta.fields] + \
                 [f"{field}_en" for field in CommentsSerializer.Meta.fields]


class TranslatedContactsSerializer(ContactsSerializer):
    class Meta(ContactsSerializer.Meta):
        fields = [f"{field}_uz" for field in ContactsSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in ContactsSerializer.Meta.fields] + \
                 [f"{field}_en" for field in ContactsSerializer.Meta.fields]


class TranslatedFooterSerializer(FooterSerializer):
    class Meta(FooterSerializer.Meta):
        fields = [f"{field}_uz" for field in FooterSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in FooterSerializer.Meta.fields] + \
                 [f"{field}_en" for field in FooterSerializer.Meta.fields]


class TranslatedPostsSerializer(PostsSerializer):
    class Meta(PostsSerializer.Meta):
        fields = [f"{field}_uz" for field in PostsSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in PostsSerializer.Meta.fields] + \
                 [f"{field}_en" for field in PostsSerializer.Meta.fields]


class TranslatedServiceCategoriesSerializer(ServiceCategoriesSerializer):
    class Meta(ServiceCategoriesSerializer.Meta):
        fields = [f"{field}_uz" for field in ServiceCategoriesSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in ServiceCategoriesSerializer.Meta.fields] + \
                 [f"{field}_en" for field in ServiceCategoriesSerializer.Meta.fields]


class TranslatedServicesSerializer(ServicesSerializer):
    class Meta(ServicesSerializer.Meta):
        fields = [f"{field}_uz" for field in ServicesSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in ServicesSerializer.Meta.fields] + \
                 [f"{field}_en" for field in ServicesSerializer.Meta.fields]


class TranslatedOurServiceSerializer(OurServiceSerializer):
    class Meta(OurServiceSerializer.Meta):
        fields = [f"{field}_uz" for field in OurServiceSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in OurServiceSerializer.Meta.fields] + \
                 [f"{field}_en" for field in OurServiceSerializer.Meta.fields]


class TranslatedContactSerializer(ContactSerializer):
    class Meta(ContactSerializer.Meta):
        fields = [f"{field}_uz" for field in ContactSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in ContactSerializer.Meta.fields] + \
                 [f"{field}_en" for field in ContactSerializer.Meta.fields]


class TranslatedPricingSerializer(PricingSerializer):
    class Meta(PricingSerializer.Meta):
        fields = [f"{field}_uz" for field in PricingSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in PricingSerializer.Meta.fields] + \
                 [f"{field}_en" for field in PricingSerializer.Meta.fields]


class TranslatedPriceListSerializer(PriceListSerializer):
    class Meta(PriceListSerializer.Meta):
        fields = [f"{field}_uz" for field in PriceListSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in PriceListSerializer.Meta.fields] + \
                 [f"{field}_en" for field in PriceListSerializer.Meta.fields]


class TranslatedTeachersSerializer(TeachersSerializer):
    class Meta(TeachersSerializer.Meta):
        fields = [f"{field}_uz" for field in TeachersSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in TeachersSerializer.Meta.fields] + \
                 [f"{field}_en" for field in TeachersSerializer.Meta.fields]


class TranslatedCoworkersSerializer(CoworkersSerializer):
    class Meta(CoworkersSerializer.Meta):
        fields = [f"{field}_uz" for field in CoworkersSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in CoworkersSerializer.Meta.fields] + \
                 [f"{field}_en" for field in CoworkersSerializer.Meta.fields]

# Boshqa modellar uchun ham xuddi shunday tarzda ko'paytirish mumkin.
