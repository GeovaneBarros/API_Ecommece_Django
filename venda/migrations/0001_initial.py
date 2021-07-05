# Generated by Django 3.1.2 on 2021-07-02 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.ManyToManyField(to='core.Produto')),
            ],
            options={
                'verbose_name': 'Carrinho',
                'verbose_name_plural': 'Carrinhos',
            },
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frete', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pagamento', models.CharField(max_length=100)),
                ('data', models.DateField(auto_now_add=True)),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venda.carrinho')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.endereco')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
            },
        ),
    ]