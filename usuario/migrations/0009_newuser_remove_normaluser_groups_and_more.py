# Generated by Django 4.2.6 on 2023-11-04 20:34

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('usuario', '0008_alter_adminuser_options_alter_normaluser_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user', models.CharField(default=None, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('huella', models.CharField(max_length=200)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_name='Newuser_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='Newuser_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='AdminUser',
        ),
        migrations.AlterField(
            model_name='faltas',
            name='ID_profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.newuser'),
        ),
    ]
