import psycopg2 as ps
import random

'''{
        'pytanie': u'Symbol pierwiastka Helu, to:',
        'odpowiedzi': [u'Fe', u'H', u'He'],
        'odpok': u'He',
    }'''

def funkcjaPytania(dane):
    pytania = []
    for i in range(5):
        numerPytania = random.randint(0,3)
        pyt = dane[numerPytania]
        tmp = {}
        tmp['pytanie'] = pyt[1]
        l = []
        l.append(pyt[2])
        l.append(pyt[3])
        l.append(pyt[4])
        l.append(pyt[5])
        tmp['odpowiedzi'] = l
        tmp['odpok'] = pyt[6]

        pytania.append(tmp)
    return pytania

def baza():
    con = ps.connect("host = localhost dbname = quiz user = postgres password = 1234")
    kursor = con.cursor()
    #kursor.execute("CREATE TABLE pytania2 (id serial PRIMARY KEY, tresc text);")
    kursor.execute("SELECT * FROM pytania")
    dane = kursor.fetchall()
    con.commit()
    kursor.close()
    con.close()
    return funkcjaPytania(dane)


