package xyz.tbvns;

import java.util.Scanner;

class ex1 {
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
}

class ex2 {
    void main() {
        Scanner input = new Scanner(System.in);
        String data = input.nextLine();

        if (data.equalsIgnoreCase("oui")) {
            System.out.println("YAy 'oui'");
        } else if (data.equalsIgnoreCase("non")) {
            System.out.println("Yay 'non'");
        } else {
            System.out.println("Stupid can't eve,n write a word");
        }
    }
}

class ex3 {
    void  main() {

    }
}