# Generated by Django 2.0.2 on 2018-03-05 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('0', 'New'), ('1', 'Removed'), ('2', 'Deprecated'), ('3', 'Replaced'), ('4', 'Splitted'), ('5', 'Merged')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(verbose_name='Date of creation')),
            ],
        ),
        migrations.CreateModel(
            name='PackageSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pes.Package')),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os_name', models.CharField(max_length=80)),
                ('major_version', models.CharField(max_length=4)),
                ('minor_version', models.CharField(max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='in_packageset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pes.PackageSet'),
        ),
        migrations.AddField(
            model_name='event',
            name='out_packageset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pes.PackageSet'),
        ),
        migrations.AddField(
            model_name='event',
            name='release',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pes.Release'),
        ),
    ]