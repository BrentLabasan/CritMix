# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Critmix'
        db.create_table('critmixes_critmix', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mix_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('critmixes', ['Critmix'])

        # Adding model 'Crit'
        db.create_table('critmixes_crit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('critmix', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['critmixes.Critmix'])),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('critique', self.gf('django.db.models.fields.IntegerField')()),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('critmixes', ['Crit'])


    def backwards(self, orm):
        # Deleting model 'Critmix'
        db.delete_table('critmixes_critmix')

        # Deleting model 'Crit'
        db.delete_table('critmixes_crit')


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
            'mix_url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['critmixes']