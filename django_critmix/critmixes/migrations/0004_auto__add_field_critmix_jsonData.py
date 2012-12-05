# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Critmix.jsonData'
        db.add_column('critmixes_critmix', 'jsonData',
                      self.gf('django.db.models.fields.TextField')(default="{'start': new Date(2012,5,1,0,0),'content': chee + '<br/>Criticism #1'}"),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Critmix.jsonData'
        db.delete_column('critmixes_critmix', 'jsonData')


    models = {
        'critmixes.crit': {
            'Meta': {'object_name': 'Crit'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'critique': ('django.db.models.fields.IntegerField', [], {}),
            'critmix': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['critmixes.Critmix']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {})
        },
        'critmixes.critmix': {
            'Meta': {'object_name': 'Critmix'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jsonData': ('django.db.models.fields.TextField', [], {'default': '"{\'start\': new Date(2012,5,1,0,0),\'content\': chee + \'<br/>Criticism #1\'}"'}),
            'mix_url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['critmixes']