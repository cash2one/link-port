# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DeadSiteCenter.ds_site_last_submit_user_name'
        db.delete_column(u'dead_app_deadsitecenter', 'ds_site_last_submit_user_name')


    def backwards(self, orm):
        # Adding field 'DeadSiteCenter.ds_site_last_submit_user_name'
        db.add_column(u'dead_app_deadsitecenter', 'ds_site_last_submit_user_name',
                      self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True),
                      keep_default=False)


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