from django.contrib import admin
from builder.models import *
import reversion

# admin.site.register(ProjectName)

# admin.site.register(VariableDescription)

# admin.site.register(Options)



class VariableAdmin(reversion.VersionAdmin):
    pass

admin.site.register(ProjectName, VariableAdmin)

admin.site.register(VariableDescription, VariableAdmin)

admin.site.register(Options)
