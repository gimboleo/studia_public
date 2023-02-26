using System;

public class List<T> {

    private class Element {
        public T val;
        public Element prev = null;
        public Element next = null;

        public Element(T val) {
        this.val = val;
        }
    }


    private Element begin = null;
    private Element end = null;
    private int size = 0;


    public void push_front(T nval) {
        Element temp = new Element(nval);
        temp.val = nval;

        temp.next = this.begin;
        if (this.begin != null) this.begin.prev = temp;
        this.begin = temp;
        if (this.end == null) this.end = temp;
        
        this.size = this.size + 1;
    }


    public void push_back(T nval) {
        Element temp = new Element(nval);
        temp.val = nval;

        if (this.end != null) this.end.next = temp;
        else this.begin = temp;
        temp.prev = end;
        this.end = temp;

        this.size = this.size + 1;
    }


    public T pop_front() {
        if (this.is_empty()) return default(T);

        T temp = this.begin.val;
        this.begin = this.begin.next;
        if (this.begin != null) this.begin.prev = null;
        else this.end = null;

        this.size = this.size - 1;
        return temp;
    }


    public T pop_back() {
        if (this.is_empty()) return default(T);

        T temp = this.end.val;
        this.end = this.end.prev;
        if (this.end != null) this.end.next = null;
        else this.begin = null;

        this.size = this.size - 1;
        return temp;
    }


    public bool is_empty() {
        if (this.size == 0) return true;
        return false;
    }
}