// import java.util.Scanner;
// // v0.1
// public class aa {
//   public static void main(String[] args) {
//     // 소수 : 1과 자기자신외에는 나누어 떨어지지 않는 수
//     Scanner sc = new Scanner(System.in);
//     int number = sc.nextInt();
//     int cnt = 0;

//     for(int k=1; k<=number; k++){
//       if(number % k == 0)
//         cnt++;
//     }

//     if(cnt == 2)
//       System.out.println(number + "은(는) 소수!");
//     else
//       System.err.println(number + "은(는) 소수가 아닙니다");
//   }
// }

// import java.util.Scanner;
// // v0.1
// public class aa {
//   public static void main(String[] args) {
//     // 소수 : 1과 자기자신외에는 나누어 떨어지지 않는 수
//     Scanner sc = new Scanner(System.in);
//     int number = sc.nextInt();
//     int cnt = 0;

//     for(int k=1; k<=number; k++){
//       if(number % k == 0)
//         cnt++;
//     }

//     if(cnt == 2)
//       System.out.println(number + "은(는) 소수!");
//     else
//       System.err.println(number + "은(는) 소수가 아닙니다");
//   }
// }

// import java.util.Scanner;
// // v0.3
// public class aa {
//   public static void main(String[] args) {
//     // 소수 : 1과 자기자신외에는 나누어 떨어지지 않는 수
//     Scanner sc = new Scanner(System.in);
//     int number = sc.nextInt();
//     //int cnt = 0;
//     boolean isPrime = true;

//     for(int k=2; k<number; k++){
//       if(number % k == 0) // 입력된 수를 k로 나누었을 때 나머지가 0인 경우. 즉, 약수
//         //cnt++;
//         isPrime = false;

//     }

//     if(isPrime) // isPrime 변수 값이 true면
//       System.out.println(number + "은(는) 소수!");
//     else
//       System.err.println(number + "은(는) 소수가 아닙니다");
//   }
// }

import java.util.Scanner;
// v0.5
public class aa {
  public static void main(String[] args) {
    // 소수 : 1과 자기자신외에는 나누어 떨어지지 않는 수
    Scanner sc = new Scanner(System.in);
    int number = sc.nextInt();
    //int cnt = 0;
    boolean isPrime = true;

    // for(int k=2; k<number; k++){
    //   if(number % k == 0) {// 입력된 수를 k로 나누었을 때 나머지가 0인 경우. 즉, 약수
    //     //cnt++;
    //     isPrime = false;
    //     break;
    //   }
    // }

    int k=2;
    while (k<number) {
      
      
    }

    if(isPrime) // isPrime 변수 값이 true면
      System.out.println(number + "은(는) 소수!");
    else
      System.err.println(number + "은(는) 소수가 아닙니다");
      
  }
}
