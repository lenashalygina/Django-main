from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(pk=True, serialize=False, unique=True)),
                ('text', models.CharField(max_length=250)),
            ],
        ),
    ]
