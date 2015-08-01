# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Offer'
        db.create_table('offers_offer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['positions.Position'])),
            ('volunteer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='offers_made', to=orm['auth.User'])),
            ('representative', self.gf('django.db.models.fields.related.ForeignKey')(related_name='offers_recieved', to=orm['auth.User'])),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(related_name='offers_confirmed', to=orm['auth.User'])),
            ('time_volunteer_accepted', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('time_representative_accepted', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('time_staff_accepted', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('offers', ['Offer'])


    def backwards(self, orm):
        
        # Deleting model 'Offer'
        db.delete_table('offers_offer')


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
        'offers.offer': {
            'Meta': {'object_name': 'Offer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['positions.Position']"}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'offers_recieved'", 'to': "orm['auth.User']"}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'offers_confirmed'", 'to': "orm['auth.User']"}),
            'time_representative_accepted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_staff_accepted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_volunteer_accepted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'offers_made'", 'to': "orm['auth.User']"})
        },
        'positions.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '31'})
        },
        'positions.position': {
            'Meta': {'object_name': 'Position'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hours': ('weekgrid.WeekgridField', [], {'max_length': '127'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'positions'", 'to': "orm['positions.Organisation']"})
        }
    }

    complete_apps = ['offers']
