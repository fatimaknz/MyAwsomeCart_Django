# Generated by Django 4.0.4 on 2022-06-22 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('head0', models.CharField(default='', max_length=500)),
                ('head1', models.CharField(default='', max_length=500)),
                ('head2', models.IntegerField(default=0, max_length=500)),
                ('pub_date', models.DateField()),
                ('thumnail', models.ImageField(default='', upload_to='shop/image')),
            ],
        ),
    ]
