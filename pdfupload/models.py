

# Create your models here.
# from django.db import models
# # from django.utils import timezone
# class Dicty(models.Model):
#     name      = models.CharField(max_length=50)

# class KeyVal(models.Model):
#     container = models.ForeignKey(Dicty,on_delete=models.CASCADE,)
#     key       = models.CharField(max_length=240, )
#     value     = models.CharField(max_length=240,)




# class File(models.Model):
    # UR = models.CharField(max_length=200,blank=False, default='')
    # file = models.FileField(blank=False, null=False)
    # #Index=models.IntegerField(default=0)
    # #date=models.DateField(auto_now=False, auto_now_add=False,default=timezone.now)
    # Date=models.CharField(max_length=50,blank=False,default='')
    # Description=models.CharField(max_length=500,blank=False,default='')
    # Debit=models.FloatField(default=0)
    # Credit=models.FloatField(default=0)
   
    # def __str__(self):
    #     return self.file.name
# from djongo import models
# from django import forms

# class Data(models.Model):
    
#     Date=models.CharField(max_length=50,blank=False,default='')
#     Description=models.CharField(max_length=500,blank=False,default='')
#     Debit=models.FloatField(default=0)
#     Credit=models.FloatField(default=0)
#     def __str__(self):
#         return self.Description
#     class Meta:
#         abstract = True
# class DataForm(forms.ModelForm):
#     class Meta:
#         model = Data
#         fields = (
#             'Date','Description','Debit','Credit'
#         )


# class File(models.Model):
#     UR = models.CharField(max_length=200,blank=False, default='')
#     #file = models.FileField(blank=False, null=False)
#     DataSaved = models.ArrayField(
#         model_container=Data,
#         model_form_class=DataForm,
#         default=[0]
#     )
#     def __str__(self):
#         return self.UR
  
    # objects = models.DjongoManager()
from djongo import models
from django import forms


# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()

#     class Meta:
#         #abstract = True
#         def __str__(self):
#             return self.name
#     objects = models.DjongoManager()

# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = (
#             'name', 'tagline'
#         )

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    
    class Meta:
        #abstract = True
        def __str__(self):
            return self.name
    objects = models.DjongoManager()

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = (
            'name', 'email'
        )
        
class Entry(models.Model):
    # blog = models.EmbeddedField(
    #     model_container=Blog,
    #     model_form_class=BlogForm
    # )
    
    headline = models.CharField(max_length=255)    
    authors = models.ArrayField(
        model_container=Author,
        model_form_class=AuthorForm
    )
    
    objects = models.DjongoManager()




