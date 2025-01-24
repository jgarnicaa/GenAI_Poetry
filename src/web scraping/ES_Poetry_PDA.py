# ------ File did to scrape www.poemas-del-alma.com -----------

### In this page we have authors and each one has different poems. So the first step is get all the autors list.

import requests
import bs4
import pandas as pd
import csv

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

    return results

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
    poems_content=[]
    poems_titles=[]
    for poem_url in poems_url:
        
        poem_url='https://www.poemas-del-alma.com/'+poem_url

        print(poem_url)
        r = requests.get(poem_url)
        soup=bs4.BeautifulSoup(r.text, features="html.parser")
        poem_title=soup.find("h1", class_="title-poem").get_text()
        poem_content=soup.find("p").get_text(separator='\n')
        poems_content.append(poem_content)
        poems_titles.append(poem_title)
        
    results.append(poems_titles)
    results.append(poems_content)

    return results


def get_dataset(name, titles, poem):

    
    df = pd.DataFrame({
        "Title": titles,
        "Poem": poem,
        "Author": name

    })

    return df



def main():
    abc=['a', 'b', 'c', 'd', 'e', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    authors = [author for lettre in abc for author in get_authors(lettre)]

    with open("PoemasDelAlmaDataset.csv", 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames= ["Title", "Poem", "Author"]
        writer=csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for author in authors:
            link_author, name_author = author
            poems_url = get_link_poems(link_author)
            titles_poem, content_poems = get_poems(poems_url)
            for i in range(len(titles_poem)):
                writer.writerow({'Title':titles_poem[i], 
                                 'Poem':content_poems[i], 
                                 "Author":name_author})
        #dataset_temp=get_dataset(name_author,titles_poem,content_poems)
    print("Done")
        #dataset = pd.concat([dataset, dataset_temp], ignore_index=True)

    #print(dataset)


if __name__== "__main__":
    main()