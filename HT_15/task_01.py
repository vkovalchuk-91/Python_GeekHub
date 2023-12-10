"""
Викорисовуючи requests, написати скрипт, який буде приймати на вхід ID категорії із сайту https://www.sears.com і буде
збирати всі товари із цієї категорії, збирати по ним всі можливі дані (бренд, категорія, модель, ціна, рейтинг тощо) і
зберігати їх у CSV файл (наприклад, якщо категорія має ID 12345, то файл буде називатись 12345_products.csv)
Наприклад, категорія https://www.sears.com/tools-tool-storage/b-1025184 має ІД 1025184
"""
import csv
import time

import requests


def get_response_json(cat_id, startIndex, endIndex):
    while True:
        try:
            cookies = {
                '_vuid': '42160fb1-bfda-402d-b47f-9bb6a4820d79',
                'initialTrafficSource': 'utmcsr=(direct)|utmcmd=(none)|utmccn=(not set)',
                '__utmzzses': '1',
                'zipCode': '10101',
                'city': 'New York',
                'state': 'NY',
                '_gid': 'GA1.2.532173224.1702151344',
                'ftr_ncd': '6',
                '_gcl_au': '1.1.1641947292.1702151345',
                'ltkSubscriber-Footer': 'eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9',
                'GSIDNqXoacKY53MN': '02c37fda-9c5f-435f-bcd4-4de3f45251f5',
                'STSID974004': '8eafc35a-949d-46a6-aba2-5ef511771779',
                '_pbjs_userid_consent_data': '3524755945110770',
                'cookie': 'e552e324-f4bb-477b-98a3-c9f3e3bd4b4c',
                '_sharedid': '4762f8c2-2b65-4cb4-afd4-1a34eb2c91a4',
                '_lr_env_src_ats': 'false',
                'cookie_cst': 'zix7LPQsHA%3D%3D',
                '__qca': 'P0-1544990140-1702151346316',
                'irp': '706fb789-ec92-46f2-9a26-09e4318dc487|tDIsQ65bakMSMioVmuaFXRR9Zc5ZhEYqoiNFN%2FdFmxA%3D|G|d4cbe428-aa83-4c92-bf94-b90f648a6dc7|0|NO_SESSION_TOKEN_COOKIE',
                '__gsas': 'ID=6c67883f5aec033d:T=1702151422:RT=1702151422:S=ALNI_MYxVry0wQUAbt1N4ehI867VgYHu8Q',
                '_clck': '16i4eem%7C2%7Cfhf%7C0%7C1438',
                'cto_bundle': 'gqC15F9rcWVNTFB6cWF4Nm55RWFzb09UY3JOTFJwNUdyTkQ4OGtVNGN2ZmlVSm9Pc05ra3N0Ym9pdXFCMEZYZ3BLTHBIQTExVE5nM1NoYmhkOG5Gb3BqQ0VsbzRhVEpZTWFMVCUyRnhZYk91SW1wdm95b3l3dHUlMkJVWkZkOFFYbHU5VW9pNTYxdCUyQmZGS1JSV1VmelFiaWVvMWJBUXclM0QlM0Q',
                'cto_bidid': 'uTRC8V9qYm1ZZlRzQUpFUkFEUnFuanNOOEhGdjUxVWZqRjFESVJKNTVMM2dsU2Y3cSUyRktnemlQNVMySVZzTXc2Qmx3TmNHd05ReDE4Ukh4ODJsbFBod3Y0dkdBZGkzbHo4RlpFaHlPQTIyS1BMZExzJTNE',
                'cto_dna_bundle': 'JW5Io180M0RITmhlJTJCZkMwOUJGQlhaMUN2czNMaCUyRmZEJTJGdHdVNVBrRm9iNFprcTM0a1ZZU1hVVHJyYklMTk5NazM0bDBK',
                '__cf_bm': 'AJ7Z8bY.AVtnbzy.6BMaMTFbfQ0KpmtKkglc4hPT2ss-1702196489-0-AYKDE5mbMpV0MJxnqaKkUNRy8gLj8QEctaX+gQRHXTHz7DCdgffjl0jCsiSoDNn3Qeow/dDzK9DPmujcAE0THfY0d9PgEy3geDdLE4cvRYgj',
                'cf_clearance': 'A9njIfbO7fefiFzt1bZQP1tRkD0OhGB4dlIvt09grX0-1702196490-0-1-2d82e503.2c0434e7.7a83bae3-0.2.1702196490',
                'ftr_blst_1h': '1702196491081',
                'ltkpopup-session-depth': '5-2',
                'OptanonAlertBoxClosed': '2023-12-10T08:22:17.897Z',
                'OptanonConsent': 'isIABGlobal=false&datestamp=Sun+Dec+10+2023+10%3A22%3A18+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202209.1.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CSPD_BG%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=UA%3B30',
                'forterToken': '5f6319577beb46cc822c22b75a62f7f9_1702196531159_846_UDF43-m4_13ck',
                '_ga': 'GA1.1.316813637.1702151344',
                '_ga_L7QE48HF7H': 'GS1.1.1702196491.3.1.1702196547.4.0.0',
                '_uetsid': '02a5ae0096cc11ee8157bb3ba7340b84',
                '_uetvid': '02a5f22096cc11eea2be41b84ea5ae80',
                '__attentive_id': '5c6155fe6a494dc3b1a270e2ecefce89',
                '_attn_': 'eyJ1Ijoie1wiY29cIjoxNzAyMTk2NTUxODc0LFwidW9cIjoxNzAyMTk2NTUxODc0LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjVjNjE1NWZlNmE0OTRkYzNiMWEyNzBlMmVjZWZjZTg5XCJ9In0=',
                '__attentive_cco': '1702196551878',
                '_clsk': '1itj5r3%7C1702196551936%7C2%7C1%7Co.clarity.ms%2Fcollect',
                '__attentive_pv': '1',
                '__attentive_ss_referrer': 'ORGANIC',
                '__attentive_dv': '1',
            }

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
                'Authorization': 'SEARS',
            }

            response = requests.get(
                f'https://www.sears.com/api/sal/v3/products/search?'
                f'startIndex={startIndex}'
                f'&endIndex={endIndex}'
                f'&storeId=10153'
                f'&catGroupId={cat_id}',
                cookies=cookies,
                headers=headers,
            )
            return response.json()
        except Exception:
            print(f"Забагато запитів! Додаткові 70 секунд очікування для повторного запиту")
            time.sleep(70)


