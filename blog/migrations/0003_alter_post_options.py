# Generated by Django 5.1.7 on 2025-03-14 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_author"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-pk"]},
        ),
    ]
