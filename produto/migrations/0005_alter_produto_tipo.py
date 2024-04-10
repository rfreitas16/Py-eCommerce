# Generated by Django 5.0.4 on 2024-04-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_alter_variacao_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('V', 'Variavel'), ('S', 'Simples')], default='V', max_length=1),
        ),
    ]
