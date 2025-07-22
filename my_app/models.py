from django.db import models


# # Create your models here.
# class Student(models.Model):
#     name = models.CharField(max_length=120)
#     age = models.PositiveSmallIntegerField()
#     place = models.CharField(max_length=180)
#     qualification = models.CharField(max_length=180)
#     phone_number = models.CharField(max_length=180)
#     hobby = models.CharField(max_length=120, default='2')
#
#     class Meta:
#         db_table = 'my_app_table'
#
#
# # navigation bar
# choice = [
#     ('microsoft 365', 'microsoft 365'),
#     ('Google workspace', 'Google work'),
#     ('zoho mail', 'zoho mail'),
#     ('professional email', 'professional email')
# ]
#
#
# class Email(models.Model):
#     name = models.CharField(max_length=120, unique=True)
#     choice = models.CharField(max_length=120, choices=choice, blank=True)
#
#     class Meta:
#         db_table = 'Email_table'
#
# choice1 = [
#     ('microsoft', 'microsoft'),
#     ('zoho', 'zoho'),
#     ('wasla', 'wasla'),
#     ('odoo', 'odoo')
# ]
#
#
# class Softwarebrands(models.Model):
#     name = models.CharField(max_length=120, blank=True, default="Softwarebrands")
#     choice1 = models.CharField(max_length=120, choices=choice1, blank=True)
#
#     class Meta:
#         db_table = 'Softwarebrands_table'
#
# choice2 = [
#     ('unified communication', 'unified communication'),
#     ('pos', 'pos'),
#     ('security system', 'security system'),
#     ('networking', 'networking')
# ]
#
#
# class Hardware(models.Model):
#     name = models.CharField(max_length=120, blank=True, default="Hardware")
#     choice2 = models.CharField(max_length=120, choices=choice2, blank=True)
#
#     class Meta:
#         db_table = 'Hardware_table'
#
# choice3 = [
#     ('sitlock', 'sitelock'),
#     ('ssl', 'ssl'),
#     ('acronis', 'acronis'),
# ]
#
#
# class Security(models.Model):
#     name = models.CharField(max_length=120, blank=True, default="Security")
#     choice2 = models.CharField(max_length=120, choices=choice3, blank=True)
#
#     class Meta:
#         db_table = 'Security_table'
#
#
# class Cloud(models.Model):
#     name = models.CharField(max_length=120, blank=True, default="Cloud")
#
#     class Meta:
#         db_table = 'Cloud_table'
#
#
# class Ondemandservices(models.Model):
#     name = models.CharField(max_length=120, blank=True, default="Ondemandservices")
#
#     class Meta:
#         db_table = 'Ondemandservices_table'
#
# class Findlocalinstallers(models.Model):
#     name = models.CharField(max_length=120, blank=True, default="Findlocalinstallers")
#
#     class Meta:
#         db_table = 'Findlocalinstallers_table'
#
# choice4 = [
#     ('aboutus', 'aboutus'),
#     ('blog', 'blog'),
#     ('contactus', 'contactus'),
# ]
#
#
# class Company(models.Model):
#     name = models.CharField(max_length=120, blank=True, default="Company")
#     choice4 = models.CharField(max_length=120, choices=choice4, blank=True)
#
#     class Meta:
#
#         db_table = 'Company_table'
# class Service(models.Model):
#     CATEGORY_CHOICES = [
#         ('email', 'Email & Collaboration'),
#         ('software', 'Software Brands'),
#         ('hardware', 'Hardware'),
#         ('security', 'Security & Backup'),
#         ('cloud', 'Cloud'),
#         ('ondemand', 'On Demand Services'),
#         ('installers', 'Find Local Installers'),
#         ('company', 'Company'),
#     ]
#
#     name = models.CharField(max_length=100)
#     category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
#     description = models.TextField(blank=True)
#     is_active = models.BooleanField(default=True)
#
#     def _str_(self):
#         return f"{self.name} ({self.get_category_display()})"


class Customer(models.Model):
    name = models.CharField(max_length=120)
    place = models.CharField(max_length=120)

    class Meta:
        db_table = "my_app_customer"


class Products(models.Model):
    name = models.CharField(max_length=120)
    price = models.PositiveSmallIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = "my_app_table"

    def __str__(self):
        return f"{self.name} - ₹{self.price}--"
