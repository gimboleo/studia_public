using System;

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

class RandomStream: IntStream {
    Random rnd = new Random();
    
    override public int next() {
        return rnd.Next();
    }
}

class RandomWordStream: PrimeStream {
    string RandomString(int x) {
        string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuwxyz";
        char[] res = new char[x];
        Random rnd = new Random();

        for (int i = 0; i < res.Length; i++)
        {
            res[i] = chars[rnd.Next(chars.Length)];
        }

        string stres = new string(res);
        return stres;
    }

    new public string next() {
        if (this.eos()) 
        {
            Console.WriteLine("Int overflow");
            return "error";
        }
        this.cur = NextPrime(this.cur);
        return RandomString(cur);
    }
}



class Program {
    public static void Main() {
        IntStream strumien = new IntStream();
        Console.WriteLine(strumien.eos());
        Console.WriteLine(strumien.next());
        Console.WriteLine(strumien.eos());
        Console.WriteLine(strumien.next());
        Console.WriteLine(strumien.eos());
        Console.WriteLine(strumien.next());
        Console.WriteLine(strumien.eos());
        strumien.reset();
        Console.WriteLine(strumien.next());

        Console.WriteLine();

        RandomStream losowy = new RandomStream();
        Console.WriteLine(losowy.next());
        Console.WriteLine(losowy.next());
        Console.WriteLine(losowy.next());
        Console.WriteLine(losowy.next());
        Console.WriteLine(losowy.next());

        Console.WriteLine();

        PrimeStream pierwsze = new PrimeStream();
        Console.WriteLine(pierwsze.next());
        Console.WriteLine(pierwsze.next());
        Console.WriteLine(pierwsze.next());
        Console.WriteLine(pierwsze.next());
        Console.WriteLine(pierwsze.next());
        Console.WriteLine(pierwsze.next());

        Console.WriteLine();

        RandomWordStream slowa = new RandomWordStream();
        Console.WriteLine(slowa.next());
        Console.WriteLine(slowa.next());
        Console.WriteLine(slowa.next());
        Console.WriteLine(slowa.next());
        Console.WriteLine(slowa.next());
    }
}
