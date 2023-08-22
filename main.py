import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
import csv

### can be modified to work in different ways


url = "https://pak-man.com/12-oz-fiber-bowls.html" # MAIN URL goes here

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.find(class_='mainbox-title').text.strip() if soup.find(class_='mainbox-title') else "Title not found" #title class here
    
    short_description1_element = soup.find(class_='product-list-field') # product desc here
    if short_description1_element:
        label = short_description1_element.find('label').text.strip() if short_description1_element.find('label') else "Label not found"
        span = short_description1_element.find('span').text.strip() if short_description1_element.find('span') else "Span not found"
        short_description1 = f"{label}: {span}"
    else:
        short_description1 = "Short description 1 not found"
    print(short_description1)
    
    description1_element = soup.find(id='content_description') # description class here
    if description1_element:
        description1 = '\n'.join(p.get_text(strip=True) for p in description1_element.find_all('p'))
    else:
        description1 = "Description 1 not found"
    
    description2_element = soup.find(id='content_description') #same description class here
    if description2_element:
        ul_element = description2_element.find('ul')
        if ul_element:
            description2 = '\n'.join(li.get_text(strip=True) for li in ul_element.find_all('li'))
        else:
            description2 = "Description 2 list not found"
    else:
        description2 = "Description 2 not found"
    
    description1 = description1.replace("�", " ")
    all_description = description1 + "\n \n" + description2
    
    # category check 
    # soup = BeautifulSoup(response, 'html.parser') # enable category check here

    breadcrumbs_div = soup.find('div', class_='breadcrumbs')

    if breadcrumbs_div:
        a_elements = breadcrumbs_div.find_all('a')

        if len(a_elements) >= 4:
            third_a_text = a_elements[2].get_text(strip=True)
            fourth_a_text = a_elements[3].get_text(strip=True)
        
        category_first = third_a_text
        category_second = third_a_text  + " > " + fourth_a_text
        main_category = category_first + ", " + category_second

        print(main_category)

    else:
        print("Breadcrumbs div not found on the page.")





    image_element = soup.find(class_='cm-image-previewer') # image class goes here
    image_link = image_element['href'] if image_element and 'href' in image_element.attrs else "Image link not found"
    
    image_filename = os.path.basename(urlparse(image_link).path)
    image_path = os.path.join("images", image_filename)
    
    
    link_to_upload = "http://aswtgroup.com/theboxshed.com/wp-content/uploads/2023/08/" + image_filename #for wordpress images location / can be changed to custom
    print(link_to_upload)


    image_response = requests.get(image_link)
    if image_response.status_code == 200:
        with open(image_path, "wb") as image_file:
            image_file.write(image_response.content)
        print("Image saved:", image_path)
    else:
        print("Failed to download the image")


    price_element = soup.find(Class_= 'price-num') # sale price class goes here
    price = price_element.text.strip() if price_element else "Sale Price not found"


    price_span = soup.find(class_='price') #real price class
    if price_span:
        price_text = price_span.get_text(strip=True)
    else:
        price_text = "Price span not found"
    
    price_text = price_text.replace("$", "") # replacing symbol with price 
    price_new = float(price_text)
    updated_prices = price_new + (price_new * 0.25)

    csv_file_path = "data.csv"
    csv_exists = os.path.exists(csv_file_path)
    with open(csv_file_path, mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        if not csv_exists:
            csv_writer.writerow(['Name', 'Short description', 'Description', 'Sale price', 'Regular price', 'Images','Categories'])
        csv_writer.writerow([title, '', all_description, '', updated_prices, link_to_upload, main_category])# update it according to need
    
    print("Added Data to csv file") #completed 


else:
    print("Failed to retrieve the webpage")

