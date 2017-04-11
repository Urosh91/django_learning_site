from django import forms
from django.core import validators

# custom val
# def must_be_empty(value):
#     if value:
#         raise forms.ValidationError('is not empty')


class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Please verify your email address')
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput, label='Leave empty',
                               validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        cleaned_data = super().clean()
        # calls clean on the whole SuggestionForm
        email = cleaned_data['email']
        verify = cleaned_data['verify_email']

        if email != verify:
            raise forms.ValidationError('Your email address does not match')


    # method
    # def clean_honeypot(self):
    #     # overwriting clean function on honeypot field
    #     honeypot = self.cleaned_data['honeypot']
    #     if len(honeypot):
    #         raise forms.ValidationError('honeypot field should be left empty')
    #     return honeypot



# A Form instance has an is_valid() method, which runs validation routines for all its fields.
# When this method is called, if all fields contain valid data, it will:
# return True
# place the form’s data in its cleaned_data attribute.