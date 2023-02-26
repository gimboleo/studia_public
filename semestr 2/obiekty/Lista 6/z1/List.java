import java.io.Serializable;

public class List<T> implements Serializable
{
    private class Element implements Serializable
    {
        private static final long serialVersionUID = 6035154233393131997L;  //generated by "serialver -classpath ./ List.Element"
        public T val;
        public Element prev = null;
        public Element next = null;

        public Element(T val)
        {
            this.val = val;
        }
    }

    private static final long serialVersionUID = 1772488282542018999L;      //generated by "serialver -classpath ./ List"
    private Element begin = null;
    private Element end = null;
    private int size = 0;

    public void PushFront(T nval)
    {
        Element temp = new Element(nval);
        temp.val = nval;

        temp.next = begin;
        if (begin != null) begin.prev = temp;
        begin = temp;
        if (end == null) end = temp;
        
        size++;
    }

    public void PushBack(T nval)
    {
        Element temp = new Element(nval);
        temp.val = nval;

        if (end != null) end.next = temp;
        else begin = temp;
        temp.prev = end;
        end = temp;

        size++;
    }

    public T PopFront()
    {
        if (IsEmpty()) return null;

        T temp = begin.val;
        begin = begin.next;
        if (begin != null) begin.prev = null;
        else end = null;

        size--;
        return temp;
    }

    public T PopBack()
    {
        if (IsEmpty()) return null;

        T temp = end.val;
        end = end.prev;
        if (end != null) end.next = null;
        else begin = null;

        size--;
        return temp;
    }

    public boolean IsEmpty()
    {
        return (size == 0);
    }
}