# Generated by Django 4.1.7 on 2023-06-17 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD1', '0004_datosventasentrenamiento_prediccionventa_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datospredeterminados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conjunto_id', models.CharField(default='Predeterminado', max_length=10, unique=True, verbose_name='Identificador de datos')),
                ('fecha', models.DateField(verbose_name='Fecha de venta')),
                ('ganancia', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ganancia por dia')),
            ],
        ),
        migrations.CreateModel(
            name='DatosVentaUsuario',
            fields=[
                ('conjunto_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Identificador de datos')),
                ('datos', models.JSONField(default='Sin datos', verbose_name='Datos de venta')),
                ('cod_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD1.usuario', verbose_name='Usuario')),
            ],
        ),
        migrations.RemoveField(
            model_name='datosventasentrenamiento',
            name='cod_usuario',
        ),
        migrations.RemoveField(
            model_name='prediccionventa',
            name='cantidad_venta',
        ),
        migrations.RemoveField(
            model_name='prediccionventa',
            name='cod_datosentrenamiento',
        ),
        migrations.RemoveField(
            model_name='prediccionventa',
            name='cod_datosventasentrenamiento',
        ),
        migrations.RemoveField(
            model_name='prediccionventa',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='prediccionventa',
            name='ganancia',
        ),
        migrations.RemoveField(
            model_name='prediccionventa',
            name='precio_unitario',
        ),
        migrations.AddField(
            model_name='prediccionventa',
            name='datos',
            field=models.JSONField(default='Sin datos', verbose_name='Datos de la predicción'),
        ),
        migrations.DeleteModel(
            name='Datosentrenamiento',
        ),
        migrations.DeleteModel(
            name='Datosventasentrenamiento',
        ),
        migrations.AddField(
            model_name='prediccionventa',
            name='cod_entrenamiento_predeterminado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CRUD1.datospredeterminados', to_field='conjunto_id', verbose_name='Conjunto de datos de entrenamiento predeterminados'),
        ),
        migrations.AddField(
            model_name='prediccionventa',
            name='cod_entrenamiento_usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CRUD1.datosventausuario', verbose_name='Conjunto de datos de entrenamiento del Usuario'),
        ),
    ]