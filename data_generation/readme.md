

The code files present in this directory are used initialization of sample fleets and sample input IOT Data generation. 

# Fleet Data initialization
The file **load_fleet_inventory.py** is used to load two sample records into Dyanmo-Db table. Two sample fleet details are available
in the file **fleet_inventory**

# Input Data generation

The file **fleet_iot_data_generation.py** is used to generate sample IOT input data and publish mqtt messages to AWS IOT service.
The file **data_generation_utils.py** supports the previous file with data generation.
