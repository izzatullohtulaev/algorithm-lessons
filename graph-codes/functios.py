graph = {'izzat': ['ali', 'vali', 'tohir'],
             'ali': ['aziza', 'olim'],
             'vali': ['botir', 'ziyoda'],
             'tohir': ['elon musk', 'mohir'],
             'olim': [],
             'aziza': [],
             'botir': [],
             'ziyoda': ['aziza'],
             'elon musk': [],
             'mohir': []
             }

from collections import deque

def search(start_node, target='elon musk'):
    search_queue = deque()
    search_queue += graph[start_node]
    searched = set()
    
    while search_queue:
        person = search_queue.popleft()
        if person == target:
            print(f"{target}ni topdim!")
            return True
        else:
            search_queue+=graph[person]
            searched.add(person)
    return False
search('izzat', 'mohir')