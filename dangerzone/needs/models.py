
class moFirstName(Audit):
	mvFirstName = models.CharField(verbose_name='First Name:', blank=True, null=True, max_length=100)
	def __unicode__(self):
		return "%s" % self.mvFirstName
	class Meta:
		get_latest_by = 'record'
		


class moLastName(Audit):
	mvLastName = models.CharField(verbose_name='Last Name:', blank=True, null=True, max_length=100)
	def __unicode__(self):
		return "%s" % self.mvLastName
	class Meta:
		get_latest_by = 'record'
		


class moRHN(Audit):
	mvRHN = models.CharField(verbose_name='RHN:', blank=False, null=False, max_length=10)
	def __unicode__(self):
		return "%s" % self.mvRHN
	class Meta:
		get_latest_by = 'record'
		


class moPHN(Audit):
	mvPHN = models.CharField(verbose_name='PHN:', blank=False, null=False, max_length=10)
	def __unicode__(self):
		return "%s" % self.mvPHN
	class Meta:
		get_latest_by = 'record'
		


class moSex(Audit):
	mvSex = models.RadioButton(verbose_name='Sex:', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvSex
	class Meta:
		get_latest_by = 'record'
		


class moDOB(Audit):
	mvDOB = models.DateField(verbose_name='DOB:', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvDOB
	class Meta:
		get_latest_by = 'record'
		


class moVisitDate(Audit):
	mvVisitDate = models.DateField(verbose_name='Date of Visit:', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvVisitDate
	class Meta:
		get_latest_by = 'record'
		


class moClinic(Audit):
	mvClinic = models.RadioButton(verbose_name='Clinic Recruited From:', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvClinic
	class Meta:
		get_latest_by = 'record'
		


class moPrelimConsent(Audit):
	mvPrelimConsent = models.BooleanField(verbose_name='Preliminary Consent:')
	def __unicode__(self):
		return "%s" % self.mvPrelimConsent
	class Meta:
		get_latest_by = 'record'
		


class moContactMethod(Audit):
	mvContactMethod = models.RadioButton(verbose_name='Preferred Method of Contact:', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvContactMethod
	class Meta:
		get_latest_by = 'record'
		


class moEmail(Audit):
	mvEmail = models.EmailField(verbose_name='E-mail Address:', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvEmail
	class Meta:
		get_latest_by = 'record'
		


class moPhoneNumb(Audit):
	mvPhoneNumb = models.CharField(verbose_name='Phone Number:', blank=True, null=True, max_length=16)
	def __unicode__(self):
		return "%s" % self.mvPhoneNumb
	class Meta:
		get_latest_by = 'record'
		


class moAltPhoneNumb(Audit):
	mvAltPhoneNumb = models.CharField(verbose_name='Alternate Phone Number:', blank=True, null=True, max_length=16)
	def __unicode__(self):
		return "%s" % self.mvAltPhoneNumb
	class Meta:
		get_latest_by = 'record'
		


class moMailAddress(Audit):
	mvMailAddress = models.TextField(verbose_name='Mailing Address:', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvMailAddress
	class Meta:
		get_latest_by = 'record'
		


class moAltContact(Audit):
	mvAltContact = models.CharField(verbose_name='Alternate Contact Person:', blank=True, null=True, max_length=100)
	def __unicode__(self):
		return "%s" % self.mvAltContact
	class Meta:
		get_latest_by = 'record'
		


class moAltContactPhone(Audit):
	mvAltContactPhone = models.CharField(verbose_name='Alternate Contact Phone Number:', blank=True, null=True, max_length=16)
	def __unicode__(self):
		return "%s" % self.mvAltContactPhone
	class Meta:
		get_latest_by = 'record'
		


class moAltContactRelation(Audit):
	mvAltContactRelation = models.CharField(verbose_name='Alternate Contact Relationship:', blank=True, null=True, max_length=200)
	def __unicode__(self):
		return "%s" % self.mvAltContactRelation
	class Meta:
		get_latest_by = 'record'
		


class moIncluded(Audit):
	mvIncluded = models.RadioButton(verbose_name='Included in Study:', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvIncluded
	class Meta:
		get_latest_by = 'record'
		


class moExcludeCalg(Audit):
	mvExcludeCalg = models.RadioButton(verbose_name='Lives in Calgary:', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvExcludeCalg
	class Meta:
		get_latest_by = 'record'
		


class moExcludeEnglish(Audit):
	mvExcludeEnglish = models.RadioButton(verbose_name='Fluent in English:', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvExcludeEnglish
	class Meta:
		get_latest_by = 'record'
		


class moExcludeOther(Audit):
	mvExcludeOther = models.RadioButton(verbose_name='Language/Hearing Impairment OR Severe Aphasia OR Moderate/Severe Developmental Delay OR Dementia:', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvExcludeOther
	class Meta:
		get_latest_by = 'record'
		


class moExcludeAge(Audit):
	mvExcludeAge = models.RadioButton(verbose_name='Patient <18 Years:', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvExcludeAge
	class Meta:
		get_latest_by = 'record'
		


class moPreConsentChart(Audit):
	mvPreConsentChart = models.RadioButton(verbose_name='Was pre-consent present in the chart:', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvPreConsentChart
	class Meta:
		get_latest_by = 'record'
		


class moPreConsentClinic(Audit):
	mvPreConsentClinic = models.RadioButton(verbose_name='Was pre-consent present in the clinic:', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvPreConsentClinic
	class Meta:
		get_latest_by = 'record'
		


class moPreferredName(Audit):
	mvPreferredName = models.CharField(verbose_name='Preferred Name:', blank=False, null=False, max_length=100)
	def __unicode__(self):
		return "%s" % self.mvPreferredName
	class Meta:
		get_latest_by = 'record'
		


class moConsentQuestionnaire(Audit):
	mvConsentQuestionnaire = models.RadioButton(verbose_name='Willing to complete the questionnaire:', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvConsentQuestionnaire
	class Meta:
		get_latest_by = 'record'
		


class moConsentInterview(Audit):
	mvConsentInterview = models.RadioButton(verbose_name='Willing to be contacted for additional phone interview:', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvConsentInterview
	class Meta:
		get_latest_by = 'record'
		


class moConsentAdditional(Audit):
	mvConsentAdditional = models.RadioButton(verbose_name='Permission to be contacted for additional studies:', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvConsentAdditional
	class Meta:
		get_latest_by = 'record'
		


class moConsentLink(Audit):
	mvConsentLink = models.RadioButton(verbose_name='Permission to link my study data with AHS and AHW health registry data:', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvConsentLink
	class Meta:
		get_latest_by = 'record'
		


class moDatafaxConsent(Audit):
	mvDatafaxConsent = models.BooleanField(verbose_name='Consent to Datafax:')
	def __unicode__(self):
		return "%s" % self.mvDatafaxConsent
	class Meta:
		get_latest_by = 'record'
		


class moDatafaxConfirmConsent(Audit):
	mvDatafaxConfirmConsent = models.BooleanField(verbose_name='Consent confirmed on Datafax:')
	def __unicode__(self):
		return "%s" % self.mvDatafaxConfirmConsent
	class Meta:
		get_latest_by = 'record'
		


class moQuestionnaireSent(Audit):
	mvQuestionnaireSent = models.BooleanField(verbose_name='Questionnaire Sent with Patient:')
	def __unicode__(self):
		return "%s" % self.mvQuestionnaireSent
	class Meta:
		get_latest_by = 'record'
		


class moQuestionnaireComplete(Audit):
	mvQuestionnaireComplete = models.BooleanField(verbose_name='Questionnaire Complete:')
	def __unicode__(self):
		return "%s" % self.mvQuestionnaireComplete
	class Meta:
		get_latest_by = 'record'
		


class moDatafaxQuestionnaire(Audit):
	mvDatafaxQuestionnaire = models.BooleanField(verbose_name='Questionnaire to Datafax:')
	def __unicode__(self):
		return "%s" % self.mvDatafaxQuestionnaire
	class Meta:
		get_latest_by = 'record'
		


class moDatafaxConfirmQuestionnaire(Audit):
	mvDatafaxConfirmQuestionnaire = models.BooleanField(verbose_name='Questionnaire confirmed on Datafax:')
	def __unicode__(self):
		return "%s" % self.mvDatafaxConfirmQuestionnaire
	class Meta:
		get_latest_by = 'record'
		

