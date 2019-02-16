# Generated by Django 2.1.5 on 2019-02-16 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20190216_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailuser',
            name='Specialization',
            field=models.CharField(choices=[('Pathologist', 'PATHOLOGIST'), ('Radiologist', 'RADIOLOGIST'), ('Obstetrician', 'OBSTETRICIAN'), ('Cardiologist', 'CARDIOLOGIST'), ('', '---------')], default='Pathologist', max_length=25, null=True),
        ),
    ]
