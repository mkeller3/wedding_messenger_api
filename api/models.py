from django.db import models


class accountData(models.Model):
    account_id = models.CharField(max_length=50, db_index=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    username = models.CharField(max_length=50, db_index=True, unique=True)
    phone_number = models.CharField(max_length=50)
    guests = models.IntegerField()
    date = models.DateTimeField()
    address = models.CharField(max_length=300)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rsvp_url = models.CharField(max_length=300)
    rsvp_alert = models.BooleanField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class guestData(models.Model):
    account_id = models.CharField(max_length=50, db_index=True)
    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email_address = models.CharField(max_length=50, default='', blank=True)
    full_address = models.CharField(max_length=300, default='', blank=True)
    latitude = models.FloatField(default=None, null=True)
    longitude = models.FloatField(default=None, null=True)
    drive_distance = models.IntegerField(default=None, null=True)
    rsvp_status = models.CharField(max_length=50, default='No Response')
    number_of_guests = models.IntegerField(default=None, null=True)
    comments = models.TextField(default='', blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class groupData(models.Model):
    account_id = models.CharField(max_length=50, db_index=True)
    group_name = models.CharField(max_length=50)
    guests = models.JSONField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class alertData(models.Model):
    account_id = models.CharField(max_length=50, db_index=True)
    message = models.TextField()
    group_message = models.BooleanField()
    group_ids = models.JSONField()
    alert_type = models.CharField(max_length=50)
    run_time = models.DateTimeField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class trialNumberData(models.Model):
    phone_number = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now=True)