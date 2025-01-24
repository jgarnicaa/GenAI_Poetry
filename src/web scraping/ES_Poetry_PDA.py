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
    ## ARREGLAR FUNCION
    for label in content:
        if (label["href"].endswith('htm')) and ("poemas" not in label["href"]): # Only poems URL has https and .htm in their URL
           results.append(label['href'])
    return results


def get_poems(poems_url): ## A list full of poems links, it's necessary complete links

    results=[]
    for poem_url in poems_url:
        
        poem_url='https://www.poemas-del-alma.com/'+poem_url
        r = requests.get(poem_url)
        soup=bs4.BeautifulSoup(r.text, features="html.parser")
        poem_title=soup.find("h1").get_text()
        poem_content=soup.find("p").get_text(separator='\n')
        results.append((poem_title, poem_content))

    return results


def main():
    authors=get_authors('a')
    link_author, name_author = authors[6]
    print("Author's name: ", name_author)
    poems_url = get_link_poems(link_author)
    poems = get_poems(poems_url)
    print(poems)

if __name__== "__main__":
    main()