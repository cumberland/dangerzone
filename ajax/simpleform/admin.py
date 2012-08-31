from django.contrib import admin
from simpleform.models import *
import reversion





admin.site.register(Appointment)

class VariableAdmin(reversion.VersionAdmin):
    pass

admin.site.register(VariableDescription, VariableAdmin)

admin.site.register(ProjectName, VariableAdmin)

