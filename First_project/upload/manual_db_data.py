import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('../db.sqlite3')
cursor = conn.cursor()

# Read Excel file
excel_file = 'products.xlsx'  
df = pd.read_excel(excel_file)

# Strip spaces from column names
df.columns = df.columns.str.strip()

# Check if 'id' column exists to avoid errors
# if 'id' in df.columns:
for index, row in df.iterrows():
    # Check if the product already exists
    cursor.execute("SELECT COUNT(*) FROM app_product WHERE id = ?", (row['id'],))
    if cursor.fetchone()[0] > 0:
    #     continue  # Skip inserting duplicate products
    
        # Insert new product
        cursor.execute("""INSERT INTO app_product 
            (name, price, dis_price, brand, model, stock, is_available, description, created_at, image_list, 
            model_number, Sales_Package, Part_number, model_name, Series, Color, Type, Suitable_For, Power_Supply, 
            Battery_Cell, MS_Office, Processor_Brand, Processor_Name, SSD, SSD_Capacity, RAM, RAM_Type, Processor_Variant, 
            Clock_Speed, Graphic_Processor, Storage_Type, Operating_System, USB_Port, HDMI_Port, Touchscreen, Screen_Size, 
            Screen_Resolution, Screen_Type, Speakers, Internal_Mic, Wireless_LAN, Bluetooth, Dimensions, Weight, Disk_Drive, 
            Web_Camera, Keyboard, Backlit_Keyboard, Warranty_Summary, Warranty_Service_Type, Covered_in_Warranty, 
            Not_Covered_in_Warranty, EMMC_Storage_Capacity, Battery_Backup, Number_of_Cores, Mic_In, Sound_Properties, 
            Pointer_Device, Included_Software, Additional_Features, Domestic_Warranty, Expandable_Memory, Processor_Generation, 
            Finger_Print_Sensor, RAM_Frequency, Cache, Hardware_Interface, Refresh_Rate, Dedicated_Graphic_Memory_Type, 
            Dedicated_Graphic_Memory_Capacity, Face_Recognition, Memory_Slots, Supported_Operating_System, RJ11, RJ45, 
            Laptop_Bag, category_id, user_id, storage) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
            row['title'], row['price'], row['dis_price'], row.get('brand', ''), row.get('model', ''), row.get('stock', 0), 
            row.get('is_available', 1), row['description'], row.get('created_at', ''), row['image_list'], row.get('model_number', ''), 
            row.get('Sales_Package', ''), row.get('Part_Number', ''), row.get('Model_Name', ''), row.get('Series', ''), 
            row.get('Color', ''), row.get('Type', ''), row.get('Suitable_For', ''), row.get('Power_Supply', ''), 
            row.get('Battery_Cell', ''), row.get('MS_Office_Provided', ''), row.get('Processor_Brand', ''), 
            row.get('Processor_Name', ''), row.get('SSD', ''), row.get('SSD_Capacity', ''), row.get('RAM', ''), 
            row.get('RAM_Type', ''), row.get('Processor_Variant', ''), row.get('Clock_Speed', ''), 
            row.get('Graphic_Processor', ''), row.get('Storage_Type', ''), row.get('Operating_System', ''), 
            row.get('USB_Port', ''), row.get('HDMI_Port', ''), row.get('Touchscreen', ''), row.get('Screen_Size', ''), 
            row.get('Screen_Resolution', ''), row.get('Screen_Type', ''), row.get('Speakers', ''), row.get('Internal_Mic', ''), 
            row.get('Wireless_LAN', ''), row.get('Bluetooth', ''), row.get('Dimensions', ''), row.get('Weight', ''), 
            row.get('Disk_Drive', ''), row.get('Web_Camera', ''), row.get('Keyboard', ''), row.get('Backlit_Keyboard', ''), 
            row.get('Warranty_Summary', ''), row.get('Warranty_Service_Type', ''), row.get('Covered_in_Warranty', ''), 
            row.get('Not_Covered_in_Warranty', ''), row.get('EMMC_Storage_Capacity', ''), row.get('Battery_Backup', ''), 
            row.get('Number_of_Cores', ''), row.get('Mic_In', ''), row.get('Sound_Properties', ''), row.get('Pointer_Device', ''), 
            row.get('Included_Software', ''), row.get('Additional_Features', ''), row.get('Domestic_Warranty', ''), 
            row.get('Expandable_Memory', ''), row.get('Processor_Generation', ''), row.get('Finger_Print_Sensor', ''), 
            row.get('RAM_Frequency', ''), row.get('Cache', ''), row.get('Multi_Card_Slot', ''), row.get('Hardware_Interface', ''), 
            row.get('Refresh_Rate', ''), row.get('Dedicated_Graphic_Memory_Type', ''), row.get('Dedicated_Graphic_Memory_Capacity', ''), 
            row.get('Face_Recognition', ''), row.get('Memory_Slots', ''), row.get('Supported_Operating_System', ''), 
            row.get('RJ11', ''), row.get('RJ45', ''), row.get('Laptop_Bag', ''), row['cat_id'], row['user_id'], None
        ))


# Commit and close connection
conn.commit()
conn.close()







# for run the script create cursor then connection then read excel and dump in sql
    # cursor = conn.cursor()
    # conn = sqlite3.connect('../db.sqlite3')
    # df = pd.read_excel('products.xlsx')
    # df.to_sql('app_product',con=conn,index=False)