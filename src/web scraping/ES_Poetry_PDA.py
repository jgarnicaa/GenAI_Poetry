# ------ File did to scrape www.poemas-del-alma.com -----------

### In this page we have authors and each one has different poems. So the first step is get all the autors list.

import requests
import bs4

## make a list of tuples between all authors and their links to access
def get_authors(char_init): ## char_init = initial char of author's name

    url = 'https://www.poemas-del-alma.com/{char}.html'.format(char=char_init)
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, features="html.parser")

    results=[]
    content=soup.find_all("a", href=True) #Find all names with associated links

    for label in content:
       if url[:-5] in label['href']: # Take only URL that match with inital char of author
           results.append((label['href'], label.text))

    return (results)

def get_link_poems(author_url):

    r = requests.get(author_url)
    soup = bs4.BeautifulSoup(r.text, features="html.parser")

    results=[]
    content=soup.find_all("a", href=True) #Find all names with associated links
    print(content)


    ## ARREGLAR FUNCION
    for label in content:
        if (label["href"].endswith('htm')) and (label["href"].startswith("https:")): # Only poems URL has https and .htm in their URL
           results.append((label['href'], label.text))
    return results
    


def main():
    authors=get_authors('a')
    link, name = authors[10]
    print("Author's name: ", name) ## <a href="abu-l-qasim-ben-al-saqqat-fiesta-en-un-jardin.htm">Fiesta en un jardín
    html=get_link_poems(link)
    print(html)

if __name__== "__main__":
    main()