# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Position.representative'
        db.add_column('positions_position', 'representative', self.gf('django.db.models.fields.related.ForeignKey')(related_name='positions', null=True, to=orm['auth.User']), keep_default=False)

        # Changing field 'Position.hours'
        db.alter_column('positions_position', 'hours', self.gf('weekgrid.WeekgridField')(max_length=127))


    def backwards(self, orm):
        
        # Deleting field 'Position.representative'
        db.delete_column('positions_position', 'representative_id')

        # Changing field 'Position.hours'
        db.alter_column('positions_position', 'hours', self.gf('volunteering.weekgrid.WeekgridField')(max_length=127))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'positions.organisation': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Organisation'},
            'charity_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'directions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'purpose': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'positions.position': {
            'Meta': {'object_name': 'Position'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'hours': ('weekgrid.WeekgridField', [], {'max_length': '127'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'oneoff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'positions'", 'to': "orm['positions.Organisation']"}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'positions'", 'null': 'True', 'to': "orm['auth.User']"}),
            'skills_gained': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['positions.Skill']", 'symmetrical': 'False'}),
            'spec_desirable': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'spec_essential': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'training_details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'training_provided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'positions.skill': {
            'Meta': {'object_name': 'Skill'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '31'})
        }
    }

    complete_apps = ['positions']
