# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DeadUser'
        db.create_table(u'dead_app_deaduser', (
            ('du_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('du_name', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('du_reason', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('du_level', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('du_ispass', self.gf('django.db.models.fields.CharField')(default='no', max_length=300, null=True, blank=True)),
            ('du_token', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('du_apply_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('du_approve_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'dead_app', ['DeadUser'])

        # Adding model 'DeadUserUrlCenter'
        db.create_table(u'dead_app_deaduserurlcenter', (
            ('duu_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('duu_user_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dead_app.DeadUser'])),
            ('duu_week_url_count', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('duu_week_url_surplus', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('duu_week_url_use', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal(u'dead_app', ['DeadUserUrlCenter'])

        # Adding model 'DeadUserSiteCenter'
        db.create_table(u'dead_app_deadusersitecenter', (
            ('dus_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dus_user_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dead_app.DeadUser'])),
            ('dus_day_site_name', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('dus_day_site_count', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('dus_day_site_surplus', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('dus_day_site_use', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal(u'dead_app', ['DeadUserSiteCenter'])

        # Adding model 'DeadSiteCenter'
        db.create_table(u'dead_app_deadsitecenter', (
            ('ds_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ds_site_name', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('ds_site_count', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('ds_site_surplus', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('ds_site_use', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('ds_site_last_submit_time', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('ds_site_last_submit_user_name', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal(u'dead_app', ['DeadSiteCenter'])

        # Adding model 'DeadJobCenter'
        db.create_table(u'dead_app_deadjobcenter', (
            ('dj_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dj_product_name', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('dj_submit_time', self.gf('django.db.models.fields.CharField')(default='', max_length=300, null=True, blank=True)),
            ('dj_crawl_time', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('dj_status', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('dj_priority', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('dj_res_scan_first_time', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('dj_res_scan_count', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('dj_res_scan_next_time', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('dj_res_scan_save', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('dj_res_scan_rate', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal(u'dead_app', ['DeadJobCenter'])


    def backwards(self, orm):
        # Deleting model 'DeadUser'
        db.delete_table(u'dead_app_deaduser')

        # Deleting model 'DeadUserUrlCenter'
        db.delete_table(u'dead_app_deaduserurlcenter')

        # Deleting model 'DeadUserSiteCenter'
        db.delete_table(u'dead_app_deadusersitecenter')

        # Deleting model 'DeadSiteCenter'
        db.delete_table(u'dead_app_deadsitecenter')

        # Deleting model 'DeadJobCenter'
        db.delete_table(u'dead_app_deadjobcenter')


    models = {
        u'dead_app.deadjobcenter': {
            'Meta': {'object_name': 'DeadJobCenter'},
            'dj_crawl_time': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'dj_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'dj_priority': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'dj_product_name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'dj_res_scan_count': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'dj_res_scan_first_time': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'dj_res_scan_next_time': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'dj_res_scan_rate': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'dj_res_scan_save': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'dj_status': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'dj_submit_time': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        u'dead_app.deadsitecenter': {
            'Meta': {'object_name': 'DeadSiteCenter'},
            'ds_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ds_site_count': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'ds_site_last_submit_time': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'ds_site_last_submit_user_name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'ds_site_name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'ds_site_surplus': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'ds_site_use': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        u'dead_app.deaduser': {
            'Meta': {'object_name': 'DeadUser'},
            'du_apply_time': ('django.db.models.fields.DateTimeField', [], {}),
            'du_approve_time': ('django.db.models.fields.DateTimeField', [], {}),
            'du_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'du_ispass': ('django.db.models.fields.CharField', [], {'default': "'no'", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'du_level': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'du_name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'du_reason': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'du_token': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        u'dead_app.deadusersitecenter': {
            'Meta': {'object_name': 'DeadUserSiteCenter'},
            'dus_day_site_count': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'dus_day_site_name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'dus_day_site_surplus': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'dus_day_site_use': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'dus_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'dus_user_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dead_app.DeadUser']"})
        },
        u'dead_app.deaduserurlcenter': {
            'Meta': {'object_name': 'DeadUserUrlCenter'},
            'duu_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'duu_user_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dead_app.DeadUser']"}),
            'duu_week_url_count': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'duu_week_url_surplus': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'duu_week_url_use': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dead_app']