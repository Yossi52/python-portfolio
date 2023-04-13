from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

yes24_url = "http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=09&PageNumber="

best_seller = pd.DataFrame({
    "제목": [],
    "저자": [],
    "출판사": [],
    "출판일": [],
    "정가": []
})

for i in range(1, 16):
    response = requests.get(yes24_url+str(i))
    soup = BeautifulSoup(response.text, "html.parser")

    titles = [data.text for data in soup.select(selector=".goodsTxtInfo>p>a")
              if data.text != "" and re.match("[0-9]{1,4}개", data.text) is None]
    pu_data = soup.select(selector=".aupu")
    authors = []
    publishers = []
    pub_date = []
    for data in pu_data:
        info = data.text.split("|")
        authors.append(info[0].strip())
        publishers.append(info[1].strip())
        pub_date.append((info[2].strip()))

    price_data = soup.select(selector=".goodsTxtInfo")
    price = []
    for data in price_data:
        price.append(int(data.select_one(selector="p:nth-child(3)").text.split(" ")[0].replace(",", "").replace("원", "")))

    df = pd.DataFrame({
        "제목": titles,
        "저자": authors,
        "출판사": publishers,
        "출판일": pub_date,
        "정가": price
    })

    best_seller = pd.concat([best_seller, df], ignore_index=True)

best_seller.to_csv("2023년_4월_베스트_셀러_300.csv")
