from requests_html import HTML

with open(r'C:\Users\shiva\OneDrive\Desktop\prac\01 corey schafer\web scraping with requests-html\sample.html') as html_file:
    source = html_file.read()
    html_source = HTML(html=source) 
    html_source.render()            # there are sometime some dynamic data generated, so it can only be captured by rendering the page, as in the sample.html there is a java script
                                    # running which is generating some text and it can only be scraped when the page is rendered and this feature is available in this library. 

# print(html_source)                # this will give url
# print(html_source.html)           # this will give html code
# print(html_source.text)           # this will give text in the code

# matches = html_source.find('div')    # we can find anything like title, div, h1, etc. and it will generate a list of items matched
#                                      # or use first = True for no list, it will just find the first occurence

# matches = html_source.find('#footer', first=True)  # this will give id = footer
# print(matches.html)

# matches = html_source.find('div.article')
# headline = html_source.find('h2')

# for head in headline:
#     print(head.text)

# for match in matches:
#     print(match.text)               # .html can also be used for code
#     print()




matches = html_source.find('div.article')
for match in matches:
    headline = match.find('h2', first=True).text
    summary = match.find('p', first=True).text
    print(headline)
    print(summary)
    print()


# DIFFERENCE BETWEEN SYNCHRONUS AND ASYNCHRONUS REQUESTS
# for synchronus requests the next request is only sent when the previous one gets completed, so in this if 3 requests are made with delay of 3 seconds, then it will take total of
# 9 secs as 3+3+3, but in case of asynchrnous requests, each requests are sent without waiting for delay so it will only take upto 3 seconds to complete.