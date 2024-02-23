"""profesie= 'traducator'
print(profesie)

NUME='Simona'
DATA_NASTERII='24.09.1994'
DATA_CURS= '23.11.2023'
procent_invatare='70%'
print(type(procent_invatare))
print("-----"*10)
sunt_pregatit_de_examen= False
print('Numele meu este '+ NUME + ' si sunt ' +profesie+'.'+'Sunt nascuta pe '+ DATA_NASTERII)
print(f'Am inceput un curs de testare automata pe data de {DATA_CURS}, procentul de invatare pentru cursul anterior fiind de {procent_invatare}.')
print(f'In momentul de fata consider ca este {sunt_pregatit_de_examen} ca as putea sa sustin examenul')
#printam prin concatenare dupa ce am facut casting-ul de la boolean spre string#
print('Sunt pregatita pentru examen:'+ str(sunt_pregatit_de_examen))

"""
#Datele citite de la tastatura se transforma in nr intreg si se atribuie constantei VALOARE_EXCURSIE#
VALOARE_EXCURSIE = int(input('Introduceti costul excursiei'))
procent_discount = float(input('Ati baneficiat de discount?Daca da, introduceti procentul.Daca nu, tastati 0.'))
valoare_discount = VALOARE_EXCURSIE*procent_discount
print(type(valoare_discount))
PRET_CALATORIE = VALOARE_EXCURSIE - valoare_discount
print(f'Pretul calatoriei dvs este de {PRET_CALATORIE}')

