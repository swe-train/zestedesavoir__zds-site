# Generated by Django 2.1.5 on 2019-01-14 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0016_topic_solved_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="last_message",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="last_message",
                to="forum.Post",
                verbose_name="Dernier message",
            ),
        ),
        migrations.AlterField(
            model_name="topic",
            name="solved_by",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Utilisateur ayant noté le sujet comme résolu",
            ),
        ),
    ]