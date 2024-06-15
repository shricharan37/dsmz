import os
import requests
from bs4 import BeautifulSoup
import codecs

directory_path = r'C:\Users\shric\Desktop\dsmz_bacteria_2'

if not os.path.exists(directory_path):
    os.makedirs(directory_path)

base_url = "https://www.dsmz.de/collection/catalogue"

total_products = 70884

for i in range(70001, total_products + 1):
    product_url = "{}/details/culture/DSM-{}".format(base_url, i)
    
    try:
        response = requests.get(product_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        
        name_tag = soup.find('h1')
        name = name_tag.get_text(strip=True) if name_tag else "Unknown_bacteria_{}".format(i)
        
        info_dict = {'Name': name}

        info_section = soup.find('div', {'class': 'properties'})
        
        if info_section:
            rows = info_section.find_all('div', {'class': 'field'})
            for row in rows:
                label_tag = row.find('div', {'class': 'label'})
                value_tag = row.find('div', {'class': 'value'})
                
                if label_tag and value_tag:
                    hidden_keywords_span = value_tag.find('span', {'class': 'hidden-keywords'})

                    if hidden_keywords_span:
                        hidden_keywords_span.decompose()

                    label = label_tag.get_text(separator=" ",strip=True).replace(':', '')
                    value = value_tag.get_text(separator=" ",strip=True)
                    info_dict[label] = value
        
        labels = [
            'Name', 'DSM No.', 'Strain designation', 'Other collection no. or WDCM no.',
            'Isolated from', 'Country', 'Date of sampling', 'Nagoya Protocol Restrictions',
            'History', 'Genbank accession numbers', 'Cultivation conditions',
            'Summary and additional information', 'Literature', 'Risk group', 'Supplied as'
        ]
        
        if name != "Results for „”":
            file_path = os.path.join(directory_path, "DSM-{}.txt".format(i))
            with codecs.open(file_path, 'w', 'utf-8') as file:
                for label in labels:
                    label_unicode = label if isinstance(label, str) else label.decode('utf-8')
                    value_unicode = info_dict.get(label, 'Not found' if label != 'Name' else name)
                    value_unicode = value_unicode if isinstance(value_unicode, str) else value_unicode.decode('utf-8')
                    file.write(u"{}\t {}\n".format(label_unicode, value_unicode))

                print("Saved: {}".format(file_path))
        else:
            print("DSM-{}: No name found".format(i))

    except requests.HTTPError as http_err:
        print("HTTP error occurred for DSM-{}: {}".format(i, http_err))
    except Exception as err:
        print("An error occurred for DSM-{}: {}".format(i, err))
