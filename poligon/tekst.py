import requests

def policz_znaki(argument):
    liczba_znakow = len(argument)
    return liczba_znakow

link = 'https://zajecia-programowania-xd.pl/kubus_puchatek'
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text

#link_b = link[:20] + '    ' + link[20:]

kubus_text = kubus_text.replace('<p>', '')
kubus_text = kubus_text.replace('</p>', '')

dlugosc_kubusia = len(kubus_text)
wyrazy_kubusia = kubus_text.split()
wyrazy_n = len(wyrazy_kubusia)
#print(kubus_text)
#print(wyrazy_kubusia)
print(dlugosc_kubusia)
print(wyrazy_n)

kubus_n = 0
for s in wyrazy_kubusia:
    if s == 'Kubuś':
        kubus_n += 1
print(kubus_n)

kubu_n = 0
for i, s in enumerate(wyrazy_kubusia):
    if 'Kubuś' in s:
        #print(i, s)
        kubu_n += 1
print(kubu_n)


l = ["a", "b", "c"]
for i, c in enumerate(l):
    print(i, c)
    