from django import forms
from AmazonParser.models import Product

class SearchBarForm(forms.Form):
    Rechercher = forms.URLField(max_length=250)

class DeleteHistoryForm(forms.Form): 
    Products_to_delete=forms.ModelMultipleChoiceField(queryset=Product.objects.values_list('name', flat=True).order_by('name'))
    #Products_to_delete=forms.ModelMultipleChoiceField(queryset=Product.objects.all())









    

   
