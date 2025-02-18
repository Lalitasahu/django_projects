from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    address = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    is_vendor = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='photos/',  blank=True, null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/',null=True)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True )
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/',null=True)


class AppProductNew(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.TextField(null=True)
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


class Product(models.Model):    
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dis_price = models.DecimalField(max_digits=10,decimal_places=2)
    brand = models.CharField(max_length=20, null=True, blank=True)
    model = models.CharField(max_length=20,null=True, blank=True)
    storage = models.CharField(max_length=20, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField(default=True, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_list = models.ImageField(upload_to='photos/', null=True, blank=True)
    model_number = models.CharField(max_length=20,null=True,blank=True)
    Sales_Package = models.CharField(max_length=30,null=True,blank=True)
    Part_number = models.CharField(max_length=50,null=True,blank=True)
    model_name = models.CharField(max_length=50,null=True,blank=True)
    Series = models.CharField(max_length=50,null=True,blank=True)
    Color = models.CharField(max_length=50,null=True,blank=True)
    Type = models.CharField(max_length=50,null=True,blank=True)
    Suitable_For = models.CharField(max_length=50,null=True,blank=True)
    Power_Supply = models.CharField(max_length=50,null=True,blank=True)
    Battery_Cell = models.CharField(max_length=20,null=True,blank=True)
    MS_Office = models.CharField(max_length=20,null=True,blank=True)
    Processor_Brand = models.CharField(max_length=20,null=True,blank=True)
    Processor_Name = models.CharField(max_length=20,null=True,blank=True)
    SSD = models.CharField(max_length=20,null=True,blank=True)
    SSD_Capacity = models.CharField(max_length=20,null=True,blank=True)
    RAM = models.CharField(max_length=20,null=True,blank=True)
    RAM_Type = models.CharField(max_length=20,null=True,blank=True)
    Processor_Variant = models.CharField(max_length=50,null=True,blank=True)
    Clock_Speed = models.CharField(max_length=50,null=True,blank=True)
    Graphic_Processor = models.CharField(max_length=50,null=True,blank=True)
    Storage_Type = models.CharField(max_length=50,null=True,blank=True)
    Operating_System = models.CharField(max_length=50,null=True,blank=True)
    USB_Port = models.CharField(max_length=50,null=True,blank=True)
    HDMI_Port = models.CharField(max_length=50,null=True,blank=True)
    Touchscreen = models.CharField(max_length=20,null=True,blank=True)
    Screen_Size = models.CharField(max_length=50,null=True,blank=True)
    Screen_Resolution = models.CharField(max_length=50,null=True,blank=True)
    Screen_Type = models.CharField(max_length=50,null=True,blank=True)
    Speakers = models.CharField(max_length=50,null=True,blank=True)
    Internal_Mic = models.CharField(max_length=50,null=True,blank=True)
    Wireless_LAN = models.CharField(max_length=50,null=True,blank=True)
    Bluetooth = models.CharField(max_length=50,null=True,blank=True)
    Dimensions = models.CharField(max_length=50,null=True,blank=True)
    Weight = models.CharField(max_length=50,null=True,blank=True)
    Disk_Drive = models.CharField(max_length=50,null=True,blank=True)
    Web_Camera = models.CharField(max_length=50,null=True,blank=True)
    Keyboard = models.CharField(max_length=50,null=True,blank=True)
    Backlit_Keyboard = models.CharField(max_length=50,null=True,blank=True)
    Warranty_Summary = models.CharField(max_length=50,null=True,blank=True)
    Warranty_Service_Type = models.CharField(max_length=50,null=True,blank=True)
    Covered_in_Warranty = models.CharField(max_length=50,null=True,blank=True)
    Not_Covered_in_Warranty = models.CharField(max_length=50,null=True,blank=True)
    EMMC_Storage_Capacity = models.CharField(max_length=50,null=True,blank=True)
    Battery_Backup = models.CharField(max_length=50,null=True,blank=True)
    Number_of_Cores = models.CharField(max_length=50,null=True,blank=True)
    Mic_In = models.CharField(max_length=50,null=True,blank=True)
    Sound_Properties = models.CharField(max_length=50,null=True,blank=True)
    Pointer_Device = models.CharField(max_length=50,null=True,blank=True)
    Included_Software = models.CharField(max_length=50,null=True,blank=True)
    Additional_Features = models.CharField(max_length=50,null=True,blank=True)
    Domestic_Warranty = models.CharField(max_length=50,null=True,blank=True)
    Expandable_Memory = models.CharField(max_length=50,null=True,blank=True)
    Processor_Generation = models.CharField(max_length=50,null=True,blank=True)
    Finger_Print_Sensor = models.CharField(max_length=50,null=True,blank=True)
    RAM_Frequency = models.CharField(max_length=50,null=True,blank=True)
    Cache = models.CharField(max_length=50,null=True,blank=True)
    Multi_Card_Slot = models.CharField(max_length=50,null=True,blank=True)
    Hardware_Interface = models.CharField(max_length=50,null=True,blank=True)
    Refresh_Rate = models.CharField(max_length=50,null=True,blank=True)
    Dedicated_Graphic_Memory_Type = models.CharField(max_length=50,null=True,blank=True)
    Dedicated_Graphic_Memory_Capacity = models.CharField(max_length=50,null=True,blank=True)
    Face_Recognition = models.CharField(max_length=50,null=True,blank=True)
    Memory_Slots = models.CharField(max_length=50,null=True,blank=True)
    Supported_Operating_System = models.CharField(max_length=50,null=True,blank=True)
    RJ11 = models.CharField(max_length=50,null=True,blank=True)
    RJ45 = models.CharField(max_length=50,null=True,blank=True)
    Laptop_Bag = models.CharField(max_length=50,null=True,blank=True)
    Multi_Card_Slot = models.CharField(max_length=50,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Order(models.Model):
    STATUS = [
    ('pending', 'pending'),
    ('confirmed', 'confirmed'),
    ('cancelled', 'cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='Cancelled')
    shipping_address = models.TextField()

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='photos/')
    upload_date = models.DateTimeField(auto_now_add=True)

    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    # _date = models.DateTimeField(auto_now_add=True)
