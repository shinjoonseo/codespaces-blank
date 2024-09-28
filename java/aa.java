import java.util.Scanner;

public class aa {
  public static void main(String[] args) {
    //Pokemon pokemon = new Pokemon(); // 추상클래스의 객체(인스턴스) 생성 불가
    
    Scanner scanner = new Scanner(System.in);
    String name = scanner.next();
    System.out.println("Hello " + name + "!");
  }
}
