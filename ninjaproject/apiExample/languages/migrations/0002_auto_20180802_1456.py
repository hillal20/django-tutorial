# Generated by Django 2.1 on 2018-08-02 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paradigm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Programer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='language',
            name='paradigm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.Paradigm'),
        ),
        migrations.AddField(
            model_name='programer',
            name='language',
            field=models.ManyToManyField(to='languages.Language'),
        ),
    ]
