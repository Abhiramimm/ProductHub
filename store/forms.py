from django import forms

from store.models import Category,Product

class CategoryForm(forms.ModelForm):

    class Meta:

        model=Category

        fields="__all__"

        widgets={
            "category_name":forms.TextInput(attrs={"class":"form-control w-50"})
        }

      
        
class ProductForm(forms.ModelForm):

    class Meta:

        model=Product

        fields="__all__"

    
