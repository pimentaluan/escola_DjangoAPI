# Generated by Django 3.1.3 on 2024-04-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_remove_matricula_curso_matricula_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='celular',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