def save_to_csv(cat_id, prods):
    filename = str(cat_id) + "_products.csv"
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'brandName', 'regularPrice', 'finalPrice']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for product in prods:
            writer.writerow(product)


while True:
    category_id_str = input("Введіть ID категорії для парсингу товарів: ")
    try:
        category_id = int(category_id_str)
        if category_id > 0:
            break
        print("ID категорії може складатися тільки з цифр та бути більше 0, повторіть спробу!")
    except ValueError:
        print("ID категорії може складатися тільки з цифр та бути більше 0, повторіть спробу!")
startIndex = 1
offset = 48
endIndex = offset
request_counter = 0
while True:
    response_json = get_response_json(category_id, startIndex, endIndex)
    products = []
    try:
        for item in response_json['items']:
            products.append({'name': item['name'], 'brandName': item['brandName'],
                             'regularPrice': item['price']['regularPrice'], 'finalPrice': item['price']['finalPrice']})
        save_to_csv(category_id, products)
    except KeyError:
        if len(products) == 0 and request_counter == 0:
            print(f"Для категорії '{category_id}' товарів не існує")
        print(f"Парсинг закінчено!")
        break

    request_counter += 1
    print(f"Успішний {request_counter} запит. Оброблено дані {startIndex=}, {endIndex=}")
    startIndex += offset
    endIndex += offset
