package Data_structure;

public class MazeSearch {
  
  private static int[][] move = {{0,1},{1,0},{-1,0},{0,-1}};

  private static boolean isValid (int[][] maze, int x, int y) {
    return x >= 0 && y >= 0 && x< maze.length && y < maze[0].length && maze[x][y] == 0;
  }

  public static boolean DFS (int[][] maze, int startX, int startY, int endX, int endY) {
    DataStructureInterface<int[]> stack = new MyStack<>();
    stack.input(new int[]{startX, startY}); // 시작 지점
    maze [startX][startY] = 2;

    while (!stack.isEmpty()) {
      int[] current = stack.output();
      int currentX = current[0];
      int currentY = current[1];

      if (currentX == endX && currentY == endY) {
        System.out.println("DFS미로의 경로: ");
        stack.entireprint();
        return true;
      }
    }
    return false;
  }
  public static boolean BFS(int[][] maze, int startX, int startY, int endX, int endY) {
    DataStructureInterface<int[]> queue = new MyQueue<>();
    queue.input(new int[]{startX, startY});
    maze [startX][startY] = 2;
    int[][] path = new int[maze.length * maze[0].length][2]; // 경로를 저장할 배열
    int pathIndex = 0; // 경로 인덱스

    while (!queue.isEmpty()) {
      int[] current = queue.output();
      int currentX = current[0];
      int currentY = current[1];

      if (currentX == endX && currentY == endY) {
        System.out.println("BFS미로의 경로: ");
        //도착 지점까지의 경로 복원
        while (maze[currentX][currentY] != 2) {
          path[pathIndex][0] = currentX;
          path[pathIndex][1] = currentY;
          pathIndex++;

          for (int[] search : move) {
            int newX = currentX + search[0];
            int newY = currentY + search[1];
            // 자기 자신보다 1 작으면
            if (newX >= 0 && newY >= 0 && newX < maze.length && newY < maze[0].length&& maze[newX][newY] == maze[currentX][currentY] - 1) { 
              currentX = newX;
              currentY = newY;
              break;
            }
          }
        }
        // 출발지 추가
        path[pathIndex][0] = startX;
        path[pathIndex][1] = startY;
        // 경로 출력
        for (int i = pathIndex; i >= 0; i--) {
        System.out.print("[" + path[i][0] + ", " + path[i][1] + "] ");
        }

        System.out.println();
        return true;
      }
      //주변 탐색
      for (int[] search : move) {
        int newX = currentX + search[0];
        int newY = currentY + search[1];

        if (isValid(maze, newX, newY)) {
          queue.input(new int[]{newX, newY});
          maze[newX][newY] = maze[currentX][currentY] + 1;
        }
      }
    }
    return false; // 경로가 없음
  }
  public static void main(String[] args) {
    // 미로 배열 설정 (0은 이동 가능, 1은 벽)
    int[][] maze = {
        {0, 1, 0, 0, 0, 1},
        {0, 1, 0, 1, 0, 1},
        {0, 0, 0, 1, 0, 0},
        {1, 1, 0, 0, 0, 1},
        {0, 0, 0, 1, 0, 1},
        {1, 1, 0, 0, 0, 0}
    };

    // 결과 출력
    if (BFS(maze, 0, 0, 5, 5)) {
        System.out.println("\n경로를 성공적으로 찾았습니다!");
    } else {
        System.out.println("\n경로를 찾을 수 없습니다.");
    }
  }
}



