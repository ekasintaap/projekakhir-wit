# Generated by Django 4.2 on 2023-06-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("toko", "0008_alter_alamatpengiriman_options_payment_order_payment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produkitem",
            name="kategori",
            field=models.CharField(
                choices=[
                    ("MA", "Makanan"),
                    ("MI", "Minuman"),
                    ("SC", "Skin Care"),
                    ("O", "Obat"),
                ],
                max_length=2,
            ),
        ),
    ]
