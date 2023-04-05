# Generated by Django 4.2 on 2023-04-05 18:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_type',
            field=models.CharField(choices=[('expense', '支出'), ('income', '收入')], default='expense', max_length=100),
        ),
        migrations.CreateModel(
            name='TransferRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_occurrence', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('currency', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.currency')),
                ('from_account', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_account', to='accounting.account')),
                ('to_account', models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_account', to='accounting.account')),
            ],
            options={
                'ordering': ['-time_of_occurrence'],
            },
        ),
    ]
