# algorithm

## Union Find (서로소 인가?)
두 원소(node)가 서로 겹치는게 없는가? 그렇다면 서로 서로소 관계이다.

- 뽀삐는 동명이견일 뿐 두 건달은 명백히 서로소이다. 장삐쭈 단편선 [시비]

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/13_yNqnlppM/0.jpg)](https://www.youtube.com/watch?v=13_yNqnlppM)



- 어데 최씹니꼬? 최익현(최민식)은 검찰 조사를 벗어나기 위해 먼 친척 당숙어른을 거쳐 더 먼 친척 부장검사 최주동(김응수)를 통해 담당검사를 압박한다. 최익현과 담당검사는 가까스로 서로소가 아니다. - 범죄와의 전쟁

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/-niYJCs7QiA/0.jpg)](https://www.youtube.com/watch?v=-niYJCs7QiA)


최익현, 당숙어른, 부장검사를 node라고 생각하자. 당숙어른은 최익현의 root node다. 최익현은 검찰과는 아무 연결점이 없는 서로소였다. 족보를 통해 당숙어른, 부장검사를 거쳐 담당검사까지 연결한 건 서로 관계를 합집합(Union)을 했다고 볼 수 있다.

당숙어른과 부장검사를 찾는 과정을 함수로 find_root

최씨 집안과 담당검사 사이 다리를 놓는 걸 union_root

최익현과 당담검사 사이 서로소인지 확인하는 걸 is_same_root

is_same_root가 True로 나올 것이므로 서로소가 아니다.

---
