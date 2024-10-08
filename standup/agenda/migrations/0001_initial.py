# Generated by Django 4.2.6 on 2024-08-03 02:39

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import martor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportEngineer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Support Engineer',
                'verbose_name_plural': 'Support Engineers',
                'db_table': 'team_members',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='SupportMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edition', models.CharField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'Decemeber')], max_length=3)),
                ('year', models.IntegerField(default=2024)),
            ],
            options={
                'verbose_name': 'Support Mail Edition',
                'verbose_name_plural': 'Support Mail Editions',
                'db_table': 'support_mail_editions',
                'ordering': ['-year', 'edition'],
            },
        ),
        migrations.CreateModel(
            name='WIN_OOPS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_occurred', models.DateField(auto_now=True)),
                ('type_of_incident', models.CharField(choices=[('WIN', 'Win!'), ('OOPS', 'Oops')], max_length=5)),
                ('clients_involved', models.CharField(max_length=255, null=True)),
                ('description', martor.models.MartorField()),
                ('added_to_supportmail', models.BooleanField(default=False)),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Win and Mistake',
                'verbose_name_plural': 'Wins and Mistakes',
                'db_table': 'wins_mistakes',
                'ordering': ['-date_occurred'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_resolved', models.DateField(blank=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('OPEN', 'Open'), ('FYI', 'Visibility Only'), ('RESOLVED', 'Resolved'), ('PUBLISHED', 'Published'), ('ACCEPTED', 'Feature Accepted'), ('REJECTED', 'Feature Rejected'), ('BACKLOG', 'Feature Pending')], default='NEW', max_length=65535)),
                ('section', models.CharField(choices=[('REVIEW', 'Ticket Help or Review'), ('MONITOR', 'Ticket Monitoring'), ('FOCUS', "Client's Need Focus or Attention"), ('CALLS', 'Upcoming Client Calls'), ('INTERNAL', 'Internal Tasks'), ('NEEDS', 'Team, Departmental, Organizaional Needs'), ('UPDATES', 'Personal, Social Updates'), ('MISC', 'Miscellaneous'), ('DOCS', 'Documentation Review and Enhancement'), ('IFEAT', 'internal Feature Requests')], max_length=65535)),
                ('title', models.CharField(default='', max_length=65535)),
                ('link_to_ticket', models.URLField(blank=True, default='', null=True)),
                ('description', martor.models.MartorField()),
                ('notes', martor.models.MartorField(blank=True, default='', null=True)),
                ('next_task_needed_to_resolve', models.CharField(blank=True, max_length=65535, null=True)),
                ('added_to_supportmail', models.BooleanField(default=False)),
                ('added_to_supportmail_on', models.DateField(blank=True, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('owner_of_next_task_needed_to_resolve', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='item_task_owner', to=settings.AUTH_USER_MODEL)),
                ('supportmail_edition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='agenda.supportmail')),
            ],
            options={
                'verbose_name': 'Agenda Item',
                'verbose_name_plural': 'Agenda Item',
                'db_table': 'items',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('date', models.CharField(default='YYYY-MM-DD', primary_key=True, serialize=False, unique=True)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='driver', to=settings.AUTH_USER_MODEL)),
                ('notetaker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='notetaker', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
                'db_table': 'agendas',
                'ordering': ['-date'],
                'get_latest_by': ['date'],
            },
        ),
    ]
