import django.forms

from product.models import Review


class ReviewForm(django.forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
