import json
from pathlib import Path
import sys
import pprint
import collections


def find_journal_with_most_drugs(json_file: Path) -> str:
    '''
    the struct of json report is :
    j : dict[drug,drug_data]

    drug_data : dict
        name : str
        clinical_trials : list of dict(keys : date,id )
        journaux : list of dict(keys: date,id)
        pubmeds : list of dict(keys: date,id)

    '''
    with open(str(json_file), 'r') as fin:
        j = json.load(fin)

    # we get the names of all journaux referenced
    names = [d['id'] for _, item in j.items() for d in item['journaux']]
    counter = collections.Counter(names)

    return counter.most_common(1)


if __name__ == '__main__':
    result = find_journal_with_most_drugs(Path(sys.argv[1]))
    print(result)
