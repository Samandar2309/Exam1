from django.db import models


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='about')

    def __str__(self):
        return self.title


class FAQ(models.Model):
    title = models.CharField(max_length=212)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.title


class Our_Clients(models.Model):
    title = models.CharField(max_length=212)
    icon = models.ImageField(upload_to='our_clients')

    def __str__(self):
        return self.title


class Comments(models.Model):
    name = models.CharField(max_length=212)
    profession = models.CharField(max_length=212)
    image = models.ImageField(upload_to='comments')
    text = models.TextField()

    def __str__(self):
        return self.name


class Contacts(models.Model):
    phone = models.CharField(max_length=212)
    email = models.EmailField()

    def __str__(self):
        return self.phone


class Footer(models.Model):
    title = models.CharField(max_length=212)
    icon = models.ImageField(upload_to='footer')
    contact = models.OneToOneField(Contacts, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.title


class Posts(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='posts')

    def __str__(self):
        return self.title


class ServiceCategories(models.Model):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=212)
    description = models.TextField()
    detail_info = models.TextField()
    read_link = models.URLField()
    category = models.ForeignKey(ServiceCategories, on_delete=models.CASCADE)


class OurService(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    category = models.ForeignKey(ServiceCategories, on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=212)
    phone = models.CharField(max_length=212)
    comments = models.TextField()
    category = models.ForeignKey(ServiceCategories, on_delete=models.CASCADE)


class Pricing(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    order = models.IntegerField()
    sub_description = models.TextField(blank=True, null=True)


class PriceList(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    pricing = models.ManyToManyField(Pricing)

    def __str__(self):
        return self.title


class Teachers(models.Model):
    name = models.CharField(max_length=212)
    profession = models.CharField(max_length=212)
    image = models.ImageField(upload_to='teachers')

    def __str__(self):
        return self.name


class Coworkers(models.Model):
    title = models.CharField(max_length=212)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
