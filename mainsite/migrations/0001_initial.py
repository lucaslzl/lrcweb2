# Generated by Django 2.1.1 on 2018-10-27 18:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.TextField()),
                ('year', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2018)])),
                ('type', models.CharField(choices=[('Book', 'Book'), ('Book Chapter', 'Book Chapter')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.TextField()),
                ('year', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2018)])),
                ('type', models.CharField(choices=[('Brazilian Conference', 'Brazilian Conference'), ('International Conference', 'International Conference')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.TextField()),
                ('year', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2018)])),
                ('type', models.CharField(choices=[('Brazilian Journal', 'Brazilian Journal'), ('International Journal', 'International Journal')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OnGoingThesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('site', models.CharField(blank=True, max_length=50, null=True)),
                ('lattes', models.CharField(blank=True, max_length=100, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('type', models.TextField(choices=[('Alumni', 'Alumni'), ('Collaborators', 'Collaborators'), ('MSc students', 'MSc students'), ('Pos-doc students', 'Pos-doc students'), ('PhD students', 'PhD students'), ('Professors', 'Professors'), ('Undergraduate students', 'Undergraduate students')], default='Alumni')),
                ('project', models.CharField(blank=True, max_length=200, null=True)),
                ('year', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2018)], verbose_name='Alumni Year')),
                ('title', models.TextField(blank=True, choices=[('Master', 'Master'), ('Doctor', 'Doctor'), ('Pos-doc', 'Pos-doc')], null=True, verbose_name='Alumni Title')),
                ('advisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.People')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('sponsor', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2018)])),
                ('type', models.CharField(choices=[('Sponsored Research', 'Sponsored Research'), ('International Cooperation Sponsored Research', 'International Cooperation Sponsored Research')], max_length=50)),
                ('state', models.CharField(choices=[('Current', 'Current'), ('Past', 'Past')], default='Current', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RecognitionAwards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.TextField()),
                ('year', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2018)])),
            ],
        ),
        migrations.CreateModel(
            name='ResearchTopics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.TextField()),
                ('year', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2018)])),
                ('authors', models.CharField(blank=True, max_length=200, null=True)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdfs/')),
            ],
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.TextField()),
                ('year', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2018)])),
                ('type', models.CharField(choices=[('Doctorate Thesis', 'Doctorate Thesis'), ('Master Thesis', 'Master Thesis')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='ongoingthesis',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.People'),
        ),
    ]