import requests
from contextlib import closing
import csv

# STEP 1: 
url = "https://storage.googleapis.com/dqlab-dataset/harga_rumah.txt"
data_harga_rumah = []
with closing(requests.get(url, stream=True)) as r:
    f = (line.decode('utf-8') for line in r.iter_lines())
    data_harga_rumah = [row for row in csv.reader(f)]

key_harga_rumah = data_harga_rumah[0]
harga_rumah = []
for baris_harga_rumah in data_harga_rumah[1:]:
    dict_harga_rumah = dict()
    for i in range(len(baris_harga_rumah)):
        dict_harga_rumah[key_harga_rumah[i]] = baris_harga_rumah[i]
    harga_rumah.append(dict_harga_rumah)

print(harga_rumah)

# STEP 2:
def get_all_specified_attributes(list_of_dictionary, specified_key):
    list_attributes = []
    for data in list_of_dictionary:
        attribute = data[specified_key]
        list_attributes.append(attribute)
    return list_attributes

# STEP 3:
def min_value(list_attributes):
    min_attribute = 9999
    for attr in list_attributes:
        if int(attr) < min_attribute:
            min_attribute = int(attr)
    return min_attribute

def max_value(list_attributes):
    max_attribute = -9999
    for attr in list_attributes:
        if int(attr) > max_attribute:
            max_attribute = int(attr)
    return max_attribute

# STEP 4:
def transform_attribute(attr, max_attr, min_attr):
    nilai_transformasi = (attr - min_attr) / (max_attr - min_attr)
    return nilai_transformasi

# STEP 5:
def data_transformation(list_of_dictionary, list_attribute_names):
    attr_info = {}
    for attr_name in list_attribute_names:
        specified_attributes = get_all_specified_attributes(list_of_dictionary, attr_name)
        max_attr = max_value(specified_attributes)
        min_attr = min_value(specified_attributes)
        attr_info[attr_name] = {'max': max_attr, 'min': min_attr}
        data_idx = 0
        while data_idx < len(list_of_dictionary):
            list_of_dictionary[data_idx][attr_name] = transform_attribute(
                int(list_of_dictionary[data_idx][attr_name]),
                max_attr,
                min_attr
            )
            data_idx += 1
    return list_of_dictionary, attr_info

# STEP 6 (diperbaiki):
def transform_data(data, attr_info):
    for key_name in data.keys():
        data[key_name] = (data[key_name] - attr_info[key_name]['min']) / (
            attr_info[key_name]['max'] - attr_info[key_name]['min'])
    return data

# STEP 7:
def abs_value(value):
    if value < 0:
        return -value
    else:
        return value

def price_based_on_similarity(data, list_of_data):
    prediksi_harga = 0
    perbedaan_terkecil = 999
    for data_point in list_of_data:
        perbedaan = abs_value(data['tanah'] - data_point['tanah'])
        perbedaan += abs_value(data['bangunan'] - data_point['bangunan'])
        perbedaan += abs_value(data['jarak_ke_pusat'] - data_point['jarak_ke_pusat'])
        if perbedaan < perbedaan_terkecil:
            prediksi_harga = data_point['harga']
            perbedaan_terkecil = perbedaan
    return prediksi_harga

# STEP 8:
harga_rumah, attr_info = data_transformation(
    harga_rumah,
    ['tanah', 'bangunan', 'jarak_ke_pusat']
)

data = {'tanah': 110, 'bangunan': 80, 'jarak_ke_pusat': 35}
data = transform_data(data, attr_info)

harga = price_based_on_similarity(data, harga_rumah)
print("Prediksi harga rumah: ", harga)
