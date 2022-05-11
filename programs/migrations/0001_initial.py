# Generated by Django 4.0.4 on 2022-05-11 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advantage', models.CharField(max_length=250, verbose_name='advantage of the program')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='name of program')),
                ('short_description', models.CharField(max_length=1000, verbose_name='short description of program')),
                ('application_deadline', models.DateField(blank=True, null=True, verbose_name='application deadline for program')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=250, unique=True, verbose_name='url ending of program')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='program description')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.course')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.offer')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.school')),
            ],
        ),
        migrations.AddIndex(
            model_name='offer',
            index=models.Index(fields=['name'], name='programs_of_name_c56035_idx'),
        ),
        migrations.AddIndex(
            model_name='offer',
            index=models.Index(fields=['slug'], name='programs_of_slug_e723ea_idx'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.offer'),
        ),
    ]