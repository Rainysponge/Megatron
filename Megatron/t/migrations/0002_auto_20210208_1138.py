# Generated by Django 2.1.15 on 2021-02-08 03:38

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False # 添加atomic
    dependencies = [
        ('t', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='department',
            new_name='t_department',
        ),
        migrations.RenameModel(
            old_name='illness',
            new_name='t_illness',
        ),
        migrations.RenameModel(
            old_name='patient',
            new_name='t_patient',
        ),
        migrations.RenameModel(
            old_name='result',
            new_name='t_result',
        ),
        migrations.RenameModel(
            old_name='treatment',
            new_name='t_treatment',
        ),
    ]