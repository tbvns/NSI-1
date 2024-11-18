import java.util.Scanner;

void main() {
    Scanner input = new Scanner(System.in);
    String data = input.nextLine();
    try {
        int i = Integer.parseInt(data);
        if (i<=5) {
            System.out.println("Yay it worked");
        } else {
            System.out.println("that's above 1 stupid !");
        }
    } catch (Exception e) {
        System.out.println("Stupid that's not a number !");
    }
}