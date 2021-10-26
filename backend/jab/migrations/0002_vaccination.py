# Generated by Django 3.2.7 on 2021-10-25 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jabbed_on', models.DateField()),
                ('dose', models.BooleanField(default=False)),
                ('next_dose', models.DateField(blank=True, null=True)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jab.vaccine')),
                ('jabbed_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jab.facility')),
                ('jabbed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccinator', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccinatee', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-jabbed_on'],
            },
        ),
    ]