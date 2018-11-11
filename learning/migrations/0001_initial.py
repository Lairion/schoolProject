# Generated by Django 2.0.2 on 2018-03-19 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schoolclasses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LearnTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.Faculty')),
                ('for_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolclasses.SchoolClass')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_date', models.DateField()),
                ('learn_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='learning.LearnTable')),
                ('who_get_mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_get_mark', to='schoolclasses.Pupil')),
            ],
        ),
        migrations.CreateModel(
            name='Pip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pips', models.IntegerField()),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pips', to='learning.Mark')),
            ],
        ),
    ]