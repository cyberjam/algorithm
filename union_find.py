# 나동빈 강의 : https://www.youtube.com/watch?v=AMByrd53PHM
# C++ -> Python

def find_root(node_list, node):
  is_root = node_list[node] == node
  if is_root:
    return node
  else: 
    node_list[node] = find_root(node_list, node_list[node])
    return node_list[node]
    
def union_root(node_list, node_a, node_b):
  node_a_root = find_root(node_list, node_a)
  node_b_root = find_root(node_list, node_b)
  if node_a_root < node_b_root:
    node_list[node_b_root] = node_a_root
  else:
    node_list[node_a_root] = node_b_root

def is_same_root(node_list, node_a, node_b):
  node_a_root = find_root(node_list, node_a)
  node_b_root = find_root(node_list, node_b)
  return node_a_root == node_b_root

def main():
  node_list = [index for index in range(10)]
  print(node_list)
  union_root(node_list, 0, 1)
  print(node_list)
  union_root(node_list, 1, 2)
  print(node_list)
  union_root(node_list, 2, 3)
  print(node_list)
  union_root(node_list, 3, 4)
  print(node_list)
  union_root(node_list, 5, 6)
  print(node_list)
  union_root(node_list, 6, 7)
  print(node_list)
  union_root(node_list, 7, 8)
  print(node_list)
  union_root(node_list, 8, 9)
  print(node_list)
  print(is_same_root(node_list, 4, 6))
  union_root(node_list, 1, 7)
  print(node_list)
  print(is_same_root(node_list, 4, 5))
  print(node_list)

if __name__ == "__main__":
  main()
