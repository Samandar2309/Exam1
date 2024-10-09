from modeltranslation.translator import register, TranslationOptions
from .models import About, FAQ, Our_Clients, Comments, Posts, ServiceCategories, Services

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('title', 'question', 'answer')

@register(Our_Clients)
class OurClientsTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Comments)
class CommentsTranslationOptions(TranslationOptions):
    fields = ('name', 'profession', 'text')

@register(Posts)
class PostsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(ServiceCategories)
class ServiceCategoriesTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'detail_info')
