from django.contrib import admin
from simpleform.models import *
import reversion

class YourModelAdmin(reversion.VersionAdmin):

	pass

admin.site.register(ProjectName, YourModelAdmin)

admin.site.register(VariableDescription)
