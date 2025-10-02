import java.util.ArrayList;
import java.util.Collections;

public class MyArrayLinearList {
    private ArrayList<Integer> list;

    // Constructor
    public MyArrayLinearList() {
        list = new ArrayList<>();
    }

    // Add element
    public void add(int value) {
        list.add(value);
    }

    // Print list
    public void display() {
        System.out.println(list);
    }

    // 1. max() - find maximum value
    public int max() {
        if (list.isEmpty()) {
            throw new IllegalStateException("List is empty.");
        }
        return Collections.max(list);
    }

    // 2. min() - find minimum value
    public int min() {
        if (list.isEmpty()) {
            throw new IllegalStateException("List is empty.");
        }
        return Collections.min(list);
    }

    // 3. sum() - calculate sum
    public int sum() {
        int s = 0;
        for (int num : list) {
            s += num;
        }
        return s;
    }

    // 4. average() - calculate average
    public double average() {
        if (list.isEmpty()) {
            throw new IllegalStateException("List is empty.");
        }
        return (double) sum() / list.size();
    }

    // 5. removeOdd() - remove odd numbers
    public void removeOdd() {
        list.removeIf(num -> num % 2 != 0);
    }

    // 6. sort() - sort in ascending order
    public void sort() {
        Collections.sort(list);
    }

    // Main for testing
    public static void main(String[] args) {
        MyArrayLinearList myList = new MyArrayLinearList();

        myList.add(5);
        myList.add(2);
        myList.add(9);
        myList.add(4);
        myList.add(7);

        System.out.print("Original list: ");
        myList.display();

        System.out.println("Max: " + myList.max());
        System.out.println("Min: " + myList.min());
        System.out.println("Sum: " + myList.sum());
        System.out.println("Average: " + myList.average());

        myList.removeOdd();
        System.out.print("After removing odd numbers: ");
        myList.display();

        myList.sort();
        System.out.print("Sorted list: ");
        myList.display();
    }
}
