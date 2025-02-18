# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppProductNew(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    cat_id = models.IntegerField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    links = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    dis_price = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image_list = models.TextField(blank=True, null=True)
    sales_package = models.TextField(db_column='Sales_Package', blank=True, null=True)  # Field name made lowercase.
    model_number = models.TextField(db_column='Model_Number', blank=True, null=True)  # Field name made lowercase.
    part_number = models.TextField(db_column='Part_Number', blank=True, null=True)  # Field name made lowercase.
    model_name = models.TextField(db_column='Model_Name', blank=True, null=True)  # Field name made lowercase.
    series = models.TextField(db_column='Series', blank=True, null=True)  # Field name made lowercase.
    color = models.TextField(db_column='Color', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    suitable_for = models.TextField(db_column='Suitable_For', blank=True, null=True)  # Field name made lowercase.
    power_supply = models.TextField(db_column='Power_Supply', blank=True, null=True)  # Field name made lowercase.
    battery_cell = models.TextField(db_column='Battery_Cell', blank=True, null=True)  # Field name made lowercase.
    ms_office_provided = models.TextField(db_column='MS_Office_Provided', blank=True, null=True)  # Field name made lowercase.
    processor_brand = models.TextField(db_column='Processor_Brand', blank=True, null=True)  # Field name made lowercase.
    processor_name = models.TextField(db_column='Processor_Name', blank=True, null=True)  # Field name made lowercase.
    ssd = models.TextField(db_column='SSD', blank=True, null=True)  # Field name made lowercase.
    ssd_capacity = models.TextField(db_column='SSD_Capacity', blank=True, null=True)  # Field name made lowercase.
    ram = models.TextField(db_column='RAM', blank=True, null=True)  # Field name made lowercase.
    ram_type = models.TextField(db_column='RAM_Type', blank=True, null=True)  # Field name made lowercase.
    processor_variant = models.TextField(db_column='Processor_Variant', blank=True, null=True)  # Field name made lowercase.
    clock_speed = models.TextField(db_column='Clock_Speed', blank=True, null=True)  # Field name made lowercase.
    graphic_processor = models.TextField(db_column='Graphic_Processor', blank=True, null=True)  # Field name made lowercase.
    storage_type = models.TextField(db_column='Storage_Type', blank=True, null=True)  # Field name made lowercase.
    operating_system = models.TextField(db_column='Operating_System', blank=True, null=True)  # Field name made lowercase.
    usb_port = models.TextField(db_column='USB_Port', blank=True, null=True)  # Field name made lowercase.
    hdmi_port = models.TextField(db_column='HDMI_Port', blank=True, null=True)  # Field name made lowercase.
    touchscreen = models.TextField(db_column='Touchscreen', blank=True, null=True)  # Field name made lowercase.
    screen_size = models.TextField(db_column='Screen_Size', blank=True, null=True)  # Field name made lowercase.
    screen_resolution = models.TextField(db_column='Screen_Resolution', blank=True, null=True)  # Field name made lowercase.
    screen_type = models.TextField(db_column='Screen_Type', blank=True, null=True)  # Field name made lowercase.
    speakers = models.TextField(db_column='Speakers', blank=True, null=True)  # Field name made lowercase.
    internal_mic = models.TextField(db_column='Internal_Mic', blank=True, null=True)  # Field name made lowercase.
    wireless_lan = models.TextField(db_column='Wireless_LAN', blank=True, null=True)  # Field name made lowercase.
    bluetooth = models.TextField(db_column='Bluetooth', blank=True, null=True)  # Field name made lowercase.
    dimensions = models.TextField(db_column='Dimensions', blank=True, null=True)  # Field name made lowercase.
    weight = models.TextField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    disk_drive = models.TextField(db_column='Disk_Drive', blank=True, null=True)  # Field name made lowercase.
    web_camera = models.TextField(db_column='Web_Camera', blank=True, null=True)  # Field name made lowercase.
    keyboard = models.TextField(db_column='Keyboard', blank=True, null=True)  # Field name made lowercase.
    backlit_keyboard = models.TextField(db_column='Backlit_Keyboard', blank=True, null=True)  # Field name made lowercase.
    warranty_summary = models.TextField(db_column='Warranty_Summary', blank=True, null=True)  # Field name made lowercase.
    warranty_service_type = models.TextField(db_column='Warranty_Service_Type', blank=True, null=True)  # Field name made lowercase.
    covered_in_warranty = models.TextField(db_column='Covered_in_Warranty', blank=True, null=True)  # Field name made lowercase.
    not_covered_in_warranty = models.TextField(db_column='Not_Covered_in_Warranty', blank=True, null=True)  # Field name made lowercase.
    emmc_storage_capacity = models.TextField(db_column='EMMC_Storage_Capacity', blank=True, null=True)  # Field name made lowercase.
    battery_backup = models.TextField(db_column='Battery_Backup', blank=True, null=True)  # Field name made lowercase.
    number_of_cores = models.TextField(db_column='Number_of_Cores', blank=True, null=True)  # Field name made lowercase.
    mic_in = models.TextField(db_column='Mic_In', blank=True, null=True)  # Field name made lowercase.
    sound_properties = models.TextField(db_column='Sound_Properties', blank=True, null=True)  # Field name made lowercase.
    pointer_device = models.TextField(db_column='Pointer_Device', blank=True, null=True)  # Field name made lowercase.
    included_software = models.TextField(db_column='Included_Software', blank=True, null=True)  # Field name made lowercase.
    additional_features = models.TextField(db_column='Additional_Features', blank=True, null=True)  # Field name made lowercase.
    domestic_warranty = models.TextField(db_column='Domestic_Warranty', blank=True, null=True)  # Field name made lowercase.
    expandable_memory = models.TextField(db_column='Expandable_Memory', blank=True, null=True)  # Field name made lowercase.
    processor_generation = models.TextField(db_column='Processor_Generation', blank=True, null=True)  # Field name made lowercase.
    finger_print_sensor = models.TextField(db_column='Finger_Print_Sensor', blank=True, null=True)  # Field name made lowercase.
    ram_frequency = models.TextField(db_column='RAM_Frequency', blank=True, null=True)  # Field name made lowercase.
    cache = models.TextField(db_column='Cache', blank=True, null=True)  # Field name made lowercase.
    multi_card_slot = models.TextField(db_column='Multi_Card_Slot', blank=True, null=True)  # Field name made lowercase.
    hardware_interface = models.TextField(db_column='Hardware_Interface', blank=True, null=True)  # Field name made lowercase.
    refresh_rate = models.TextField(db_column='Refresh_Rate', blank=True, null=True)  # Field name made lowercase.
    dedicated_graphic_memory_type = models.TextField(db_column='Dedicated_Graphic_Memory_Type', blank=True, null=True)  # Field name made lowercase.
    dedicated_graphic_memory_capacity = models.TextField(db_column='Dedicated_Graphic_Memory_Capacity', blank=True, null=True)  # Field name made lowercase.
    face_recognition = models.TextField(db_column='Face_Recognition', blank=True, null=True)  # Field name made lowercase.
    memory_slots = models.TextField(db_column='Memory_Slots', blank=True, null=True)  # Field name made lowercase.
    supported_operating_system = models.TextField(db_column='Supported_Operating_System', blank=True, null=True)  # Field name made lowercase.
    rj11 = models.TextField(db_column='RJ11', blank=True, null=True)  # Field name made lowercase.
    rj45 = models.TextField(db_column='RJ45', blank=True, null=True)  # Field name made lowercase.
    laptop_bag = models.TextField(db_column='Laptop_Bag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'app_product_new'
