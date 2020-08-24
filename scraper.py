from bs4 import BeautifulSoup
import requests
import os
import sqlite3
from sqlite3 import Error


def main(tier):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "phone.db")

    try:
        connection = sqlite3.connect(db_path)
    except Error as e:
        print(e)

    db = connection.cursor()

    def remove(string):
        return string.replace(" ", "")

    if tier != 'best':
        source = requests.get(
            'https://www.91mobiles.com/top-10-mobiles-below-'+tier+'-in-india').text

    else:
        source = requests.get(
            'https://www.91mobiles.com/top-10-mobiles-in-india').text

    soup = BeautifulSoup(source, 'lxml')

    all_phone = soup.find_all("span", class_="a2 star star_width")

    phones = []
    prices = []

    for phone in all_phone:
        phones.append(phone.h3.get_text())

    all_price = soup.find_all(
        "span", class_=["price price_padding", "price price_float"])
    for price in all_price:
        prices.append((price.get_text()))

    per = []
    dis = []
    cam = []
    bat = []
    frocam = []
    ram = []
    counter = 1

    big_section = soup.find_all("li", class_="left")
    for item in big_section:
        my_property = (item.contents[0].strip())
        all_item = item.find("div", class_="a")
        if my_property == "Performance":
            per.append(all_item.contents[2].get_text())
            ram.append(all_item.contents[4].get_text())

        # elif my_property == "Display":
        #     for pro in all_item:
        #         dis.append(pro.get_text())

        elif my_property == "Camera":
            cam.append(all_item.contents[0].get_text())
            frocam.append(all_item.contents[4].get_text())

        elif my_property == "Battery":
            bat.append(all_item.contents[0].get_text())

    storage = []
    all_storage = soup.find_all("div", class_="finder_icon_storage_text")
    for item in all_storage:
        storage.append(item.get_text())

    info = []

    all_info = soup.find_all("div", class_="exp_comnt_pnl")

    for item in all_info:
        info.append(item.p.contents[1].strip())

    images = []

    allimg = soup.find_all("img", class_="finder_pro_image fimage gaclick")
    for item in allimg:
        if item.has_attr('src'):
            imgid = item['src']
        elif item.has_attr('data-src'):
            imgid = item['data-src']
        images.append(imgid)

    for item in range(len(phones)):
        db.execute("""INSERT INTO PHONES (name, price, camera, front_cam, processor, storage, ram, battery, discription, image, tier)
        VALUES ("{0}","{1}","{2}","{3}","{4}","{5}",
                "{6}","{7}","{8}","{9}","{10}")
        ON CONFLICT(name) DO UPDATE SET
        name= "{0}",
        price= "{1}",
        camera= "{2}",
        front_cam= "{3}",
        processor= "{4}",
        storage= "{5}",
        ram= "{6}",
        battery= "{7}",
        discription= "{8}",
        image = "{9}",
        tier= "{10}"
        """.format(phones[item], prices[item], cam[item], frocam[item], per[item], storage[item], ram[item], bat[item], info[item], images[item], tier))

    connection.commit()
    connection.close()


all_the_choices = ['5000', '8000', '10000', '12000',
                   '15000', '20000', '25000', '30000', 'best']

if __name__ == '__main__':
    for choice in all_the_choices:
        print(f"Extracting phones of price/tier: {choice}")
        main(choice)
