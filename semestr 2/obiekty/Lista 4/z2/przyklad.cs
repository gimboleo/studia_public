using System;

public class Program {
    public static void Main() {
        PrimeCollection pc = new PrimeCollection();

        foreach(int p in pc) 
        {
        Console.WriteLine(p);
        if (p > 1000) break;
        }

        foreach(int p in pc) 
        {
        Console.WriteLine(p);
        if (p > 1000) break;
        }
    }
}