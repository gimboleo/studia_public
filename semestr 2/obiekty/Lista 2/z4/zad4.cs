using System;
using System.Collections.Generic;

class IntStream {
    protected int cur = -1;

    virtual public int next() {
        if (this.eos()) 
        {
            Console.WriteLine("Int overflow");
            return -1;
        }
        this.cur = this.cur + 1;
        return this.cur;
    }

    virtual public bool eos() {
        if (this.cur == Int32.MaxValue) return true;
        return false;
    }

    public void reset() {
        this.cur = -1;
    }
}

class PrimeStream: IntStream {
    protected int NextPrime(int x) {
        if (x < 2) return 2;

        int p = x + 1;

        while (true)
        {
            if (IsPrime(p))
            {
                return p;
            }
            p++;
        }
    }

    bool IsPrime(int x) {
        if (x < 2) return false;
        if (x == 2) return true;

        int roof = System.Convert.ToInt32(Math.Ceiling(Math.Sqrt(x)));

        for (int i = 2; i<= roof; i++)
        {
            if (x % i == 0) return false;
        }
        return true;
    }

    override public int next() {
        if (this.eos()) 
        {
            Console.WriteLine("Int overflow");
            return -1;
        }
        this.cur = NextPrime(this.cur);
        return this.cur;
    }
}



class ListaLeniwa {
    protected List<int> list = new List<int>();

    public int size() {
        return list.Count;
    }

    virtual public int element(int i) {
        if (i < 0) return -1;
        if (i < list.Count) return list[i];

        Random rnd = new Random();
        while (list.Count <= i)
        {
            list.Add(rnd.Next());
        }
        
        return list[i];
    }
}

class Pierwsze: ListaLeniwa {
    PrimeStream pierwsze = new PrimeStream();

    override public int element(int i) {
        if (i < 0) return -1;
        if (i < list.Count) return list[i];

        while (list.Count <= i)
        {
            if (pierwsze.eos())
            {
                return -1;
            }
            list.Add(pierwsze.next());
        }
        return list[i];
    }
}



public class Program {
    public static void Main() {
        ListaLeniwa lista = new ListaLeniwa();
        Console.WriteLine(lista.size());
        Console.WriteLine(lista.element(-1));
        Console.WriteLine(lista.size());
        Console.WriteLine(lista.element(0));
        Console.WriteLine(lista.size());
        Console.WriteLine(lista.element(30));
        Console.WriteLine(lista.size());
        Console.WriteLine(lista.element(25));
        Console.WriteLine(lista.size());
        Console.WriteLine(lista.element(15));
        Console.WriteLine(lista.size());
        Console.WriteLine(lista.element(0));
        Console.WriteLine(lista.size());

        Console.WriteLine();

        Pierwsze prime = new Pierwsze();
        Console.WriteLine(prime.size());
        Console.WriteLine(prime.element(-1));
        Console.WriteLine(prime.size());
        Console.WriteLine(prime.element(0));
        Console.WriteLine(prime.size());
        Console.WriteLine(prime.element(30));
        Console.WriteLine(prime.size());
        Console.WriteLine(prime.element(25));
        Console.WriteLine(prime.size());
        Console.WriteLine(prime.element(15));
        Console.WriteLine(prime.size());
        Console.WriteLine(prime.element(0));
        Console.WriteLine(prime.size());

        Console.WriteLine();

        for (int i = 0; i < 20; i++)
        {
            Console.WriteLine(prime.element(i));
        }
    }
}