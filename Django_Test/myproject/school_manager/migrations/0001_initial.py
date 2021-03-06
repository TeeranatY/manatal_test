# Generated by Django 3.0.7 on 2020-06-07 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=20)),
                ('max_student_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student_School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_manager.School')),
                ('student_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_manager.Student')),
            ],
        ),
    ]
