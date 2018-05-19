# Generated by Django 2.0.1 on 2018-05-10 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='conceptoPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoAsistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoInstrumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('identificacion', models.CharField(max_length=255)),
                ('correo', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('eps', models.CharField(max_length=255)),
                ('alergico', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('nombre_madre', models.CharField(max_length=255)),
                ('identificacion_madre', models.CharField(max_length=255)),
                ('telefono_madre', models.CharField(max_length=255)),
                ('nombre_padre', models.CharField(max_length=255)),
                ('identificacion_padre', models.CharField(max_length=255)),
                ('telefono_padre', models.CharField(max_length=255)),
                ('nombre_emergencia', models.CharField(max_length=255)),
                ('telefono_emergencia', models.CharField(max_length=255)),
                ('nombre_retira_nino', models.CharField(max_length=255)),
                ('telefono_retira_nino', models.CharField(max_length=255)),
                ('enfermedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.Enfermedad')),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrumento', models.CharField(max_length=255)),
                ('observaciones', models.CharField(max_length=500)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.EstadoInstrumento')),
            ],
        ),
        migrations.CreateModel(
            name='mes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PagoEstudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadPago', models.IntegerField()),
                ('concepto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.conceptoPago')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.EstadoPago')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.Estudiante')),
                ('mes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.mes')),
            ],
        ),
        migrations.CreateModel(
            name='PagoProfesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=255)),
                ('cantidadPago', models.IntegerField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.EstadoPago')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('identificacion', models.CharField(max_length=255)),
                ('correo', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='profesor',
            name='tecnica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.Tecnica'),
        ),
        migrations.AddField(
            model_name='pagoprofesor',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.Profesor'),
        ),
        migrations.AddField(
            model_name='inventario',
            name='tecnica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.Tecnica'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='grado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.Grado'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.Sexo'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='tecnica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.Tecnica'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.EstadoAsistencia'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.Estudiante'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='tecnica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiero.Tecnica'),
        ),
    ]
