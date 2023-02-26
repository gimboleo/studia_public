using System;

class Program {
    public static void Main() {
        List<int> lista = new List<int>();
        lista.push_front(5);
        lista.push_front(6);
        lista.push_back(11);
        Console.WriteLine(lista.is_empty());
        Console.WriteLine(lista.pop_front());
        Console.WriteLine(lista.pop_front());
        Console.WriteLine(lista.pop_front());
        Console.WriteLine(lista.is_empty());
        Console.WriteLine(lista.pop_back());        //Lista pusta, funkcja zwroci wartosc domyslna
        Console.WriteLine();

        lista.push_front(1);
        lista.push_back(2);
        lista.push_front(3);
        lista.push_back(4);
        lista.push_front(5);
        lista.push_back(6);
        lista.push_front(7);
        lista.push_back(8);                         //lista: 7 5 3 1 2 4 6 8
        Console.WriteLine(lista.is_empty());
        Console.WriteLine(lista.pop_back());
        Console.WriteLine(lista.pop_back());
        Console.WriteLine(lista.pop_back());
        Console.WriteLine(lista.pop_back());
        Console.WriteLine(lista.pop_front());
        Console.WriteLine(lista.pop_front());
        Console.WriteLine(lista.pop_front());
        Console.WriteLine(lista.pop_front());
        Console.WriteLine(lista.is_empty());
        Console.WriteLine(lista.pop_front());       //Lista pusta, funkcja zwroci wartosc domyslna
        Console.WriteLine();

        List<string> napisy = new List<string>();
        napisy.push_front("ma");
        napisy.push_front("Ala");
        napisy.push_back("Kota");
        Console.WriteLine(napisy.is_empty());
        Console.WriteLine(napisy.pop_front());
        Console.WriteLine(napisy.pop_front());
        Console.WriteLine(napisy.pop_front());
        Console.WriteLine(napisy.pop_back());        //Lista pusta, funkcja zwroci wartosc domyslna
        Console.WriteLine(napisy.is_empty());
        Console.WriteLine();

        napisy.push_back("A");
        napisy.push_front("B");
        napisy.push_back("C");
        napisy.push_front("D");
        napisy.push_back("E");
        napisy.push_front("F");
        napisy.push_back("G");
        napisy.push_front("H");                     //napisy: H F D B A C E G
        Console.WriteLine(napisy.is_empty());
        Console.WriteLine(napisy.pop_front());
        Console.WriteLine(napisy.pop_front());
        Console.WriteLine(napisy.pop_front());
        Console.WriteLine(napisy.pop_front());
        Console.WriteLine(napisy.pop_back());
        Console.WriteLine(napisy.pop_back());
        Console.WriteLine(napisy.pop_back());
        Console.WriteLine(napisy.pop_back());
        Console.WriteLine(napisy.is_empty());
        Console.WriteLine(napisy.pop_back());       //Lista pusta, funkcja zwroci wartosc domyslna
    }
}