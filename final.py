from bs4 import BeautifulSoup
import requests

source = requests.get('http://webcrawler.ml').text

soup = BeautifulSoup(source, 'lxml')

title = soup.find('div',class_='col-sm-9')
headline = title.h2.text
print(headline)

print()

para = title.p.text
print(para)

print()

for sec_head in soup.find_all('div',class_='section-header'):

    head_line = sec_head.h2.text
    print(head_line)
    parag = sec_head.p.text
    print(parag)
    print()
    if head_line=='OUR Features':
        for download in soup.find_all('div',class_='media service-box wow fadeInRight'):
            head = download.h4.text
            print(head)
            paragraph = download.p.text
            print(paragraph)

            print()

    elif head_line == 'Service':
        for media_heading in soup.find_all('div',class_='media service-box'):
            media = media_heading.h4.text
            print(media)
            paragrap = media_heading.p.text
            print(paragrap)
            print()


    elif head_line == 'About Us':
        for web_crawler in soup.find_all('div',class_='col-sm-6 wow fadeInRight'):
            web = web_crawler.h3.text
            print(web)
            pragraph = web_crawler.p.text
            print(pragraph)
            print()
        

    elif head_line == 'OUR TEAM':
        for about in soup.find_all('div',class_='team-info'):
            abou = about.h3.text
            print(abou)
            par = about.p.text
            print(par)
            print()
            
            
#for link in soup.find_all('a'):
  #  print(link.get('href'))

#print(soup.prettify())















         
