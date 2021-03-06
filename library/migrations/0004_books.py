# Generated by Django 3.0.4 on 2020-04-07 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_delete_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('BookId', models.AutoField(primary_key=True, serialize=False)),
                ('BookTitle', models.CharField(default='Book Title', max_length=240)),
                ('BookEdition', models.CharField(default='0th', max_length=10)),
                ('BookPublisher', models.CharField(default='Publisher', max_length=150)),
                ('BookYearOfPublisher', models.DateField()),
                ('BookISBN', models.CharField(default='Book ISBN', max_length=100)),
                ('BookAvailbity', models.CharField(choices=[('Available', 'Available'), ('Notavailable', 'Not available')], max_length=40)),
                ('BookFile', models.FileField(default='book.pdf', upload_to='Library/')),
                ('BookCoverPage', models.ImageField(default='Cover Page', upload_to='Library/CoverPage')),
                ('BookAuthor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.BookAuthor')),
            ],
        ),
    ]
