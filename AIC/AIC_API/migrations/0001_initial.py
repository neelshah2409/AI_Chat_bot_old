# Generated by Django 3.2.5 on 2022-07-31 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AIC_APP', '0004_yobotuser_apikey'),
        ('rest_framework_api_key', '0005_auto_20220110_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('api_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_framework_api_key.apikey')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AIC_APP.yobotuser')),
            ],
            options={
                'db_table': 'AIC_API',
            },
        ),
    ]
