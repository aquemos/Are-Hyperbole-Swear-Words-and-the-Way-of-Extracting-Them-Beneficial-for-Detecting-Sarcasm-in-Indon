import requests
from bs4 import BeautifulSoup

'''
adjective_check function is used to check the class of a word.
this function return list of a word which classified as adjective class
'''

def adjective_check(text):
    adjective_list = [] #a list to collect word with adjective class
    
    for word in text.split():
        #scrap the html of a page
        URL = "http://tesaurus.kemdikbud.go.id/tematis/lema/" + word + "/adjektiva"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        #find div element with class note-notfound. 
        #this element appears when a word is not in the dictionary
        job_elements = soup.find("div", class_="note-notfound")
        content = bool(job_elements)

        if content:
            #if a word is not in the dictionary, continue to check next word in text
            continue
        else:
            #find hyperlink element with class lema-ordinary
            elements = soup.find_all("a", class_="lemma-ordinary")
            adjective_possibility = []
            for element in elements:
                adjective_possibility.append(element.get_text())
            
            
            if word in adjective_possibility: #check if the word is in list of adverb_possibility
                adjective_list.append(word)
            else:
                continue
    return adjective_list

text = 'Nana sangat cantik dan baik'
print(f'List of adjective in the sentence are {adjective_check(text)}')
