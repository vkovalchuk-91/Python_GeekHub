"""
Викорисовуючи requests, заходите на ось цей сайт "https://www.expireddomains.net/deleted-domains/" (з ним будьте
обережні), вибираєте будь-яку на ваш вибір доменну зону і парсите список  доменів - їх там буде десятки тисяч (звичайно
ураховуючи пагінацію). Всі отримані значення зберігти в CSV файл.
"""
import time

import requests
from bs4 import BeautifulSoup
import csv


def scrape_domains(base_url, sleep_time):
    all_domains = []
    next_page_suffix = "/expired-domains"
    page_counter = 1

    while True:
        print(f"Starting processing {page_counter} page")
        url = base_url + next_page_suffix
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        if soup.find('a', class_='next') is None:
            print("Parsing finished")
            break

        next_page_suffix = soup.find('a', class_='next')['href']

        domains = soup.find_all('td', class_='field_domain')
        for domain in domains:
            domain_name = domain.find('a')['title']
            all_domains.append({'Domain': domain_name})
        print(f"Page {page_counter} has been processed")
        page_counter += 1
        time.sleep(sleep_time)

    return all_domains


def save_to_csv(domains, filename='domains.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Domain']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for domain in domains:
            writer.writerow(domain)


if __name__ == "__main__":
    main_url = "https://www.expireddomains.net"
    pause_time = 30

    domains_data = scrape_domains(main_url, pause_time)
    save_to_csv(domains_data)
