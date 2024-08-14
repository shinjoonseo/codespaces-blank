#링크드 리스트 리스트 코드
#node 생성 클레스
#속성 dat,link
class Node() :
  data = None
  link = None
  def __init__(self, data, link = None) :
    self.data = data
    self.link = None


class Linkdlist() :
  def __init__(self) :
    self.Head = Node(None)

  def add_node(self,node) :
    self.Head.next = node
  
  def link_print(self) :
    loc_node = self.Head :

    while loc_node = None :
      loc_node = loc_node.next
      print(loc_node)


    