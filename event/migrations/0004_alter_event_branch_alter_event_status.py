# Generated by Django 4.1.7 on 2023-03-10 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_delete_role_alter_branch_options'),
        ('event', '0003_event_end_date_event_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.branch'),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, 'Pending'), (2, 'Approved'), (3, 'Rejected'), (4, 'Complete'), (5, 'Cancel'), (6, 'Certified'), (7, 'Ongoing')], default=1),
        ),
    ]
