# Generated by Django 3.2.7 on 2021-09-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empolyee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('empolyee_id', models.IntegerField()),
                ('citizan_document', models.FileField(upload_to='documents/')),
                ('adress', models.CharField(max_length=300)),
                ('position', models.CharField(choices=[('Junior', 'Junior'), ('Mid level', 'Mid level'), ('Senior', 'Senior')], default='Junior', max_length=30)),
            ],
        ),
    ]