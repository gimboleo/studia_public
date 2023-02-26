using System;
using System.Collections.Generic;

public class Wektor {
    private List<float> cords = new List<float>();
    private int size = 0;

    public Wektor(List<float> new_v) {
        if (new_v != null)
        {
            this.size = new_v.Count;
            for (int i = 0; i < this.size; i++)
            {
                this.cords.Add(new_v[i]);
            }
        }
    }


    public void print() {
        for (int i = 0; i < this.size; i++)
        {
            Console.Write(this.cords[i] + " ");
        }
        Console.WriteLine();
    }


    public static Wektor operator +(Wektor v1, Wektor v2) {
        if (v1.size != v2.size) return v1;
        Wektor v3 = new Wektor(null);
        for (int i = 0; i < v1.size; i++) v3.cords.Add(v1.cords[i] + v2.cords[i]);
        v3.size = v1.size;
        return v3;
    }


    public static Wektor operator *(Wektor v1, Wektor v2) {
        if (v1.size != v2.size) return v1;
        Wektor v3 = new Wektor(null);
        for (int i = 0; i < v1.size; i++) v3.cords.Add(v1.cords[i] * v2.cords[i]);
        v3.size = v1.size;
        return v3;
    }


    public static Wektor operator *(float val, Wektor v) {
        Wektor v2 = new Wektor(null);
        for (int i = 0; i < v.size; i++) v2.cords.Add(val * v.cords[i]);
        v2.size = v.size;
        return v2;
    }


    public static Wektor operator *(Wektor v, float val) {
        Wektor v2 = new Wektor(null);
        for (int i = 0; i < v.size; i++) v2.cords.Add(val * v.cords[i]);
        v2.size = v.size;
        return v2;
    }


    public float norma() {
        Wektor temp = this * this;
        float res = 0;
        for (int i = 0; i < temp.size; i++)
        {
            res = res + temp.cords[i];
        }
        res = (float)Math.Sqrt(res);
        return res;
    }
}