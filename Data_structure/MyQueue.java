package Data_structure;

public class MyQueue<T> implements DataStructureInterface<T> {
  private Node<T> head; // 큐의 처음노드
  private Node<T> tail; // 큐의 마지막노드


  public MyQueue(){
    head = tail = null;
  }

  
}
