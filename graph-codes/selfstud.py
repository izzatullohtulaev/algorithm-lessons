from collections import deque

def search(start_node, target='mohir'):
    search_que = deque()
    search_que += (graph[start_node])
    searched = set()
    while search_que:
        person = search_que.popleft()
        if person==target:
            print(f"{target}ni topdim!")
            return True
        else:
            search_que += graph[person]
            searched.add(person)
    return False

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
