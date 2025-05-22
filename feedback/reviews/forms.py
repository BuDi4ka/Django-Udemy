from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(
        label="Your name",
        max_length=100,
        error_messages={
            "required": "Please enter your name",
            "max_length": "Name is too long (max 100 characters)",
        },
    )
