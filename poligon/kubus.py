import requests

link = 'https://zajecia-programowania-xd.pl/kubus_puchatek'
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text
kubus_linie_b = kubus_text.split('</p>')

#czyszczenie
kubus_linie = []
for l in kubus_linie_b:
	l = l.replace('<p>', '')
	kubus_linie.append(l)

#wyswietlanie

koszyk = ['jablko', 'maliny', 'mango', 'agrest']

tajemniczy_bohater = 'Cyber Przemo'
tajemniczy_bohater2 = 'dot MS'

start = 200
end = 220
for index, linia in enumerate(kubus_linie):
    if index >= start and index < end:
        linia = linia.replace('Kubuś', tajemniczy_bohater)
        linia = linia.replace('Puchatek', tajemniczy_bohater)
        linia = linia.replace('Królik', tajemniczy_bohater2)
        print(linia)
print()
print('Czytała Krystyna Czubówna')
print()
