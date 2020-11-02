============
Introduction
============

Cette documentation présente les résultats des tests.

La partie python a été implémentée en utilisant spark et hadoop parquet, pour avoir une implémentation type bigdata.
On aurait pu le faire en python sans utiliser spark, le volume de données le permettant.

Je les ai fait tourner sur mon PC perso en local, sous ubuntu 20.04 LTS, l'installation est standard.

L'ingestion fait une correction sur le format de date, par contre on aurait pu aussi corriger le nom des journaux,
par exemple `"Journal of emergency nursing\xc3\x28"` en `"Journal of emergency nursing"`, et aussi corriger les
doublons apparents.
