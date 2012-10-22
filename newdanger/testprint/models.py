from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import reversion

class NewPatient(models.Model):
	Name = models.CharField(verbose_name='Name:', blank=False, null=False, max_length=100)
	DOB = models.DateField(verbose_name='Date of birth:', blank=False, null=False)
	Gender = models.BigIntegerField(verbose_name='Gender:', blank=False, null=False)
	RHRN = models.CharField(verbose_name='RHRN:', blank=False, null=False, max_length=20)
	Address = models.TextField(verbose_name='Street address:', blank=False, null=False)
	HomePhone = models.CharField(verbose_name='Home phone:', blank=False, null=False, max_length=20)
	CellPhone = models.CharField(verbose_name='Cell phone:', blank=False, null=False, max_length=20)
	EmergContact = models.CharField(verbose_name='Emergency contact:', blank=False, null=False, max_length=200)
	OtherContact = models.CharField(verbose_name='Other contact:', blank=False, null=False, max_length=200)
		

class FollowUp24H(models.Model):
	FocalResolved = models.BigIntegerField(verbose_name='Does the patient feel the focal neurological symptoms are completely resolved?', blank=True, null=True)
	FocalDurationDays = models.PositiveIntegerField(verbose_name='Days', blank=True, null=True)
	FocalDurationHours = models.PositiveIntegerField(verbose_name='Hours', blank=True, null=True)
	FocalDurationMinutes = models.PositiveIntegerField(verbose_name='Minutes', blank=True, null=True)
	AllSymptomsResolved = models.BigIntegerField(verbose_name='Does the patient feel all symptoms of any kind (focal symptoms or associated symptoms) related to this event have resolved?', blank=True, null=True)
	SympDurationDays = models.PositiveIntegerField(verbose_name='Days', blank=True, null=True)
	SympDurationHours = models.PositiveIntegerField(verbose_name='Hours', blank=True, null=True)
	SympDurationMinutes = models.PositiveIntegerField(verbose_name='Minutes', blank=True, null=True)
	ResearchNurse = models.CharField(verbose_name='Research Nurse:', blank=True, null=True, max_length=100)
	Date = models.DateField(verbose_name='Date:', blank=True, null=True)
		

class FirstEvent(models.Model):
	
		

class CT(models.Model):
	CTHeadDateTime = models.DateTimeField(verbose_name='CT head exam date/time:', blank=True, null=True)
	CTADateTime = models.DateTimeField(verbose_name='CTA exam date/time:', blank=True, null=True)
	PlainCTInfarct = models.BigIntegerField(verbose_name='Acute/subacute infarct on plain CT only:', blank=True, null=True)
	PlainCTLesion = models.BigIntegerField(verbose_name='Lesion:', blank=True, null=True)
	PlainCTSide = models.BigIntegerField(verbose_name='Side(s):', blank=True, null=True)
	PlainCTCorticalGreyMatter = models.BooleanField(verbose_name='Cortical Grey Matter')
	PlainCTWhiteMatter = models.BooleanField(verbose_name='White Matter')
	PlainCTBasalGanglia = models.BooleanField(verbose_name='Basal Ganglia')
	PlainCTBrainstem = models.BooleanField(verbose_name='Brainstem nuclei or tracts')
	PlainCTMicrohemorrhage = models.BooleanField(verbose_name='Microhemorrhage in lesion (hyperdensity)')
	OldInfarct = models.BigIntegerField(verbose_name='Old infarcts on plain CT only:', blank=True, null=True)
	OldInfarctLesion = models.BigIntegerField(verbose_name='Lesion:', blank=True, null=True)
	OldInfarctSide = models.BigIntegerField(verbose_name='Side(s):', blank=True, null=True)
	CTASI = models.BigIntegerField(verbose_name='CTA-SI evidence of focal relative hypocontrastation of tissue:', blank=True, null=True)
	CTANeck = models.BigIntegerField(verbose_name='Neck CTA: (if not done nor MRA look for Carotid doppler)', blank=True, null=True)
	AorticArch = models.BigIntegerField(verbose_name='Aortic Arch:', blank=True, null=True)
	GreatVesselOrigin = models.BigIntegerField(verbose_name='Great vessel origins:', blank=True, null=True)
	GreatVesselSpecify = models.CharField(verbose_name='Which vessel?', blank=True, null=True, max_length=200)
	CTAWillis = models.BigIntegerField(verbose_name='CTA Circle of Willis:', blank=True, null=True)
	CTASIVisibleAcute = models.BigIntegerField(verbose_name='In a visible acute/subacute infarct:', blank=True, null=True)
	CTASIVisibleOld = models.BigIntegerField(verbose_name='In a visible old infarct:', blank=True, null=True)
	CTASIVisibleNoInfarct = models.BigIntegerField(verbose_name='In an area without visible acute infarct:', blank=True, null=True)
	WhiteMatterChangeRating = models.BigIntegerField(verbose_name='Age-related White matter changes rating:', blank=True, null=True)
		

