
===========
python code
===========

.. _code_p1:

process p1
----------

lit le fichier csv et l'écrit dans parquet

.. literalinclude:: ../test_de_python_v2/ingest_drug.py
    :linenos:
    :language: python
    :pyobject: ingest


.. _code_p2:

process p2
----------

lit le fichier csv et l'écrit dans parquet
en essayant de corriger le champ date

.. literalinclude:: ../test_de_python_v2/ingest_pubmed.py
    :linenos:
    :language: python
    :pyobject: ingest

le mapping permet de corriger le champ date, en testant quelques
formats possibles et en retenant le premier qui marche

.. literalinclude:: ../test_de_python_v2/ingest_pubmed.py
    :linenos:
    :language: python
    :pyobject: _correct_date

.. _code_p3:

process p3
----------

lit le fichier csv et l'écrit dans parquet
en essayant de corriger le champ date, et le nom du journal

.. literalinclude:: ../test_de_python_v2/ingest_clinical_trial.py
    :linenos:
    :language: python
    :pyobject: ingest


le mapping permet de corriger le champ date, et aussi quelques caractères
apparemment erronés dans le nom du journak

.. literalinclude:: ../test_de_python_v2/ingest_clinical_trial.py
    :linenos:
    :language: python
    :pyobject: _correct_item

.. _code_p4:

process p4
----------

les parquets drug et pubmed sont utilisés pour faire un produit cartésien,
et on filtre pour ne garder que les enregistrements pour lesquels le nom de la drogue
est vu dans le titre de la publication

.. literalinclude:: ../test_de_python_v2/find_references.py
    :linenos:
    :language: python
    :pyobject: find_references_drug_pubmed


.. _code_p5:

process p5
----------

les parquet drug et clinical trial sont utilisés pour faire leur produit cartésien,
et on filtre pour ne garder que les enregistrements pour lesquels le nom de la drogue
est vu dans le titre scientifique de l'essai clinique

.. literalinclude:: ../test_de_python_v2/find_references.py
    :linenos:
    :language: python
    :pyobject: find_references_drug_clinical_trial

.. _code_p6:

process p6
----------

on utilise les parquet drug, clinical trial et journal, on fait le produit cartésien
de drug et pubmed, on filtre sur les mentions.
de même avec drug et clinical clients, on filtre.

les deux dataframe sont projetés sur les mêmes colonnes drug_atccode, journal et date, on peut
faire leur union, retirer les duplications et enregistrer dans le parquet suivant.

Remarque : on pourrait utiliser p4 et p5 comme entrée de p6.

.. literalinclude:: ../test_de_python_v2/find_references.py
    :linenos:
    :language: python
    :pyobject: find_references_drug_journal

.. _code_p7:

process p7
----------

On utilise les trois parquets permettant de savoir les relations entre drug, clinical trial et
journal (par rapport à savoir qui référence une drogue).
On itère sur ces parquets pour générer le json en sortie.

Le code étant le même pour les trois itérations, il a été factorisé.

Le format json n'étant pas utilisable pour du bigdata, on se limite à max_allowed enregistrements.

.. literalinclude:: ../test_de_python_v2/json_result.py
    :linenos:
    :language: python
    :pyobject: write_json

.. _code_p8:

process p8
----------

On parcourt le json, c'est un dictionnaire dont la clef est la drogue. On utilise une list comprehension
pour n'avoir que les journaux. Cette liste est la liste des noms des journaux. Enfin le module collections
de python nous fournit ce qu'il faut pour avoir le nom le plus commun.

.. literalinclude:: ../test_de_python_v2/extract_journal_with_most_drugs.py
    :linenos:
    :language: python
    :pyobject: find_journal_with_most_drugs
