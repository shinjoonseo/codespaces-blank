import java.io.FileWriter;
import java.io.IOException;

public class Game{
    public static void main(String[] args) {
        // try catch resource
        try(FileWriter file = new FileWriter("inha.txt")){
            file.write("Hello Java~");
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}


//import java.io.FileWriter;
//import java.io.IOException;
//
//public class Game{
//    public static void main(String[] args) throws IOException {
//        FileWriter file = null;
//        try{
//            file = new FileWriter("inha.txt");
//            file.write("Hello Java~");
//        } finally {
//          file.close();
//        }
//    }
//}



//import java.io.FileWriter;
//import java.io.IOException;
//
//public class Game{
//    public static void main(String[] args) {
//        FileWriter file = null;
//        try{
//            file = new FileWriter("inha.txt");
//            file.write("Hello Java~");
//        } catch (IOException e){
//            throw new RuntimeException();
//        } finally {
//            try {
//                file.close();
//            } catch (IOException e){
//                throw new RuntimeException();
//            }
//        }
//    }
//}


