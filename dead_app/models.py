from django.db import models

# Create your models here.

class DeadUser(models.Model):
    du_id = models.AutoField(primary_key = True)
    du_name = models.CharField(max_length = 300, null = True, blank = True)
    du_reason = models.CharField(max_length = 300, null = True, blank = True)
    du_level = models.CharField(max_length = 300, null = True, blank = True)
    du_ispass = models.CharField(max_length = 300, null = True, blank = True, default = "no")
    du_token = models.CharField(max_length = 300, null = True, blank = True)
    du_apply_time = models.DateTimeField()
    du_approve_time = models.DateTimeField()
    class meta:
        db_table = 'dead_user'
        ordering = ['du_id']
    class admin:
        pass


class DeadUserUrlCenter(models.Model):
    duu_id = models.AutoField(primary_key = True)
    duu_user_name = models.ForeignKey(DeadUser,related_name="deaduserurl")
    duu_week_url_count = models.CharField(max_length = 300, null = True, blank = True)
    duu_week_url_surplus = models.CharField(max_length = 300, null = True, blank = True)
    duu_week_url_use = models.CharField(max_length = 300, null = True, blank = True)
    class meta:
        db_table = 'dead_user_url_center'
        ordering = ['duu_id']
    class admin:
        pass

class DeadUserSiteCenter(models.Model):
    dus_id = models.AutoField(primary_key = True)
    dus_user_name = models.ForeignKey(DeadUser,related_name="deadusersite")
    dus_day_site_name = models.CharField(max_length = 300, null = True, blank = True)
    dus_day_site_count = models.CharField(max_length = 300, null = True, blank = True)
    dus_day_site_surplus = models.CharField(max_length = 300, null = True, blank = True)
    dus_day_site_use = models.CharField(max_length = 300, null = True, blank = True)
    class meta:
        db_table = 'dead_user_site_center'
        ordering = ['dus_id']
    class admin:
        pass

class DeadSiteCenter(models.Model):
    ds_id = models.AutoField(primary_key = True)
    ds_site_name = models.CharField(max_length = 300, null = True, blank = True)
    ds_site_count = models.CharField(max_length = 300, null = True, blank = True)
    ds_site_surplus = models.CharField(max_length = 300, null = True, blank = True)
    ds_site_use = models.CharField(max_length = 300, null = True, blank = True)
    ds_site_last_submit_time = models.CharField(max_length = 300, null = True, blank = True)
    ds_site_last_submit_user_name = models.CharField(max_length = 300, null = True, blank = True)
    class meta:
        db_table = 'dead_site_center'
        ordering = ['dus_id']
    class admin:
        pass


class DeadJobCenter(models.Model):
    dj_id = models.AutoField(primary_key = True)
    dj_user_name = models.CharField(max_length = 300, null = True, blank = True)
    dj_submit_time = models.CharField(max_length = 300, null = True, blank = True, default="") 
    dj_crawl_time = models.CharField(max_length = 300, null = True, blank = True)
    dj_status = models.CharField(max_length = 300, null = True, blank = True)
    dj_priority = models.CharField(max_length = 300, null = True, blank = True)
    dj_res_scan_first_time = models.CharField(max_length = 300, null = True, blank = True)
    dj_res_scan_count = models.CharField(max_length = 300, null = True, blank = True)
    dj_res_scan_next_time = models.CharField(max_length = 300, null = True, blank = True)
    dj_res_scan_save = models.CharField(max_length = 300, null = True, blank = True)
    dj_res_scan_rate = models.CharField(max_length = 300, null = True, blank = True)
    class meta:
        db_table = 'dead_job_center'
        ordering = ['dcs_id']
    class admin:
        pass



