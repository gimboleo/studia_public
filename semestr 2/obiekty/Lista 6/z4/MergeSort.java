import java.util.Arrays;

public class MergeSort<T extends Comparable<T>>
{
    private static <T extends Comparable<T>> void Merge(T[] array, int b1, int e1, int b2, int e2)
    {
        T[] temp = Arrays.copyOf(array, array.length);
        int i = b1;
        int p1 = b1;
        int p2 = b2;
        
        //System.out.println(Arrays.toString(temp));

        while (p1 <= e1 && p2 <= e2)
        {
            if (array[p1].compareTo(array[p2]) < 0)
            {
                temp[i] = array[p1];
                p1++;
            }
            else
            {
                temp[i] = array[p2];
                p2++;
            }
            i++;
        }

        while (p1 <= e1)
        {
            temp[i] = array[p1];
            p1++;
            i++;
        }

        while (p2 <= e2)
        {
            temp[i] = array[p2];
            p2++;
            i++;
        }
       
        //System.out.println(Arrays.toString(temp));
        //System.out.println();

        for(int j = b1; j <= e2; j++)
        {
            array[j] = temp[j];
        }
    }


    private static class SortThreads<T extends Comparable<T>> extends Thread
    {
        private T[] array;
        private int b;
        private int e;

        public SortThreads(T[] array, int b, int e)
        {
            this.array = array;
            this.b = b;
            this.e = e;
        }

        public void run()
        {
            if (b == e) return;

            int m = (b + e) / 2;
            Thread[] Threads = new Thread[2];
            Threads[0] = new SortThreads<T>(array, b, m);
            Threads[1] = new SortThreads<T>(array, m+1, e);

            Threads[0].start();
            Threads[1].start();
            
            try 
            {
                Threads[0].join();
                Threads[1].join();
            } 
            catch (InterruptedException exc) 
            {
                System.out.println(exc);
                System.exit(1);
            }

            Merge(array, b, m, m+1, e);
        }
    }


    public static <T extends Comparable<T>> T[] sort(T[] array)
    {
        T[] sorted = Arrays.copyOf(array, array.length);

        Thread MainThread = new SortThreads<T>(sorted, 0, sorted.length - 1);
        MainThread.start();

        try 
        {
            MainThread.join();
        } 
        catch (InterruptedException exc) 
        {
            System.out.println(exc);
            System.exit(1);
        }

        return sorted;
    }
}