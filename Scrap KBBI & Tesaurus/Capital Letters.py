import requests
from bs4 import BeautifulSoup

'''
acronym_check function is used to check is the word is an acronym.
this function return list of a word which not an acronym but written in uppercase
'''

def check_acronym(text):
    capital_letter = [] #a list to collect upper case word and not an acronym

    for word in text.split():
        #check if a word is written in uppercase
        if word.isupper():
            URL = "https://kbbi.kemdikbud.go.id/entri/" + word
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")

            #find span element with class glyphicon glyphicon-alert text-danger. 
            #this element appears when a word is not in the dictionary
            job_elements = soup.find_all('span', class_ = "glyphicon glyphicon-alert text-danger")
            content = bool(job_elements)

            if content:
                continue
            else:
                class_word = []
                job_elements = soup.find_all('span')

                for element in job_elements:
                    #get attribute of each element
                    class_word.append(element.get('title', 'No title attribute'))

                if 'singkatan' in class_word: #check if an acronym attribut is in class_word
                    #if a word is an acronym, continue to check next word in the text
                    continue
                else:
                    #if acronym is not in class word, append the word into capital_letter list
                    capital_letter.append(word)

        else: #if word is not written in uppercase, continue to check next word in the text
            continue
    
    return capital_letter

text = "BLT yang kami dapatkan KURANG"
print(f'Word written in capital letters are {check_acronym(text)}')
