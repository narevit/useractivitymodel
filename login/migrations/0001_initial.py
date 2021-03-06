# Generated by Django 2.2.5 on 2020-08-10 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useremail', models.CharField(db_column='userEmail', max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=500, null=True)),
                ('lastlogindate', models.DateTimeField(blank=True, db_column='lastLoginDate', null=True)),
                ('createdon', models.DateTimeField(blank=True, db_column='createdOn', null=True)),
                ('loginattempts', models.IntegerField(blank=True, db_column='loginAttempts', null=True)),
            ],
        ),
    ]
