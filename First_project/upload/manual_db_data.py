import sqlite3
import os
import pandas as pd

conn = sqlite3.connect('../db.sqlite3')

# Create a cursor object 
cursor = conn.cursor()

# Read Excel file
excel_file = 'all_products.xlsx'  
df = pd.read_excel(excel_file)

# Insert data into SQLite
for index, row in df.iterrows():
    cursor.execute("SELECT COUNT(*) FROM app_product WHERE id = ?", (row['id'],))
    if cursor.fetchone()[0] == 0:  
        cursor.execute("INSERT INTO app_product VALUES ('name', 'price', 'dis_price', 'brand', 'model', 'stock', 'is_available', 'description', 'created_at', 'image_list', 'model_number', 'Sales_Package', 'Part_number', 'model_name', 'Series', 'Color', 'Type', 'Suitable_For', 'Power_Supply', 'Battery_Cell', 'MS_Office', 'Processor_Brand', 'Processor_Name', 'SSD', 'SSD_Capacity', 'RAM', 'RAM_Type', 'Processor_Variant', 'Clock_Speed', 'Graphic_Processor', 'Storage_Type', 'Operating_System', 'USB_Port', 'HDMI_Port', 'Touchscreen', 'Screen_Size', 'Screen_Resolution', 'Screen_Type', 'Speakers', 'Internal_Mic', 'Wireless_LAN', 'Bluetooth', 'Dimensions', 'Weight', 'Disk_Drive', 'Web_Camera', 'Keyboard', 'Backlit_Keyboard', 'Warranty_Summary', 'Warranty_Service_Type', 'Covered_in_Warranty', 'Not_Covered_in_Warranty', 'EMMC_Storage_Capacity', 'Battery_Backup', 'Number_of_Cores', 'Mic_In', 'Sound_Properties', 'Pointer_Device', 'Included_Software', 'Additional_Features', 'Domestic_Warranty', 'Expandable_Memory', 'Processor_Generation', 'Finger_Print_Sensor', 'RAM_Frequency', 'Cache', 'Hardware_Interface', 'Refresh_Rate', 'Dedicated_Graphic_Memory_Type', 'Dedicated_Graphic_Memory_Capacity', 'Face_Recognition', 'Memory_Slots', 'Supported_Operating_System', 'RJ11', 'RJ45', 'Laptop_Bag', 'Multi_Card_Slot', 'category_id', 'user_id', 'storage')", 
                    (1,row['cat_id'], row['category'], row['links'], row['title'], row['price'],
                        row['dis_price'], row['description'], row['image_list'], row['Sales Package'], row['Model Number'], 
                        row['Part Number'], row['Model Name'], row['Series'], row['Color'], row['Type'], row['Suitable For'],
                        row['Power Supply'], row['Battery Cell'], row['MS Office Provided'], row['Processor Brand'], row['Processor Name'],
                        row['SSD'], row['SSD Capacity'], row['RAM'], row['RAM Type'], row['Processor Variant'], row['Clock Speed'],
                        row['Graphic Processor'], row['Storage Type'], row['Operating System'], row['USB Port'], row['HDMI Port'], row['Touchscreen'],
                        row['Screen Size'], row['Screen Resolution'], row['Screen Type'], row['Speakers'], row['Internal Mic'], row['Wireless LAN'],
                        row['Bluetooth'], row['Dimensions'], row['Weight'], row['Disk Drive'], row['Web Camera'], row['Keyboard'],
                        row['Backlit Keyboard'], row['Warranty Summary'], row['Warranty Service Type'], row['Covered in Warranty'], row['Not Covered in Warranty'], row['EMMC Storage Capacity'],
                        row['Battery Backup'], row['Number of Cores'], row['Mic In'], row['Sound Properties'], row['Pointer Device'], row['Included Software'],
                        row['Additional Features'], row['Domestic Warranty'], row['Expandable Memory'], row['Processor Generation'], row['Finger Print Sensor'], row['RAM Frequency'],
                        row['Cache'], row['Multi Card Slot'], row['Hardware Interface'], row['Refresh Rate'], row['Dedicated Graphic Memory Type'], row['Dedicated Graphic Memory Capacity'],
                        row['Face Recognition'], row['Memory Slots'], row['Supported Operating System'], row['RJ11'], row['RJ45'], row['Laptop Bag'],  None, None, None, None, None))
                        
conn.commit() 

# Closing the connection 
conn.close()