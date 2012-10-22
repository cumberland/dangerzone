from django.contrib import admin
from doubt.models import *
import reversion

class VersioningAdmin(reversion.VersionAdmin):
    pass

admin.site.register(NewPatient, VersioningAdmin)

admin.site.register(FollowUp24H, VersioningAdmin)

admin.site.register(FirstEvent, VersioningAdmin)

admin.site.register(CT, VersioningAdmin)

admin.site.register(MRI, VersioningAdmin)

admin.site.register(Doppler, VersioningAdmin)

admin.site.register(FollowUp, VersioningAdmin)

admin.site.register(StrokeOutcome, VersioningAdmin)

admin.site.register(FinalDiagnosis, VersioningAdmin)

admin.site.register(Baseline, VersioningAdmin)

admin.site.register(PlainCTVasc, VersioningAdmin)

admin.site.register(CTAWillisVasc, VersioningAdmin)

admin.site.register(OldInfarctVasc, VersioningAdmin)

