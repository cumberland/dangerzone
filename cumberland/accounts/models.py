from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class MyProfile(UserenaBaseProfile):
	user = models.OneToOneField(User,
								unique=True,
								verbose_name=_("user"),
								related_name="my_profile")
	# Example of adding additional fields below.
	# favourite_snack = models.CharField(_("favourite snack"), max_length=5)


from django import forms

class InviteForm(forms.Form):
    email = forms.EmailField()
    # message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass