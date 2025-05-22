from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(
#         label="Your name",
#         max_length=100,
#         error_messages={
#             "required": "Please enter your name",
#             "max_length": "Name is too long (max 100 characters)",
#         },
#     )
#     review_text = forms.CharField(
#         label="Your feedback",
#         widget=forms.Textarea,
#         max_length=200,
#     )
#     rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)
#


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "user_name": "Your name",
            "review_text": "Your feedback",
            "rating": "Your rating",
        }
        widgets = {
            "review_text": forms.Textarea(attrs={"rows": 4, "cols": 40}),
        }
        error_messages = {
            "user_name": {
                "required": "Please enter your name",
                "max_length": "Name is too long (max 100 characters)",
            },
            "review_text": {
                "required": "Please enter your feedback",
                "max_length": "Feedback is too long (max 200 characters)",
            },
        }
