import java.util.Scanner;

public class lengthConverter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the length in miles: ");
        double miles = sc.nextDouble();
        double km = miles * 1.60934;
        System.out.println(miles + " miles is " + km + " kilometers");
        sc.close();
    }
}
