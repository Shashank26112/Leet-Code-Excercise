import java.io.*;

public class FileIOExample {
    public static void main(String[] args) {
        // Write to file
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("example.txt"))) {
            writer.write("Hello, this is an example!");
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Read from file
        try (BufferedReader reader = new BufferedReader(new FileReader("example.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
