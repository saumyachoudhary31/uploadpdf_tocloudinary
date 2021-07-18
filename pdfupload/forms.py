from django import forms
from .models import File
class PDFUPLOADForms(forms.ModelForm):
    class Meta:
        model=File
        fields=[]
       
    def save(self,commit=True,*args,**kwargs):
        obj=super(PDFUPLOADForms,self).save(commit=False,*args,**kwargs)
        if commit:
            obj.UR=""
            obj.save()
        return obj