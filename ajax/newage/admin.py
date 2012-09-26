from django.contrib import admin
from newage.models import *
import reversion


admin.site.register(Name)

admin.site.register(NewName)

admin.site.register(FormVersion)

admin.site.register(Seizure)
