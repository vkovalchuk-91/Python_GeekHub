"""
http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи: цитата, автор, інфа
про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл
"""
import requests
from bs4 import BeautifulSoup
import csv


def scrape_quotes(base_url, num_pages):
    all_quotes = []
    next_page_suffix = ""

    for page in range(1, num_pages + 1):
        print(f"Starting processing {page} page")
        url = base_url + next_page_suffix
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        if page != num_pages:
            next_page_suffix = soup.find('li', class_='next').find('a')['href']

        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            text = quote.find('span', class_='text').text[1:-1]
            author = quote.find('small', class_='author').text
            if author in authors.keys():
                born_date, born_location, description = get_authors_data_from_dictionary(author)
            else:
                born_date, born_location, description = get_authors_data_from_request(base_url, quote)
                authors[author] = {'Author-born-date': born_date, 'Author-born-location': born_location,
                                   'Author-description': description}

            all_quotes.append({'Text': text, 'Author-name': author, 'Author-born-date': born_date,
                               'Author-born-location': born_location, 'Author-description': description})
        print(f"Page {page} has been processed")

    return all_quotes


def get_authors_data_from_request(base_url, quote):
    author_info_url = base_url + quote.find('a')['href']
    author_response = requests.get(author_info_url)
    author_soup = BeautifulSoup(author_response.text, 'lxml')

    born_date = author_soup.find('span', class_='author-born-date').text.strip()
    born_location = author_soup.find('span', class_='author-born-location').text.strip()
    description = author_soup.find('div', class_='author-description').text.strip()
    return born_date, born_location, description


def get_authors_data_from_dictionary(author):
    born_date = authors[author]["Author-born-date"]
    born_location = authors[author]["Author-born-location"]
    description = authors[author]["Author-description"]
    return born_date, born_location, description


def save_to_csv(quotes, filename='quotes.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Text', 'Author-name', 'Author-born-date', 'Author-born-location', 'Author-description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for quote in quotes:
            writer.writerow(quote)


if __name__ == "__main__":
    main_url = "http://quotes.toscrape.com"
    pages_number = 10
    authors = {}

    quotes_data = scrape_quotes(main_url, pages_number)
    save_to_csv(quotes_data)
