# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      1.5

stundenansatz = 31.5

anzahl_stunden_pro_tag = 8.4

tageslohn = stundenansatz * anzahl_stunden_pro_tag

# Wir arbeiten während 20 Tagen (Wochenende ausgeschlossen) in einem Monat
anzahl_arbeitstage_pro_monat = 20

monatslohn = tageslohn * anzahl_arbeitstage_pro_monat

print("Der Tageslohn beträgt", tageslohn, "CHF")
print("Der Monatslohn beträgt", monatslohn, "CHF")