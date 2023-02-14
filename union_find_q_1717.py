#https://www.acmicpc.net/problem/1717

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

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
  is_same_root = node_a_root == node_b_root
  return "YES" if is_same_root else "NO"
     
  

def main():
  n, m = map(int, input().split())
  node_list = [index for index in range(n+1)]
  
  for turn in range(m):
    operator, node_a, node_b = map(int, input().split())
    if operator == 0:
      union_root(node_list, node_a, node_b)
    elif operator == 1:
      print(is_same_root(node_list, node_a, node_b))

if __name__ == "__main__":
  main()
