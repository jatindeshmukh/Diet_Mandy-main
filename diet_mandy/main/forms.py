from django import forms

class InquiryForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your contact number'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Your age'})
    )
    gender = forms.ChoiceField(
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other'),
        ]
    )
    goal = forms.ChoiceField(
        choices=[
            ('Weight Loss', 'Weight Loss'),
            ('Weight Gain', 'Weight Gain'),
            ('Muscle Gain', 'Muscle Gain'),
            ('Diabetic Control', 'Diabetic Control'),
            ('PCOD / PCOS', 'PCOD / PCOS'),
        ]
    )
    food = forms.ChoiceField(
        choices=[
            ('Veg', 'Veg'),
            ('Non-Veg', 'Non-Veg'),
            ('Vegan', 'Vegan'),
        ]
    )
    routine = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Describe your daily routine'})
    )