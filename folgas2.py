dias_do_ano = list(range(1, 366))
weekdaysano = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
folgas = ['domingo', 'sabado', 'sexta', 'quarta']
#weekdays = ['quarta', 'quinta', 'sexta', 'sabado', 'domingo', 'segunda', 'terca']
#folgas = ['sexta', 'quarta', 'domingo', 'sabado']
quantiadias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def diadasemana(lista):
    dict = {}
    i= 0
    for day in lista:
        dict[day] = weekdaysano[i % len (weekdaysano)]
        i += 1
    return dict

def diasdefolga(dict, ordemfolgas):
    dias_de_folga = []
    ii = 0
    for day in dict:
        if dict[day] == ordemfolgas[ii % len(ordemfolgas)]:
            dias_de_folga.append(day)
            ii += 1
    return dias_de_folga

def separarmeses(diasfolgados, quantiadias):
    dict = {}
    i = 1
    somaquantia = 0
    diasdefolga = diasfolgados
    diasprocessados = []
    for quantia in quantiadias:
        diaslista = []
        for dia in diasdefolga:
            if abs(dia - somaquantia) <= quantia and dia not in diasprocessados:
                adddia = abs(dia - somaquantia)
                diaslista.append(adddia)
                diasprocessados.append(dia)
        somaquantia += quantia
        dict[i] = diaslista
        i += 1
    return dict

anodict = diadasemana(dias_do_ano)
diasdefolgaano = diasdefolga(anodict, folgas)
folgaspormes = separarmeses(diasdefolgaano, quantiadias)
print(folgaspormes)

contagemdias = 0
for item in folgaspormes:
    for element in folgaspormes[item]:
        contagemdias += 1
print(contagemdias)