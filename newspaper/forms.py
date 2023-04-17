from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from newspaper.models import Newspaper, Redactor


class NewspaperForm(forms.ModelForm):
    redactors = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class NewspaperSearchForm(forms.Form):
    model = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title..."})
    )


class RedactorSearchForm(forms.Form):
    model = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username..."})
    )


class TopicSearchForm(forms.Form):
    model = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."})
    )


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )

    # def clean_years_of_experience(self):
    #     return validate_years_of_experience(self.cleaned_data["years_of_experience"])


class RedactorExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ["years_of_experience"]

    # def clean_years_of_experience(self):
    #     return validate_years_of_experience(self.cleaned_data["years_of_experience"])
    #

# def validate_years_of_experience(
#     years_of_experience,
# ):  # regex validation is also possible here
#     if len(license_number) != 8:
#         raise ValidationError("License number should consist of 8 characters")
#     elif not license_number[:3].isupper() or not license_number[:3].isalpha():
#         raise ValidationError("First 3 characters should be uppercase letters")
#     elif not license_number[3:].isdigit():
#         raise ValidationError("Last 5 characters should be digits")
#
#     return license_number
