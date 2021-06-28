# Generated by Django 3.2.4 on 2021-06-28 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graphql_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='graphql_api.user')),
            ],
        ),
    ]