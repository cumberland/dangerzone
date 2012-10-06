from django.contrib import admin
from builder.models import *
import reversion


class VersioningAdmin(reversion.VersionAdmin):
    pass


class FormTracking(reversion.VersionAdmin):
    pass


class VariableTracking(reversion.VersionAdmin):
    pass


class OptionTracking(reversion.VersionAdmin):
    pass


admin.site.register(Project, ProjectTracking)

admin.site.register(Form, FormTracking)

admin.site.register(Variable, VariableTracking)

admin.site.register(Option, OptionTracking)

