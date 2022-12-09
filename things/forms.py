"""Forms of the project."""

# Create your forms here.
class ThingForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'name':'name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'name':'description', 'rows':'3'}))
    quantity = forms.IntegerField()

    def clean(self):
        if len(self.cleaned_Data['name']) == 0 or len(self.cleaned_Data['description']) == 0 or self.cleaned_Data['quantity'] == 0:
            raise ValueError('Bad Data')