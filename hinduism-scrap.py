from requests import get
import requests
from bs4 import BeautifulSoup
errors=[]
for i in range(0,56937):

  try:
 

       url = 'https://www.wisdomlib.org/hinduism/book/manusmriti-with-the-commentary-of-medhatithi/d/doc'+str(145371+i)+'.html'
       htmlString = get(url).text
       html = BeautifulSoup(htmlString, 'lxml')
       entries = html.find_all('div', {'class':'chapter-content text_1173'})
       entries2=html.find_all('h1', {'class':'h2'})
       text = [e.get_text() for e in entries]
       text2= [e.get_text() for e in entries2]
       #print text[0]
       #text.append(text2)
       f= open("./Manusmriti/" + str(i+1) + ".utf8","w")
       f.write(text2[0].encode('utf-8'))
       f.write(text[0].encode('utf-8'))
       print("processed page number " + str(i+1))
  except requests.exceptions.ConnectionError:
       errors.append(str(i))
       print("Error at page number " + str(i))

log = open("errors.txt","w")
log.write(",".join(errors))


