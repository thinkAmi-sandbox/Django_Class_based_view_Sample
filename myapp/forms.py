from django import forms
from .models import ItemModel

class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemModel
        fields = '__all__'
        # 項目を指定する場合
        # fields = ['name', 'unit_price',]
