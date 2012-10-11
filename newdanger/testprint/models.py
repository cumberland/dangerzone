from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import reversion

class NewPatient(models.Model):
	FirstName = models.CharField(verbose_name='First Name:', blank=False, null=False, max_length=100)
	LastName = models.CharField(verbose_name='Last Name:', blank=False, null=False, max_length=100)
	RHRN = models.CharField(verbose_name='RHRN:', blank=False, null=False, max_length=20)
	PHN = models.CharField(verbose_name='PHN:', blank=False, null=False, max_length=20)
		

class Consent(models.Model):
	ChartReview = models.BigIntegerField(verbose_name='You have my consent to review and use my health records including any images for research purposes provided any proposed research project undergoes and receives ethics review and approval keeping with current Canadian and provincial standards.', blank=False, null=False)
	BioSamples = models.BigIntegerField(verbose_name='You have my consent to store, review, and use my excised biosamples for research purposes and to correlate these with my health records provided any proposed research project undergoes and receives ethics review and approval with current Canadian provincial standards.', blank=False, null=False)
	ResearchContact = models.BigIntegerField(verbose_name='You have my consent to contact me if you think I may be eligible to participate in a research trial.', blank=False, null=False)
	PatientSigned = models.BigIntegerField(verbose_name='Patient/proxy has signed the consent form:', blank=False, null=False)
	WitnessSigned = models.BigIntegerField(verbose_name='Witness has signed the consent form:', blank=False, null=False)
	ConsentDate = models.DateField(verbose_name='Date of consent:', blank=False, null=False)
	ProxyConsent = models.BigIntegerField(verbose_name='Was consent given by the patient or a proxy:', blank=False, null=False)
	ProxyName = models.CharField(verbose_name='Name of proxy:', blank=True, null=True, max_length=200)
	ProxyRelationship = models.CharField(verbose_name='Relationship of proxy:', blank=True, null=True, max_length=100)
		

