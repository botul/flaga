import requests
import sys

#orangutan = 'https://zajecia-programowania-xd.pl/flagi'

def pobierz_strone( orangutan):    
    surowe_info = requests.get( orangutan)
    text = surowe_info.text
    return text

def stworz_liste_flag( orangutan):
    text_strony_www = pobierz_strone( orangutan)
    lista_linii = text.split('</p>')
    linki = []
    for linia in lista_linii:

        link = linia.replace('<p>', '')
        link = link.replace('- ', '')
        link = link.strip()
        if ' ' in link or '<' in link:
            continue
        linki.append( link)
    
    return linki

if __name__ == '__main__':
    args = sys.argv[1]
    lista_flag = stworz_liste_flag(args)
#    print(lista_flag)
