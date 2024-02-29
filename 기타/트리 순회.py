# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.
#
# 예를 들어 위와 같은 이진 트리가 입력되면,
#
# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
# 가 된다.
#
#
# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.
#
#
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

import sys

class Node:
    def __init__(self, v = None, l = None, r = None):
        self.value = v
        self.lvalue = l
        self.rvalue = r

def preorder(node):
    print(node.value, end='')
    if node.lvalue != '.':
        preorder(tree[node.lvalue])
    if node.rvalue != '.':
        preorder(tree[node.rvalue])

def inorder(node):
    if node.lvalue != '.':
        inorder(tree[node.lvalue])
    print(node.value, end='')
    if node.rvalue != '.':
        inorder(tree[node.rvalue])

def postorder(node):
    if node.lvalue != '.':
        postorder(tree[node.lvalue])
    if node.rvalue != '.':
        postorder(tree[node.rvalue])
    print(node.value, end='')

input = sys.stdin.readline
n = int(input())
inputs = list()
[inputs.append(input().split()) for _ in range(n)]

tree = dict()
for v, l, r in inputs:
    tree[v] = Node(v, l, r)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
