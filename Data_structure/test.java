package Data_structure;

public class test {
  public static void main(String[] args) {
    MyQueue<Integer> queue = new MyQueue<>();

    // 1부터 10까지 큐에 추가
    for (int i = 1; i <= 10; i++) {
        queue.input(i);
    }

    // 큐의 모든 요소 출력
    System.out.println("큐의 모든 요소:");
    queue.entireprint();

    // 큐에서 요소 하나씩 제거하며 출력
    System.out.println("큐에서 요소 제거:");
    while (!queue.isEmpty()) {
        System.out.print(queue.output() + " ");
    }
    System.out.println();

    // 큐가 비어있는지 확인
    System.out.println("큐가 비어있는가? " + queue.isEmpty());
  }
}


