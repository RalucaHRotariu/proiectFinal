			De ce este importantă testarea automată?

Testarea automată reduce sarcinile manuale repetitive în timpul fazei de testare. 
- permite realizarea mai multor teste în mai puțin timp, mărind astfel productivitatea și capacitatea de testare.
- înlătura eroarea umană, un script configurând mereu în același fel și validând mereu în același mod scenariul dorit.


			Test Driven Development (TDD)
- este un proces de dezvoltare software
- se bazeaza pe transformarea cerintelor de business in teste inainte de a avea codul sursa dezvoltat. 

TDD este in general implementat de catre echipa de dezvoltare prin definirea a ceea ce se numesc teste unitare care vor testa ceea ce stim ca ar trebui sa faca sistemul.


			Avantajele utilizarii unui TDD: 

- Ajuta la crearea minimului de cod optim necesar implementarii unei functionalitati
- Se concentreaza pe teste, asigurand astfel o aplicatie mai apropiata de nevoile clientului
- Asigura o acoperire mai mare a aplicatiei prin teste
- Codul este mai usor de intretinut.

			Testarea unitară (sau de componente) 

- este o modalitate prin care fiecare bucată individuală de cod este testată pentru a verifica dacă este pregatită pentru utilizare. 

Un test unitar reprezintă testarea celei mai mici bucăți funcționale dintr-o aplicație cum ar fi funcții, clase, proceduri, interefețe.



				Testare functionalitati site Decathlon

Testele au fost scrise in Python, IDE Pycharm -> Selenium (Pentru a folosi libraria selenium trebuie sa o importam folosind instructiunea insert, din care trebuie sa importam clasa webdriver: from selenium import webdriver) si UnitTest (import unittest, apoi, pentru a putea sa ne folosim de libraria unit test, trebuie sa cream o clasa de teste care sa mosteneasca clasa TestCase din libraria unittest).  
Pentru rulare, se poate executa comanda: "python AllTestsSuite.py"

Testele au fost grupate in 3 clase dupa cum urmeaza:

 1. TestLogin

- Verificare login cu email correct si parola incorecta
- Verificare buton de confirmare este indisponibil
- Verificare login cu email si parola corecte

2. TestFavorites 

- verificare lista de favorite este goala
- verificare produs adaugat ca favorit  se regaseste in lista de favorite
- verificare produsul a fost sters din lista de favorite
- verificare produsul a fost mutat din lista de favorite in cosul de cumparaturi

3. TestCart

- verificare cosul de cumparaturi este gol
- verificare produsul selectat a fost adaugat in cosul de cumparaturi
- verificare produsul a fost inlaturat din cosul de cumparaturi

   Clasa TestUtils contine cele doua metode de SetUp si TearDown folosite in toate testele create.

   Clasa AllTestsSuite contine suita de teste si ne ajuta sa:

- Rulam toate testele in acelasi timp
- Specificam configuratia pentru raportul de executie


   			Atunci cand vrem sa rulam testele putem sa o facem sub mai multe forme: 
 - Click pe triunghiul verde de langa numele clasei de test -> va rula toate testele din acea clasa
 - Click pe triunghiul verde de langa numele metodei de test -> va executa doar metoda de test pe care am rulat-o
 - Rularea din terminal a unui fisier de teste specific: python -m unittest filename.py
 - Rularea din terminal a tuturor fisierelor de test: python -m unittest


            			 Configurarea raportului

- va trebui sa definim un runner care sa contina parametrii de configurare ai raportului de executie:

runner = HTMLTestRunner(output='report',      	                      
			combine_reports=True,                                     
			report_title='TestLogin Results',                                        
			report_name='Login Automated Test Results')

Pentru a putea avea acest runner functional trebuie sa instalam (pip install html-testRunner) si sa importam (from HtmlTestRunner import HTMLTestRunner) libraria aferenta. 

- runner este un obiect instantiat din clasa HTMLTestRunner care a primit drept argumente valorile combine_reports, report_title si report_name.





