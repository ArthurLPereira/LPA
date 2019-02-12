import java.io.*;


public class Conversion {
    public static void main(String [] args) {
        translate("101 bin");
    }

    private void translate(String s) {
        String[] parts = s.split(' ');
        System.out.println(parts[0]+" "+parts[1]);
    }
}