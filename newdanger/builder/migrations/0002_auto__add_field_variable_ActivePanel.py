# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Variable.ActivePanel'
        db.add_column('builder_variable', 'ActivePanel',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Variable.ActivePanel'
        db.delete_column('builder_variable', 'ActivePanel')


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
            'ActivePanel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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