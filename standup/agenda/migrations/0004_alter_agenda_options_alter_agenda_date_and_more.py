# Generated by Django 4.2.6 on 2023-10-08 17:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("agenda", "0003_alter_agenda_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="agenda",
            options={
                "get_latest_by": ["-date"],
                "ordering": ["-date"],
                "verbose_name": "Agenda",
                "verbose_name_plural": "Agendas",
            },
        ),
        migrations.AlterField(
            model_name="agenda",
            name="date",
            field=models.CharField(
                default="2023-10-08", primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="section",
            field=models.CharField(
                choices=[
                    ("REVIEW", "Ticket Help or Review"),
                    ("MONITOR", "Ticket Monitoring"),
                    ("FOCUS", "Client's Need Focus or Attention"),
                    ("CALLS", "Upcoming Client Calls"),
                    ("INTERNAL", "Internal Tasks"),
                    ("NEEDS", "Team, Departmental, Organizaional Needs"),
                    ("UPDATES", "Personal, Social Updates"),
                    ("MISC", "Miscellaneous"),
                    ("DOCS", "Documentation Review and Enhancement"),
                    ("IFEAT", "internal Feature Requests"),
                ],
                max_length=65535,
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="status",
            field=models.CharField(
                choices=[
                    ("NEW", "New"),
                    ("OPEN", "Open"),
                    ("FYI", "Visibility Only"),
                    ("RESOLVED", "Resolved"),
                    ("ACCEPTED", "Feature Accepted"),
                    ("REJECTED", "Feature Rejected"),
                    ("BACKLOG", "Feature Pending"),
                ],
                default="NEW",
                max_length=65535,
            ),
        ),
    ]
