# Generated by Django 2.2 on 2020-06-09 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('duocmobile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='materialApoyo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, null=True)),
                ('archivo', models.FileField(upload_to='media/')),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='material_curso', to='duocmobile.Curso')),
                ('docente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='docente_material', to='duocmobile.Docente')),
            ],
        ),
    ]
