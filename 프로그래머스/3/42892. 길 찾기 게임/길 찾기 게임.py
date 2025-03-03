# 트리 구성 노드 x,y 좌표 값은 정수
# 모든 노드는 서로 다른 x값
# 같은 레벨에 있는 노드는 y좌표 
# 자식 노드의 y값 < 부모 노드 
# 왼쪽 서브 트리  < 부모 < 오른쪽 서브트리

from sys import setrecursionlimit
setrecursionlimit(10000) #기존 1000으로 제한된 재귀 깊이를 늘려줌

class Node(object):
    def __init__(self,info):
        self.num = info[2]
        self.pos = info[:2]
        self.left = None
        self.right = None




def solution(nodeinfo):
    
    for i in range(len(nodeinfo)):
        # [x,y,idx]가 들어가게 인덱스 정보 추가
        nodeinfo[i].append(i+1)
        
    # 왼쪽은 자신보다 y좌표가 작은 노드가 오른쪽은 자신보다 y좌표가 큰 노드가 들어가게 구성
    nodeinfo.sort(key = lambda x : (-x[1],x[0]))
    tree = Node(nodeinfo[0])
    
    for info in nodeinfo[1:]:
        add_node(tree,info)
        
    
    return [pre_order(tree),post_order(tree)]

def add_node(parent,info):
    # 부모보다 x값이 작다면 left 자식
    if parent.pos[0] > info[0]:
        if parent.left:
            add_node(parent.left,info)
        else:
            parent.left = Node(info)
    else:
        if parent.right:
            add_node(parent.right,info)
        else:
            parent.right = Node(info)
            
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
    