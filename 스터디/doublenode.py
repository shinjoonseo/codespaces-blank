class Node :
  def __init__(self, data, right = None, left = None) :
    self.data = data
    self.right = right
    self.left = left

class Deque :
  def __init__(self) :
    self.head = Node(None)
    self.head.right = self.head

  def add_left(self, data):
    new_node = Node(data)
    if self.head.right == self.head :
      self.head.right = new_node

      self.head.right.left = self.head.right
      self.head.right.right = self.head.right

    elif self.head.right.right == self.head.right:
      new_node.right = self.head.right
      new_node.left = self.head.right
      
      self.head.right.left = new_node
      self.head.right.right = new_node
      self.head.right = new_node

    else:
      #추가할 node의 링크를 Head와 처음node와 연결해준다
      new_node.right = self.head.right
      new_node.left = self.head.right.left

      #Head와 처음 node의 링크를 new_node로 변경한다.
      self.head.right = new_node
      self.head.right.left = new_node

  def add_right(self, data):
    new_node = Node(data)
    if self.head.right == self.head :
      self.head.right = new_node

      self.head.right.left = self.head.right
      self.head.right.right = self.head.right

    elif self.head.right.right == self.head.right :
      new_node.right = self.head.right
      new_node.left = self.head.right
      
      
      self.head.right.left = new_node
      self.head.right.right = new_node

    else:
      #추가할 node의 링크를 Head와 처음node와 연결해준다
      new_node.right = self.head.right
      new_node.left = self.head.right.left

      #Head와 처음 node의 링크를 new_node로 변경한다.
      self.head.right.left.right = new_node
      self.head.right.left = new_node

  def double_print(self) :
    loc_node = self.head

    if self.head.right == self.head :
      print('끝')
    
    else :
      start_node = self.head.right
      print(start_node.data)
      loc_node = start_node

      while loc_node.right != start_node :
        loc_node = loc_node.right
        print(loc_node.data)

# Deque 사용 예시
deque = Deque()

# 앞쪽에 추가
deque.add_left(1)
deque.add_left(2)
deque.add_left(3)
deque.double_print()