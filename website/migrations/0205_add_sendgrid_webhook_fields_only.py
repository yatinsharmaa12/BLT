# Generated by Django 5.1.6 on 2025-02-21 22:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0204_ossharticle_osshcommunity_osshdiscussionchannel_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="email_bounce_reason",
            field=models.TextField(blank=True, help_text="Reason for email bounce if applicable", null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="email_click_count",
            field=models.PositiveIntegerField(default=0, help_text="Number of email link clicks"),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="email_last_event",
            field=models.CharField(blank=True, help_text="Last email event from SendGrid", max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="email_last_event_time",
            field=models.DateTimeField(blank=True, help_text="Timestamp of last email event", null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="email_open_count",
            field=models.PositiveIntegerField(default=0, help_text="Number of email opens"),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="email_spam_report",
            field=models.BooleanField(default=False, help_text="Whether the email was marked as spam"),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="email_status",
            field=models.CharField(
                blank=True, help_text="Current email status from SendGrid", max_length=50, null=True
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="email_unsubscribed",
            field=models.BooleanField(default=False, help_text="Whether the user has unsubscribed"),
        ),
    ]
