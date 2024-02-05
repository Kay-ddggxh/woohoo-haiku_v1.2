from .models import Haiku, Tanka
from django import forms


class HaikuForm(forms.ModelForm):
    """
    Form model that allows authenticated users to
    add and save haiku posts
    """

    class Meta:
        model = Haiku
        fields = (
            "title",
            "tag",
            "content",
        )

        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter a title"}),
            "tag": forms.Select(),
            "content": forms.Textarea(attrs={"placeholder": "Write Haiku here"}),
        }


class TankaForm(forms.ModelForm):
    """
    Form model that allows authenticated users to
    submit tankas on haikus
    """

    class Meta:
        model = Tanka
        fields = ("body",)
