# Generated by Django 3.2.6 on 2021-08-23 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210823_0845'),
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='family',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
            preserve_default=False,
        ),
    ]