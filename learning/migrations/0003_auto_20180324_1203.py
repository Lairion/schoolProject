# Generated by Django 2.0.2 on 2018-03-24 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_auto_20180324_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='learn_table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_marks', to='learning.LearnTable'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='who_get_mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_marks', to='schoolclasses.Pupil'),
        ),
    ]