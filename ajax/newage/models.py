from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms import Textarea, Select, RadioSelect, TextInput
import re
import reversion
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.forms.models import modelformset_factory

class FormVersion(models.Model):
	inactive = models.TextField()
	def __unicode__(self):
		return "%s" % self.inactive

class Name(models.Model):
	name = models.CharField(max_length=100, verbose_name="Name:")
	newname = models.CharField(max_length=100, verbose_name="NewName:")
	inactive = models.ForeignKey(FormVersion, editable=False)
	# def save(self, *args, **kwargs):
	# 	reversion.set_comment('Some comment')
	# 	super(Name, self).save(*args, **kwargs)

class NewName(models.Model):
	name = models.CharField(max_length=100, verbose_name="Name:")
	newname = models.CharField(max_length=100, verbose_name="NewName:")
	def __unicode__(self):
		return "%s %s" % (self.name, self.newname)

reversion.register(Name)


cosztype = [(0, 'Simple Partial'), (1, 'Complex Partial'), (2, 'Generalized T/C'), (3, 'Secondary Generalized T/C'), (4, 'Absence'), (5, 'Tonic'), (6, 'Atonic'), (7, 'Myoclonic'), (8, 'Non-Epileptic - Psychogenic'), (9, 'Syncope'), (10, 'Unknown'), (11, 'Larval'), (12, 'Other')]
copb = [(0, 'Patient'), (1, 'Other'), (2, 'None')]
coptstatus = [(0, 'Awake'), (1, 'Drowsy'), (2, 'Asleep')]

class Seizure(models.Model):
	number = models.BigIntegerField(blank=True, null=True)
	date = models.DateField(blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	onset = models.DateTimeField(blank=True, null=True)
	offset = models.DateTimeField(blank=True, null=True)
	sztype = models.BigIntegerField(blank=True, null=True)
	pb = models.BigIntegerField(blank=True, null=True)
	ptstatus = models.BigIntegerField(blank=True, null=True)
	techclinical = models.TextField(verbose_name="Tech Clinical:",blank=True, null=True)
	techeeg = models.TextField(verbose_name="Tech EEG:",blank=True, null=True)
	mdclinical = models.TextField(verbose_name="MD Clinical:",blank=True, null=True)
	mdeeg = models.TextField(verbose_name="MD EEG:",blank=True, null=True)

class mfSeizure(ModelForm):
	class Meta:
		model = Seizure
		widgets = {
	'techclinical': Textarea(attrs={'rows': 3, 'class': 'span8'}),
	'techeeg': Textarea(attrs={'rows': 3, 'class': 'span8'}),
	'mdclinical': Textarea(attrs={'rows': 3, 'class': 'span8'}),
	'mdeeg': Textarea(attrs={'rows': 3, 'class': 'span8'}),
	'sztype': Select(choices=cosztype),
	'pb': RadioSelect(choices=copb),
	'ptstatus': RadioSelect(choices=coptstatus),
	'date': TextInput(attrs={'class':'span1'}),
	'time': TextInput(attrs={'class':'span1'}),
	'onset': TextInput(attrs={'class':'span1'}),
	'offset': TextInput(attrs={'class':'span1'}),
	'number': TextInput(attrs={'class':'span1'})
	}	

SeizureFormSet = modelformset_factory(Seizure, form=mfSeizure)

class mfNewName(ModelForm):
	class Meta:
		model = NewName

class mfName(ModelForm):
	class Meta:
		model = Name
	def __init__(self, *args, **kwargs):
		super(mfName, self).__init__(*args, **kwargs)
		if kwargs.has_key('instance'):
			a = eval(kwargs['instance'].inactive.inactive)
			for i in a:
				del self.fields[i]
		else:
			a = eval(FormVersion.objects.filter().order_by('-id')[0].inactive)
			print a
			for i in a:
				del self.fields[i]
  #       not kwargs['instance'].is_foo_bar()):
  #       del self.fields['bar']
		# del self.fields['newname']



NameFormSet = modelformset_factory(NewName)

def print_keyword_args(**kwargs):
# kwargs is a dict of the keyword args passed to the function
	for key, value in kwargs.iteritems():
		print "%s = %s" % (key, value)


# @receiver(reversion.pre_revision_commit)
# def it_worked(sender, **kwargs):
# 	print "Got the signal."
# 	currentVersion = kwargs.pop('versions')[0].field_dict
# 	pastVersion = reversion.get_for_object(kwargs.pop('instances')[0])[0].field_dict
# 	changes = set(currentVersion.items()) - set(pastVersion.items())
# 	changedVars = []
# 	for var in changes:
# 		changedVars.append(var[0])
# 	comment = "Changed: %s" % ", ".join(changedVars)
# 	revision = kwargs.pop('revision')
# 	revision.comment = comment
# 	revision.save()
# 	kwargs['revision'] = revision
	# print dir(sender.get_for_object)
	# print dir(sender)
	# sender.save_revision
	# print_keyword_args(**kwargs)
	# print dir(kwargs.pop('instances'))
	# print dir(kwargs.pop('revision'))
	# for i in kwargs.pop('instances'):
	# 	print dir(i)
	# 	print dir(i.clean_fields)

