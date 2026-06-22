"""
The program reads data from an XML file and displays the total cost of all goods.
"""

import xml.etree.ElementTree as ET


# Calculates the total of all purchases
def parse_xml(xml_str):
    root = ET.fromstring(xml_str)
    price_list = []

    for product in root.findall('product'):
        price = float(product.find('price').text)
        price_list.append(price)
    total_price = sum(price_list)
    return print(f'Total cost of all products: {total_price}')


# Reads the file and calls the "parse_xml" function
def read_xml(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        return parse_xml(content)


read_xml('products.xml')
