
class mfFirstName(ModelForm):
	class Meta:
		model = moFirstName
		
		


class mfLastName(ModelForm):
	class Meta:
		model = moLastName
		
		


class mfRHN(ModelForm):
	class Meta:
		model = moRHN
		
		


class mfPHN(ModelForm):
	class Meta:
		model = moPHN
		
		


class mfSex(ModelForm):
	class Meta:
		model = moSex
		
widgets = {
	'mvSex': RadioSelect(choices=coSex)
	}

		


class mfDOB(ModelForm):
	class Meta:
		model = moDOB
		
		


class mfVisitDate(ModelForm):
	class Meta:
		model = moVisitDate
		
		


class mfClinic(ModelForm):
	class Meta:
		model = moClinic
		
widgets = {
	'mvClinic': RadioSelect(choices=coClinic)
	}

		


class mfPrelimConsent(ModelForm):
	class Meta:
		model = moPrelimConsent
		
		


class mfContactMethod(ModelForm):
	class Meta:
		model = moContactMethod
		
widgets = {
	'mvContactMethod': RadioSelect(choices=coContactMethod)
	}

		


class mfEmail(ModelForm):
	class Meta:
		model = moEmail
		
		


class mfPhoneNumb(ModelForm):
	class Meta:
		model = moPhoneNumb
		
		


class mfAltPhoneNumb(ModelForm):
	class Meta:
		model = moAltPhoneNumb
		
		


class mfMailAddress(ModelForm):
	class Meta:
		model = moMailAddress
		
		


class mfAltContact(ModelForm):
	class Meta:
		model = moAltContact
		
		


class mfAltContactPhone(ModelForm):
	class Meta:
		model = moAltContactPhone
		
		


class mfAltContactRelation(ModelForm):
	class Meta:
		model = moAltContactRelation
		
		


class mfIncluded(ModelForm):
	class Meta:
		model = moIncluded
		
widgets = {
	'mvIncluded': RadioSelect(choices=coIncluded)
	}

		


class mfExcludeCalg(ModelForm):
	class Meta:
		model = moExcludeCalg
		
widgets = {
	'mvExcludeCalg': RadioSelect(choices=coExcludeCalg)
	}

		


class mfExcludeEnglish(ModelForm):
	class Meta:
		model = moExcludeEnglish
		
widgets = {
	'mvExcludeEnglish': RadioSelect(choices=coExcludeEnglish)
	}

		


class mfExcludeOther(ModelForm):
	class Meta:
		model = moExcludeOther
		
widgets = {
	'mvExcludeOther': RadioSelect(choices=coExcludeOther)
	}

		


class mfExcludeAge(ModelForm):
	class Meta:
		model = moExcludeAge
		
widgets = {
	'mvExcludeAge': RadioSelect(choices=coExcludeAge)
	}

		


class mfPreConsentChart(ModelForm):
	class Meta:
		model = moPreConsentChart
		
widgets = {
	'mvPreConsentChart': RadioSelect(choices=coPreConsentChart)
	}

		


class mfPreConsentClinic(ModelForm):
	class Meta:
		model = moPreConsentClinic
		
widgets = {
	'mvPreConsentClinic': RadioSelect(choices=coPreConsentClinic)
	}

		


class mfPreferredName(ModelForm):
	class Meta:
		model = moPreferredName
		
		


class mfConsentQuestionnaire(ModelForm):
	class Meta:
		model = moConsentQuestionnaire
		
widgets = {
	'mvConsentQuestionnaire': RadioSelect(choices=coConsentQuestionnaire)
	}

		


class mfConsentInterview(ModelForm):
	class Meta:
		model = moConsentInterview
		
widgets = {
	'mvConsentInterview': RadioSelect(choices=coConsentInterview)
	}

		


class mfConsentAdditional(ModelForm):
	class Meta:
		model = moConsentAdditional
		
widgets = {
	'mvConsentAdditional': RadioSelect(choices=coConsentAdditional)
	}

		


class mfConsentLink(ModelForm):
	class Meta:
		model = moConsentLink
		
widgets = {
	'mvConsentLink': RadioSelect(choices=coConsentLink)
	}

		


class mfDatafaxConsent(ModelForm):
	class Meta:
		model = moDatafaxConsent
		
		


class mfDatafaxConfirmConsent(ModelForm):
	class Meta:
		model = moDatafaxConfirmConsent
		
		


class mfQuestionnaireSent(ModelForm):
	class Meta:
		model = moQuestionnaireSent
		
		


class mfQuestionnaireComplete(ModelForm):
	class Meta:
		model = moQuestionnaireComplete
		
		


class mfDatafaxQuestionnaire(ModelForm):
	class Meta:
		model = moDatafaxQuestionnaire
		
		


class mfDatafaxConfirmQuestionnaire(ModelForm):
	class Meta:
		model = moDatafaxConfirmQuestionnaire
		
		

