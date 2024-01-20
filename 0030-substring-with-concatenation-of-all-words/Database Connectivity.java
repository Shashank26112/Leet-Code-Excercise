import java.sql.*;

public class JdbcExample {
    public static void main(String[] args) {
        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "username", "password")) {
            Statement statement = connection.createStatement();

            // Create table
            statement.executeUpdate("CREATE TABLE IF NOT EXISTS employees (id INT PRIMARY KEY, name VARCHAR(255))");

            // Insert data
            statement.executeUpdate("INSERT INTO employees (id, name) VALUES (1, 'John')");
            statement.executeUpdate("INSERT INTO employees (id, name) VALUES (2, 'Alice')");

            // Retrieve data
            ResultSet resultSet = statement.executeQuery("SELECT * FROM employees");
            while (resultSet.next()) {
                System.out.println("ID: " + resultSet.getInt("id") + ", Name: " + resultSet.getString("name"));
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
