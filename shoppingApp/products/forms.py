from django import forms
from.models import Post, Categories

# Dynamic
# ToDo: create a function
choices = Categories.objects.all().values_list('name', 'name')

choiceList = []
for item in choices:
    choiceList.append(item)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('productName', 'brand', 'price', 'productImage', 'rating',
                  'category', 'seller', 'productDetails'
                  )  # # Select the fields on the page to create the product
        widgets = {
            'productName': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'productImage': forms.FileInput(attrs={'class': 'form-control', 'accept':"image/x-png,image/gif,image/jpeg"}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'max: 5 and min: 1'}),
            # 'seller': forms.Select(attrs={'class': 'form-control'}),
            'seller': forms.TextInput(attrs={'value': '', 'id': 'seller', 'type': 'hidden'}),
            'category': forms.Select(choices=choiceList, attrs={ 'class': 'form-control'}),
            'productDetails': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('productName', 'brand', 'price', 'rating', 'category',
                  'productDetails'
                  )  # # Select the fields on the page to create the product
        widgets = {
            'productName': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'max: 5 and min: 1'}),
            'category': forms.Select(choices=choiceList, attrs={'class': 'form-control'}),
            'productDetails': forms.Textarea(attrs={'class': 'form-control'}),
        }

class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ('name',)  # # Select the fields on the page to create the product

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }