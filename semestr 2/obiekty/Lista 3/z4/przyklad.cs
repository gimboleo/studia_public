using System;
using System.Collections.Generic;

class Program {
    public static void Main() {
        Wektor wek = new Wektor(new List<float> {1, 2, 3});
        Wektor wek2 = new Wektor(new List<float> {4, 5, 6});
        Wektor wek3 = wek + wek2;                   //[5, 7, 9]
        wek3.print();
        Wektor wek4 = wek + wek2 + wek3;            //[10, 14, 18]
        wek4.print();
        wek = wek * wek2;                           //[4, 10, 18]
        wek.print();
        wek = wek * 0.5f;                           //[2, 5, 9]
        wek.print();
        wek = 3 * wek;                              //[6, 15, 27]
        wek.print();
        wek = 0.5f * wek * wek2;                    //[12, 37.5, 81]
        wek.print();
        Console.WriteLine(wek.norma());             //~90.06 dla [12, 37.5, 81]
        Wektor wek5 = wek + (-10 * wek2);           //[12-40, 37.5-50, 81-60] == [-28, -12.5, 21]
        wek5.print();

        Wektor wek6 = new Wektor(new List<float> {1, 2, 3, 4, 5, 6});
        Wektor wek7 = new Wektor(new List<float> {6, 5, 4, 3, 2, 1});
        wek6 = wek6 + wek7;                         //[7, 7, 7, 7, 7, 7]
        wek6.print();
        wek7 = 2 * wek6 * wek7;                     //[84, 70, 56, 42, 28, 14]
        wek7.print();
    }
}