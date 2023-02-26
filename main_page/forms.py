from django import forms
from manager.models import UserReservation
from contact.models import UserContact


class UserReservationForm(forms.ModelForm):

    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                                'type': 'text',
                                'name': 'name',
                                'class': "form-control",
                                'id': "name",
                                'placeholder': "Ваше ім'я",
                                'data-rule': "minlen:4",
                                'data-msg': "Будь ласка, введіть принаймні 4 символи"
                           }))

    num_people = forms.IntegerField(widget=forms.NumberInput(attrs={
                                'type': 'number',
                                'class': 'form-control',
                                'name': 'people',
                                'id': 'people',
                                'placeholder': 'Кількість людей',
                                'data-rule': 'minlen:1',
                                'data-msg': 'Будь ласка, введіть принаймні 1 символ'
                            }))

    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
                                'type': 'text',
                                'class': 'form-control',
                                'name': 'phone',
                                'id': 'phone',
                                'placeholder': 'Ваш телефон',
                                'data-rule': 'minlen:4',
                                'data-msg': 'Будь ласка, введіть коректний номер телефону'
                            }))

    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
                                'class': 'form-control',
                                'name': 'message',
                                'rows': '5',
                                'placeholder': 'Повідомлення'
                            }))

    class Meta:
        model = UserReservation
        fields = ('name', 'num_people', 'phone', 'message')


class UserContactForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                'type': 'text',
                                'name': 'name',
                                'class': "form-control",
                                'id': 'name',
                                'placeholder': "Ваше ім'я"
    }))

    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                                'type': 'email',
                                'class': 'form-control',
                                'name': 'email',
                                'id': 'email',
                                'placeholder': 'Ваша пошта'
    }))

    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                'type': 'text',
                                'class': 'form-control',
                                'name': 'subject',
                                'id': 'subject',
                                'placeholder': 'Тема'
    }))

    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
                                'class': 'form-control',
                                'name': 'message',
                                'rows': '5',
                                'placeholder': 'Message'
    }))

    class Meta:
        model = UserContact
        fields = ('name', 'email', 'subject', 'message')
