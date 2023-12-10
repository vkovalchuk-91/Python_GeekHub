import logging
import scrapy
import csv
from bs4 import BeautifulSoup


class ExtensionsParser:
    @staticmethod
    def parse_location_page(response):
        soup = BeautifulSoup(response.text, 'lxml')
        locations_data = soup.find_all('loc')
        return [location.text.strip() for location in locations_data]

    @staticmethod
    def parse_extensions_page(response):
        soup = BeautifulSoup(response.text, 'lxml')
        links_data = soup.find_all('loc')
        return [link_data.text.strip() for link_data in links_data]

    @staticmethod
    def parse_extension_details(response):
        soup = BeautifulSoup(response.text, 'lxml')
        extension_id = response.url.split('/')[-1]
        name = soup.find('h1').text
        descr0 = soup.find('div', class_='C-b-p-j-Pb').text
        descr1 = soup.find('pre', class_='C-b-p-j-Oa').text
        description = f"{descr0}\n{descr1}" if descr0 and descr1 else descr0 or descr1

        return {'Extension ID': extension_id, 'Extension Name': name, 'Description': description}


class ExtensionsSpider(scrapy.Spider):
    name = 'chrome_webstore'
    start_urls = ['https://chrome.google.com/webstore/sitemap']

    def parse(self, response, **kwargs):
        locations = ExtensionsParser.parse_location_page(response)
        self.log(f"Processed {len(locations)} locations", logging.INFO)
        location_counter = 1

        for location in locations:
            yield scrapy.Request(url=location, callback=self.parse_extensions_page)
            self.log(f"Links from location {location_counter} in process", logging.INFO)
            location_counter += 1

    def parse_extensions_page(self, response):
        extensions_links = ExtensionsParser.parse_extensions_page(response)
        for extension_link in extensions_links:
            yield scrapy.Request(url=extension_link, callback=self.parse_extension_details)
            self.log(f"Extension details {extension_link} in process", logging.INFO)

    def parse_extension_details(self, response):
        extension_details = ExtensionsParser.parse_extension_details(response)
        self.save_to_csv(extension_details)
        self.log(f"{extension_details['Extension Name']} details saved", logging.INFO)

    @staticmethod
    def save_to_csv(extension_info, filename='results/extensions.csv'):
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Extension ID', 'Extension Name', 'Description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(extension_info)
