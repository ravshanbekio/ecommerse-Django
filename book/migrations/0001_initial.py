# Generated by Django 3.2.9 on 2022-03-19 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('base_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tovar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tovar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_user.main_user')),
            ],
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(default=1)),
                ('tovar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tovar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_user.main_user')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_time', models.IntegerField()),
                ('general_sum', models.IntegerField()),
                ('status', models.CharField(default='Progress', max_length=30)),
                ('box', models.ManyToManyField(to='book.Box')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_user.main_user')),
            ],
        ),
    ]