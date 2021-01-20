from bs4 import BeautifulSoup 
import requests
import csv

source  = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source,'lxml')

f =  open('web_scr.csv','wt') 
csv_wtr = csv.writer(f)
csv_wtr.writerow(['Title','Discription','Video Link'])

for article in soup.find_all('article'):

    try:
        header = article.h2.a.text
    except Exception as e :
        header = None

    print(header)
    print()

    for main in soup.find_all('main') :
        try :
            body = main.div.p.text
        except Exception as e :
            body = None
        print(body)
        print()

        try :
            link = main.div.span.iframe
            link = str(link)
            link_list = (link.split('"'))
            link_split1 = (link_list[9]).split('/')
            link_split2 = (link_split1[4]).split('?')
            main_ID_link = link_split2[0]
        except Exception as e :
            link = None
            link_list = None
            link_split1 = None
            link_split2 = None
            main_ID_link =None
            
        yt_link = f'https://youtube.com/watch?v={main_ID_link}'
        print(yt_link)
        print()
        print()
        print()
        print()

        csv_wtr.writerow([header,body,yt_link])

f.close()


#------------>>>>>>>> DIFFERENT WAYS TO DO IT

# # print(soup.prettify())
# article = soup.find('article')
# main = soup.find('main')


# print(article.prettify())

# link_ext = article.find('iframe',class_='youtube-player')['src']
# link_b1 = (link_ext.split('/'))

# link_b2 = link_b1[4]

# link_b3 = link_b2.split('?')
# main_Video_id = link_b3[0]
# # print(main_id)

# yt_link = f'https://youtube.com/watch?v={main_Video_id}'
# # print(yt_link)