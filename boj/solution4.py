# [재귀] 1991 트리순회

n = int(input())
tree = dict()

def preorder(tree, root) : # root / 왼 / 오
    result = []
    if(root == '.') :
        return []
    result.append(root)
    result += preorder(tree, tree[root][0])
    result += preorder(tree, tree[root][1])
    return result

def inorder(tree, root) : # 왼 / root / 오
    result = []
    if(root == '.') :
        return []
    result += inorder(tree, tree[root][0])
    result.append(root)
    result += inorder(tree, tree[root][1])
    return result

def postorder(tree, root) : # 왼 / 오 / root
    result = []
    if(root == '.') :
        return []
    result += postorder(tree, tree[root][0])
    result += postorder(tree, tree[root][1])
    result.append(root)
    return result

for _ in range(n) :
    nodes = input().split()
    tree[nodes.pop(0)] = nodes

preorder_result = preorder(tree, 'A')
inorder_result = inorder(tree, 'A')
postorder_result = postorder(tree, 'A')

print(''.join(preorder_result))
print(''.join(inorder_result))
print(''.join(postorder_result))