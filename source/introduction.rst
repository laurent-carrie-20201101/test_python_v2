============
Introduction
============

Cette documentation présente les résultats des tests.

La partie python a été implémentée en utilisant spark et hadoop parquet, pour avoir une implémentation type bigdata.
On aurait pu le faire en python sans utiliser spark, le volume de données le permettant.

Je les ai fait tourner sur mon PC perso en local, sous ubuntu 20.04 LTS, l'installation est standard.

L'arborescence est standard :

.. code-block:: bash

   racine
     + ------ enonce-du-probleme : fichiers fournis pour le test
     + ------ test_de_python_v2 : code python du module de même nom, utilisable par d'autres
     + ------ test : tests unitaires du code python, utilisent le framework pytest
     + ------ sql  : code sql de l'exercice. Contient aussi du code python pour le tester
     + ------ source : les sources de la doc ( la doc est générée par Sphix )
     + ------ demo.py : code python de la demo
     + ------ requirements.txt : modules pythons requis
     + ------ setup.py : script permettant de créer un module de même nom
     + ------ .flake8 : configuration du vérificateur de code
     + ------ .pre-commit-config.yaml : configuration des hooks de pre-commit

Ces fichiers sont disponibles sous <https://github.com/laurent-carrie-20201101/test_python_v2>_
Il y a deux branches master et dev, de façon classique. La branche dev est mergée dans master pour les releases.
D'autres participants, et d'autres outils tels Jira ou Clubhouse, créent une branche par ticket.