class MRI(models.Model):
	
		

class Doppler(models.Model):
	
		

class FollowUp(models.Model):
	
		

class StrokeOutcome(models.Model):
	SymptomsDate = models.DateField(verbose_name='Date of the first few focal neurological symptoms:', blank=True, null=True)
		

class FinalDiagnosis(models.Model):
	
		

class Baseline(models.Model):
	ReferDateTime = models.DateTimeField(verbose_name='Date/Time:', blank=True, null=True)
	ReferFrom = models.BigIntegerField(verbose_name='From:', blank=True, null=True)
	StrokeAssessDateTime = models.DateTimeField(verbose_name='Date/Time:', blank=True, null=True)
	StrokeAssessFrom = models.BigIntegerField(verbose_name='From:', blank=True, null=True)
	PatientLocation = models.BigIntegerField(verbose_name='Location of Patient:', blank=True, null=True)
	MRIType = models.BigIntegerField(verbose_name='Type of MRI:', blank=True, null=True)
	FellowName = models.CharField(verbose_name='Fellow name:', blank=True, null=True, max_length=100)
	StaffName = models.CharField(verbose_name='Staff name:', blank=True, null=True, max_length=100)
	Hypertension = models.BooleanField(verbose_name='Hypertension')
	Diabetes = models.BooleanField(verbose_name='Diabetes')
	Dyslipidemia = models.BooleanField(verbose_name='Dyslipidemia')
	AFibFlutter = models.BooleanField(verbose_name='A.fib or Flutter')
	CurrentSmoking = models.BooleanField(verbose_name='Smoking (current)')
	CHD = models.BooleanField(verbose_name='CHD')
	ValveDisease = models.BooleanField(verbose_name='Heart valve disease')
	PVD = models.BooleanField(verbose_name='PVD')
	DiseaseHxNone = models.BooleanField(verbose_name='NONE of the above')
	ASA = models.BooleanField(verbose_name='ASA')
	Clopidogrel = models.BooleanField(verbose_name='Clopidogrel')
	Aggrenox = models.BooleanField(verbose_name='Aggrenox')
	Warfarin = models.BooleanField(verbose_name='Warfarin')
	Heparin = models.BooleanField(verbose_name='Full dose Heparin (SC)')
	Antihypertensive = models.BooleanField(verbose_name='Antihypertensive')
	OralHypoglycemic = models.BooleanField(verbose_name='Oral Hypoglycemic')
	Insulin = models.BooleanField(verbose_name='Insulin')
	Statin = models.BooleanField(verbose_name='Statin')
	OtherLipidAgent = models.BooleanField(verbose_name='Other lipid lowering agent')
	MedicationNone = models.BooleanField(verbose_name='NONE of the above')
		

class PlainCTVasc(models.Model):
	PlainCTVascTerritory = models.BigIntegerField(verbose_name='Territory', blank=True, null=True)
	PlainCTVascSide = models.BigIntegerField(verbose_name='Side', blank=True, null=True)
		

class CTAWillisVasc(models.Model):
	CTAWillisVascSide = models.BigIntegerField(verbose_name='Side', blank=True, null=True)
	CTAWillisVascSite = models.BigIntegerField(verbose_name='Site', blank=True, null=True)
	CTAWillisVascStenosis = models.BigIntegerField(verbose_name='Stenosis', blank=True, null=True)
		

class OldInfarctVasc(models.Model):
	OldInfarctVascTerritory = models.BigIntegerField(verbose_name='Territory', blank=True, null=True)
	OldInfarctVascSide = models.BigIntegerField(verbose_name='Side', blank=True, null=True)
		