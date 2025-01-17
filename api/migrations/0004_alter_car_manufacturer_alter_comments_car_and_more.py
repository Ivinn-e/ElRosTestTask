# Generated by Django 5.1.1 on 2024-09-13 06:52

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_comments_dateofcreation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='api.manufacturer'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.car'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=10000, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='email',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(9)], verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manufacturers', to='api.country'),
        ),
    ]
