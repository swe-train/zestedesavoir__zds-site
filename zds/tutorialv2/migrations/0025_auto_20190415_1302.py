# Generated by Django 2.1.5 on 2019-04-15 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tutorialv2", "0024_publicationevent"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contentread",
            options={"verbose_name": "Contenu lu", "verbose_name_plural": "Contenus lus"},
        ),
    ]