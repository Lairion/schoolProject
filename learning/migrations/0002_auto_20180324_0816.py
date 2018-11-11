# Generated by Django 2.0.2 on 2018-03-24 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learntable',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_learn_table', to='learning.Faculty'),
        ),
        migrations.AlterField(
            model_name='learntable',
            name='for_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_learn_table', to='schoolclasses.SchoolClass'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='learn_table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='learning.Faculty'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='who_get_mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_mark', to='schoolclasses.Pupil'),
        ),
    ]
