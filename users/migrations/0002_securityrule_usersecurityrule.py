# Generated by Django 4.2 on 2023-05-03 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityRule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated_time', models.DateTimeField(auto_now=True)),
                ('creator', models.IntegerField()),
                ('last_updater', models.IntegerField()),
                ('category', models.CharField(choices=[('Screen', 'Screen'), ('Function', 'Function')], max_length=255)),
            ],
            options={
                'verbose_name': 'Security Rule',
                'verbose_name_plural': 'Security Rules',
            },
        ),
        migrations.CreateModel(
            name='UserSecurityRule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated_time', models.DateTimeField(auto_now=True)),
                ('creator', models.IntegerField()),
                ('last_updater', models.IntegerField()),
                ('security_rule', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.securityrule')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Security Rule',
                'verbose_name_plural': 'User Security Rules',
            },
        ),
    ]
