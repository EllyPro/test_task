# step 1
import requests, bs4, time
import pandas as pd
urls = ['https://kun.uz/uz/news/2022/11/30/parda-ortidagi-xususiylashtirish-yirik-aktivlar-qanday-qilib-ofshor-kompaniyalarga-otib-ketmoqda',
       'https://kun.uz/uz/news/2022/12/02/termizda-afgoniston-iqtisodiyotiga-mutaxassislar-tayyorlash-uchun-talim-klasteri-tashkil-etiladi',
        'https://kun.uz/uz/news/2022/12/02/dunyoning-eng-qimmat-shaharlari-reytingi-elon-qilindi-toshkent-eng-arzon-shaharlar-beshtaligida'
        ]

access_times = []
contents = []
for url in urls:
    req = requests.get(url)

    req.raise_for_status()

    soup = bs4.BeautifulSoup(req.text, 'html.parser')

    p_tags = soup.select('p')

    res = ''
    for p in p_tags:
        res += str(p.text)

    access_datetime = time.asctime(time.localtime(time.time()))

    access_times.append(access_datetime)

    contents.append(res)

details = {
    'source_url': urls,
    'access_datetime': access_times,
    'content': contents
}

df = pd.DataFrame(details)
print(df)

# Step 2
df['word'] = df['content'].str.split(' ')

df.to_csv('res.csv')
# step 3