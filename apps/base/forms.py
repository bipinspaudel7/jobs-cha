from django import forms


class DashboardQueryForm(forms.Form):
    query = forms.CharField(label="Search", max_length=150)
    site = forms.CharField(
        label="Site", max_length=100, required=True, widget=forms.HiddenInput()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["query"].widget.attrs.update(
            {
                "class": "form-control",
                "type": "search",
                "placeholder": "Search for a product",
            }
        )
        # Add ID to site.
        self.fields["site"].widget.attrs.update({"id": "site"})

    def clean_query(self):
        if query := self.cleaned_data.get("query"):
            return query
        else:
            raise forms.ValidationError("Please enter a search term")

    def clean_site(self):
        if site := self.cleaned_data.get("site"):
            return site
        else:
            raise forms.ValidationError("Please select a site")
