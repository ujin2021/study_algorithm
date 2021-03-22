# 출발 노드와 도착노드 설정
graph = {
    'A' : {'B' : 8, 'C' : 1, 'D' : 2},
    'B' : {},
    'C' : {'B' : 5, 'D' : 2},
    'D' : {'E' : 3, 'F' : 5},
    'E' : {'F' : 1},
    'F' : {'A' : 5}
}

import heapq # heapq : 우선순위 큐 구현

def dijkstra(graph, start) :
    distances = {node: float('inf') for node in graph} # start로 부터 노드까지의 거리(inf로 초기화)
    distances[start] = 0 # start -> start 니까 0으로 설정
    queue = []
    heapq.heappush(queue, [distances[start], start]) # queue = [0, 'A'] (시작노드부터 탐색)
    
    while queue : # queue에 남아있는 노드가 없으면 끝난다
        print('\n new while')
        current_distance, current_destination = heapq.heappop(queue) # 거리, 탐색할 노드를 가지고 온다
        print(f'A(start) -> {current_destination}(current) : {current_distance}')
        # current_distance : start -> destination 거리, current_destination : 탐색할 노드

        print(f'distances[current_destination] : {distances[current_destination]} < current_distance : {current_distance} => {distances[current_destination] < current_distance}')
        if distances[current_destination] < current_distance :
            # 계산해 놓은 A -> destination 거리보다 현재 거리가 더 크면 볼필요 없음
            print('continue')
            continue
        # 만약 계산해놓은 거리보다 지금이 같거나 짧다면 => 짧은걸로 갱신해야겠지
        print('items : ',graph[current_destination].items())
        for new_destination, new_distance in graph[current_destination].items():
            print(f'[new_destination, new_distance] : {new_destination}, {new_distance}')
            distance = current_distance + new_distance # 해당 노드를 거쳐 갈 때 거리
            print(f'distance : {distance} (current_distance : {current_distance} + new_distance : {new_distance})')
            print(f'distance({distance}) < distances[new_destination]({distances[new_destination]}) => {distance < distances[new_destination]}')
            if (distance < distances[new_destination]) : # 알고 있는 거리 보다 작으면 갱신
                print('===renew distance===')
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination]) # 다음 인접 거리를 계산하기 위해 큐에 삽입
                print(f'after renew distance queue : {queue}')
    return distances
    
print(dijkstra(graph, 'A'))
# q = []
# heapq.heappush(q, [2, 'D'])
# heapq.heappush(q, [8, 'B'])
# heapq.heappush(q, [3, 'E'])
# heapq.heappush(q, [1, 'C'])
# heapq.heappush(q, [6, 'F'])
# print(q) # [[1, 'C'], [2, 'D'], [3, 'E'], [8, 'B'], [6, 'F']]