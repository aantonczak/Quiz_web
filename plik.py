import psycopg2 as ps
import random
def funkcjaPytania(dane):
    wynik = 0
    for i in range(3):
        numerPytania = random.randint(0,3)
        pyt = dane[numerPytania]
        print(pyt[1])
        print(pyt[2])
        print(pyt[3])
        print(pyt[4])
        print(pyt[5])
        odp = input()
        if odp == pyt[6]:
            wynik += 1

    print(wynik)

con = ps.connect("host = localhost dbname = quiz user = postgres password = 1234")
kursor = con.cursor()
#kursor.execute("CREATE TABLE pytania2 (id serial PRIMARY KEY, tresc text);")
kursor.execute("SELECT * FROM pytania")
dane = kursor.fetchall()
con.commit()
kursor.close()
con.close()
funkcjaPytania(dane)


