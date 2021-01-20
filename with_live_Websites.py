from requests_html import HTML, HTMLSession
import csv

session = HTMLSession()
r = session.get('https://coreyms.com/')


web_links = r.html.links            # this will return a list of all the links from the requested page 
                                    # use (r.html.absoulute_links) for absolute links from the page 
for lnk in web_links:
    print(lnk)


# article = r.html.find('article')

# csv_file = open('csv_scrape.csv','w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Headline','Date','Author','Summary','Youtube Link'])

# for match in article:
#     headline = match.find('.entry-title-link', first=True)
#     date_posted = match.find('.entry-time', first=True)
#     author = match.find('.entry-author-name', first=True)
#     content = match.find('.entry-content p', first=True)
#     try:
#         iframe = match.find('.youtube-player', first=True).attrs
#         vid_src = iframe['src']
#         vid_src = vid_src.split('/')[4]
#         vid_src = vid_src.split('?')[0]
#     except Exception as e:
#         None
        
#     print(headline.text)
#     print(f'{date_posted.text} by {author.text}')
#     print(content.text)
#     yt_link = (f'https://www.youtube.com/watch?v={vid_src}')
#     print(yt_link)
#     print()
    
#     csv_writer.writerow([headline.text,date_posted.text,author.text,content.text,yt_link])

# csv_file.close()