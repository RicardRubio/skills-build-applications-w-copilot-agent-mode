from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ("octofit_tracker", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="leaderboard",
            name="period",
            field=models.CharField(default="weekly", max_length=20),
        ),
        migrations.AddField(
            model_name="workout",
            name="activity_type",
            field=models.CharField(default="Other", max_length=100),
        ),
        migrations.AddField(
            model_name="workout",
            name="difficulty",
            field=models.CharField(default="medium", max_length=20),
        ),
        migrations.AddField(
            model_name="workout",
            name="duration",
            field=models.IntegerField(default=30),
        ),
    ]
