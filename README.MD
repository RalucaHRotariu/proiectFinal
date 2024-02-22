Testare functionalitati site Decathlon

Testele au fost scrise in Python, IDE Pycharm -> Selenium (Pentru a folosi libraria selenium trebuie sa o importam folosind instructiunea insert, din care trebuie sa importam clasa webdriver: from selenium import webdriver) si UnitTest (import unittest, apoi, pentru a putea sa ne folosim de libraria unit test, trebuie sa cream o clasa de teste care sa mosteneasca clasa TestCase din libraria unittest. )

Testele au fost grupate in 3 clase dupa cum urmeaza:

 1. Login
∙ Verificare login cu email correct si parola incorecta
∙ Verificare buton de confirmare este indisponibil
∙ Verificare login cu email si parola corecte
2. Favorites 
∙ verificare lista de favorite este goala
∙ verificare produs adaugat ca favorit  se regaseste in lista de favorite
∙ verificare produsul a fost sters din lista de favorite
∙ verificare produsul a fost mutat din lista de favorite in cosul de cumparaturi
3. Cart
∙ verificare cosul de cumparaturi este gol
∙ verificare produsul selectat a fost adaugat in cosul de cumparaturi
∙ verificare produsul a fost inlaturat din cosul de cumparaturi



