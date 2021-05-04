import java.util.Scanner;
import java.util.*;

public class Animal{
    public static final double FAVNUMBER=1.6180;
    private String name;
    private int weight;
    private boolean hasOwner=false;
    private byte age;
    private long uniqueID;
    private char favouriteChar;
    private float height;

    protected static int numberOfAnimal=0;
    static Scanner userinput=new Scanner(System.in);

    public Animal(){
        numberOfAnimal++;
        int sumOfNumbers=5+1;
        System.out.println("5 + 1 = "+sumOfNumbers);
    }


}
