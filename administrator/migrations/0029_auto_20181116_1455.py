# Generated by Django 2.1.1 on 2018-11-16 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0028_section_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='grade_level',
            field=models.CharField(choices=[('0', 'Kinder'), ('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV'), ('5', 'V'), ('6', 'VI')], max_length=1),
        ),
    ]
