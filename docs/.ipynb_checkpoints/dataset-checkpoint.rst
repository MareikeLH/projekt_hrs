Datensatz Beschreibung
======================

research_dataset.csv
--------------------

Der Datensatz beschreibt die Nutzung der HRS-Software im Probezeitraum inkl. der Fortführung von Abos über den Testzeitraum hinaus.

Basics:

- Zeitraum: 1. November 2023 bis 31. Oktober 2024
- n of entities = 10.000
- n of attributes = 9 (alle numerisch, bis auf did_renew (int) alle float)

Liste der Variablen:

- ``sales_calls``: Anzahl Verkaufsgespräche
- ``interactions``: Kontakte mit dem Kunden (inkl Verkaufsgespräche)
- ``economy``: wirtschaftliche Lage des Kunden
- ``last_upgrade``: Tage seit dem letzten Software Update durch den Kunden
- ``discount``: Rabatt der dem Kunden gewährt wird. Höhe des Discounts je nach Gefühl des Sales Mitarbeiters bzgl der Wahrscheinlichkeit, dass ein Kunde abspringen könnte d.h. ein hoher discount deutet schon eher auf eine niedrige Wahrscheinlichkeit hin, dass der Vertrag verlängert wird. Der discount ist ein Angebot, das nicht unbedingt angenommen worden sein muss
- ``monthly usage``: monatliche Nutzung der Software durch den Kunden, normalisiert 0 bis 1
- ``ad_spend``: Höhe der Werbeausgaben in tausend Euro, als Ausgaben des Kunden als Teil der Nutzung der Software (eigene Personalisierung/ Erweiterung)
- ``bugs_reported``: Fehler in der Software, die durch den Kunden gemeldet werden, potentieller Indikator für Engagement der Kunden
- ``did_renew``: Wurde der Nutzungsvertrag am Ende des Testzeitraumes verlängert

Datenqualität:

- Es gibt keine Duplikate und keine Missing Values