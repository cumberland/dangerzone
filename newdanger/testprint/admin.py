from django.contrib import admin
from cep.models import *
import reversion

class VersioningAdmin(reversion.VersionAdmin):
    pass

admin.site.register(NewPatient, VersioningAdmin)

admin.site.register(Consent, VersioningAdmin)




