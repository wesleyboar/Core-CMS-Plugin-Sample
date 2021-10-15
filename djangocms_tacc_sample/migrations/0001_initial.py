# Generated by Django 2.2.16 on 2021-04-13 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaccsiteSample',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='taccsite_sample_taccsitesample', serialize=False, to='cms.CMSPlugin')),
                ('guest_name', models.CharField(blank=True, default='Guest', help_text='If user is logged in they are greeted by their name. If not logged in, they are greeted as this value. If this value is blank, they are greeted as "Guest".', max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]