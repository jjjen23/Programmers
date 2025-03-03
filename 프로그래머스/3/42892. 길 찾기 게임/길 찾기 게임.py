# 트리 구성 노드 x,y 좌표 값은 정수
# 모든 노드는 서로 다른 x값
# 같은 레벨에 있는 노드는 y좌표 
# 자식 노드의 y값 < 부모 노드 
# 왼쪽 서브 트리  < 부모 < 오른쪽 서브트리

from sys import setrecursionlimit
setrecursionlimit(10000) #기존 1000으로 제한된 재귀 깊이를 늘려줌

class Node(object):
    def __init__(self,info):
        self.num = info[2] # 노드(idx) 번호 저장
        self.pos = info # [x,y,idx]
        self.left = None 
        self.right = None

# parent == tree 
# info == 신입
# add_node 함수 == 트리의 루트부터 탐색하며 조건에 맞는 신입 자리 찾아주는 함수
def add_node(parent,info):
    # 부모 보다 x값이 작다면 left으로
    if parent.pos[0] > info[0]:
        # 자식이 존재하면 재귀 호출, 자식이 없는 곳 까지 깊이 탐색
        if parent.left:
            add_node(parent.left,info)
        # None이라면, 새로운 노드를 생성하여 부모의 자식으로 설정
        else:
            parent.left = Node(info)
    # 부모보다 x값이 크다면 right으로
    else:
        if parent.right:
            add_node(parent.right,info)
        else:
            parent.right = Node(info)


def solution(nodeinfo):
    
    for i in range(len(nodeinfo)):
        # [x,y,idx]가 들어가게 인덱스 정보 추가
        nodeinfo[i].append(i+1)
        
    # 왼쪽은 자신보다 y좌표가 작은 노드가 오른쪽은 자신보다 y좌표가 큰 노드가 들어가게 구성 -> 부모노드가 먼저 나오도록 정렬해줌. -> 여기까진 사고함(?)
    nodeinfo.sort(key = lambda x : (-x[1],x[0]))
    
    tree = Node(nodeinfo[0]) # 트리생성,루트생성
    
    # 생성된 루트에 add_node함수를 통해서 노드를 추가해나감
    for info in nodeinfo[1:]:
        add_node(tree,info)
        
    
    return [pre_order(tree),post_order(tree)]


            
# 부모 -> Left -> Right 순서로
def pre_order(curr):
    path = [curr.num]
    if curr.left:
        path += pre_order(curr.left)
    if curr.right:
        path += pre_order(curr.right)
        
    return path

# Left -> Right -> 부모 순서로
def post_order(curr):
    path = []
    if curr.left:
        path += post_order(curr.left)
    if curr.right:
        path += post_order(curr.right)
        
    path.append(curr.num)
    
    return path
    