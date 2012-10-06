# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('builder_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ProjectName', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ProjectURL', self.gf('django.db.models.fields.SlugField')(max_length=18)),
            ('ProjectDescription', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('builder', ['Project'])

        # Adding model 'Form'
        db.create_table('builder_form', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ProjectID', self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='Form', to=orm['builder.Project'])),
            ('FormName', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('FormDescription', self.gf('django.db.models.fields.TextField')()),
            ('VariableOrder', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(default='[]', max_length=500, blank=True)),
        ))
        db.send_create_signal('builder', ['Form'])

        # Adding model 'Variable'
        db.create_table('builder_variable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('FormID', self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='Variable', to=orm['builder.Form'])),
            ('VarLabel', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('VarName', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('VarDescription', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('FieldType', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('VarBlank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('VarNull', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Identifier', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('VarMaxDigits', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('VarMaxDecimalPlaces', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('VarMaxLength', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('builder', ['Variable'])

        # Adding model 'Option'
        db.create_table('builder_option', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('VariableID', self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='Option', to=orm['builder.Variable'])),
            ('Value', self.gf('django.db.models.fields.BigIntegerField')()),
            ('Label', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal('builder', ['Option'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('builder_project')

        # Deleting model 'Form'
        db.delete_table('builder_form')

        # Deleting model 'Variable'
        db.delete_table('builder_variable')

        # Deleting model 'Option'
        db.delete_table('builder_option')


    models = {
        'builder.form': {
            'FormDescription': ('django.db.models.fields.TextField', [], {}),
            'FormName': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'Meta': {'object_name': 'Form'},
            'ProjectID': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'Form'", 'to': "orm['builder.Project']"}),
            'VariableOrder': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'default': "'[]'", 'max_length': '500', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'builder.option': {
            'Label': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Meta': {'object_name': 'Option'},
            'Value': ('django.db.models.fields.BigIntegerField', [], {}),
            'VariableID': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'Option'", 'to': "orm['builder.Variable']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'builder.project': {
            'Meta': {'object_name': 'Project'},
            'ProjectDescription': ('django.db.models.fields.TextField', [], {}),
            'ProjectName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ProjectURL': ('django.db.models.fields.SlugField', [], {'max_length': '18'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'builder.variable': {
            'FieldType': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'FormID': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'Variable'", 'to': "orm['builder.Form']"}),
            'Identifier': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'Variable'},
            'VarBlank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'VarDescription': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'VarLabel': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'VarMaxDecimalPlaces': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VarMaxDigits': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VarMaxLength': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VarName': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'VarNull': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['builder']