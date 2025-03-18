# Generated by Django 5.1.3 on 2025-02-22 06:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('confirmed', 'confirmed'), ('cancelled', 'cancelled')], default='Cancelled', max_length=10)),
                ('shipping_address', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.TextField(null=True)),
                ('links', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('price', models.TextField(blank=True, null=True)),
                ('dis_price', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_list', models.TextField(blank=True, null=True)),
                ('sales_package', models.TextField(blank=True, db_column='Sales_Package', null=True)),
                ('model_number', models.TextField(blank=True, db_column='Model_Number', null=True)),
                ('part_number', models.TextField(blank=True, db_column='Part_Number', null=True)),
                ('model_name', models.TextField(blank=True, db_column='Model_Name', null=True)),
                ('series', models.TextField(blank=True, db_column='Series', null=True)),
                ('color', models.TextField(blank=True, db_column='Color', null=True)),
                ('type', models.TextField(blank=True, db_column='Type', null=True)),
                ('suitable_for', models.TextField(blank=True, db_column='Suitable_For', null=True)),
                ('power_supply', models.TextField(blank=True, db_column='Power_Supply', null=True)),
                ('battery_cell', models.TextField(blank=True, db_column='Battery_Cell', null=True)),
                ('ms_office_provided', models.TextField(blank=True, db_column='MS_Office_Provided', null=True)),
                ('processor_brand', models.TextField(blank=True, db_column='Processor_Brand', null=True)),
                ('processor_name', models.TextField(blank=True, db_column='Processor_Name', null=True)),
                ('ssd', models.TextField(blank=True, db_column='SSD', null=True)),
                ('ssd_capacity', models.TextField(blank=True, db_column='SSD_Capacity', null=True)),
                ('ram', models.TextField(blank=True, db_column='RAM', null=True)),
                ('ram_type', models.TextField(blank=True, db_column='RAM_Type', null=True)),
                ('processor_variant', models.TextField(blank=True, db_column='Processor_Variant', null=True)),
                ('clock_speed', models.TextField(blank=True, db_column='Clock_Speed', null=True)),
                ('graphic_processor', models.TextField(blank=True, db_column='Graphic_Processor', null=True)),
                ('storage_type', models.TextField(blank=True, db_column='Storage_Type', null=True)),
                ('operating_system', models.TextField(blank=True, db_column='Operating_System', null=True)),
                ('usb_port', models.TextField(blank=True, db_column='USB_Port', null=True)),
                ('hdmi_port', models.TextField(blank=True, db_column='HDMI_Port', null=True)),
                ('touchscreen', models.TextField(blank=True, db_column='Touchscreen', null=True)),
                ('screen_size', models.TextField(blank=True, db_column='Screen_Size', null=True)),
                ('screen_resolution', models.TextField(blank=True, db_column='Screen_Resolution', null=True)),
                ('screen_type', models.TextField(blank=True, db_column='Screen_Type', null=True)),
                ('speakers', models.TextField(blank=True, db_column='Speakers', null=True)),
                ('internal_mic', models.TextField(blank=True, db_column='Internal_Mic', null=True)),
                ('wireless_lan', models.TextField(blank=True, db_column='Wireless_LAN', null=True)),
                ('bluetooth', models.TextField(blank=True, db_column='Bluetooth', null=True)),
                ('dimensions', models.TextField(blank=True, db_column='Dimensions', null=True)),
                ('weight', models.TextField(blank=True, db_column='Weight', null=True)),
                ('disk_drive', models.TextField(blank=True, db_column='Disk_Drive', null=True)),
                ('web_camera', models.TextField(blank=True, db_column='Web_Camera', null=True)),
                ('keyboard', models.TextField(blank=True, db_column='Keyboard', null=True)),
                ('backlit_keyboard', models.TextField(blank=True, db_column='Backlit_Keyboard', null=True)),
                ('warranty_summary', models.TextField(blank=True, db_column='Warranty_Summary', null=True)),
                ('warranty_service_type', models.TextField(blank=True, db_column='Warranty_Service_Type', null=True)),
                ('covered_in_warranty', models.TextField(blank=True, db_column='Covered_in_Warranty', null=True)),
                ('not_covered_in_warranty', models.TextField(blank=True, db_column='Not_Covered_in_Warranty', null=True)),
                ('emmc_storage_capacity', models.TextField(blank=True, db_column='EMMC_Storage_Capacity', null=True)),
                ('battery_backup', models.TextField(blank=True, db_column='Battery_Backup', null=True)),
                ('number_of_cores', models.TextField(blank=True, db_column='Number_of_Cores', null=True)),
                ('mic_in', models.TextField(blank=True, db_column='Mic_In', null=True)),
                ('sound_properties', models.TextField(blank=True, db_column='Sound_Properties', null=True)),
                ('pointer_device', models.TextField(blank=True, db_column='Pointer_Device', null=True)),
                ('included_software', models.TextField(blank=True, db_column='Included_Software', null=True)),
                ('additional_features', models.TextField(blank=True, db_column='Additional_Features', null=True)),
                ('domestic_warranty', models.TextField(blank=True, db_column='Domestic_Warranty', null=True)),
                ('expandable_memory', models.TextField(blank=True, db_column='Expandable_Memory', null=True)),
                ('processor_generation', models.TextField(blank=True, db_column='Processor_Generation', null=True)),
                ('finger_print_sensor', models.TextField(blank=True, db_column='Finger_Print_Sensor', null=True)),
                ('ram_frequency', models.TextField(blank=True, db_column='RAM_Frequency', null=True)),
                ('cache', models.TextField(blank=True, db_column='Cache', null=True)),
                ('multi_card_slot', models.TextField(blank=True, db_column='Multi_Card_Slot', null=True)),
                ('hardware_interface', models.TextField(blank=True, db_column='Hardware_Interface', null=True)),
                ('refresh_rate', models.TextField(blank=True, db_column='Refresh_Rate', null=True)),
                ('dedicated_graphic_memory_type', models.TextField(blank=True, db_column='Dedicated_Graphic_Memory_Type', null=True)),
                ('dedicated_graphic_memory_capacity', models.TextField(blank=True, db_column='Dedicated_Graphic_Memory_Capacity', null=True)),
                ('face_recognition', models.TextField(blank=True, db_column='Face_Recognition', null=True)),
                ('memory_slots', models.TextField(blank=True, db_column='Memory_Slots', null=True)),
                ('supported_operating_system', models.TextField(blank=True, db_column='Supported_Operating_System', null=True)),
                ('rj11', models.TextField(blank=True, db_column='RJ11', null=True)),
                ('rj45', models.TextField(blank=True, db_column='RJ45', null=True)),
                ('laptop_bag', models.TextField(blank=True, db_column='Laptop_Bag', null=True)),
                ('cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=10)),
                ('is_vendor', models.BooleanField(default=False)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='photos/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
    ]
