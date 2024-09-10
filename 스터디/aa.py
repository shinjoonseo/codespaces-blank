#링크드 리스트 코드
#node 생성 클레스
#속성 dat,link
class Node :
  def __init__(self, data) :
    self.data = data
    self.link = None


class LinkedList :
  def __init__(self) :
    self.Head = Node(None)

  #노드를 끝에 추가하는 함수
  def add_node(self, data) :
    new_node = Node(data)
    if self.Head.link == None :
      self.Head.link = new_node
    else :
      last_node, _ = self.loc_search()
      last_node.link = new_node

  #연결된 링크를 끊어주는 함수
  def delete_link(self) :
    if self.Head.link == None :
      print("연결된 링크가 없습니다.")
    else :
      _, Prev_node = self.loc_search()
      Prev_node.link = None

  #마지막 node를 출력하고 연결은 끊는 함수
  def pop(self) :
    if self.Head.link == None :
      print("연결된 링크가 없습니다.")
    else :
      last_node, Prev_node = self.loc_search()
      Prev_node.link = None
    return last_node.data

  #이전과 이후 node주소를 찾는 함수
  def loc_search(self) :
    last_node = self.Head.link
    Prev_node = None
    while last_node.link != None:
      Prev_node = last_node
      last_node = last_node.link
    return last_node, Prev_node
  

  #가지고있는 데이터를 출력하는 함수
  def link_print(self) :
    loc_node = self.Head.link
    while loc_node != None :
      print(loc_node.data)
      loc_node = loc_node.link
    print("끝")
    
linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.link_print()
print(linked_list.pop())
linked_list.link_print()





    