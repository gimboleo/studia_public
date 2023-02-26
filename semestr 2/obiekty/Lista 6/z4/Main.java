import java.util.Arrays;

public class Main 
{
    public static void main(String[] args)
    {
        Integer[] test1 = {3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48};
        Integer[] sorted1 = MergeSort.sort(test1);
        System.out.println(Arrays.toString(sorted1));

        String[] test2 = {"sketch", "abolish", "manufacturer", "draw", "embryo", "frog", "calendar", "taste"};
        String[] sorted2 = MergeSort.sort(test2);
        System.out.println(Arrays.toString(sorted2));
    }
}