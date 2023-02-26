//package z1;

public class OrderedList<E extends Comparable<E>> {
    protected class Element {
        public E val;
        public Element next;

        public Element(E value) {
            val = value;
            next = null;
        }
    }

    public OrderedList() {
        head = null;
    }

    protected Element head;
    
    public void add(E elem) {
        // 1. pusta
        if (head == null) {
            head = new Element(elem);
            return;
        }
        // 2. na początek
        // elem < head.val
        Element inserted = new Element(elem);

        if (elem.compareTo(head.val) < 0) {
            inserted.next = head;
            head = inserted;
        }
        // 3. środek/koniec (to samo)
        else {
            Element curr = head;

            while (curr.next != null && elem.compareTo(curr.next.val) >= 0) {
                curr = curr.next;
            }
            
            // wstawiany za curr
            inserted.next = curr.next;
            curr.next = inserted;
        }

    }

    public E getFirst() {
        return head.val;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("[ ");
        Element temp = head;
        Boolean first = true;

        while (temp != null) {
            if (first) {
                sb.append("\"");
                sb.append(temp.val);
                sb.append("\"");
                first = false;
            } else {
                sb.append(", \"");
                sb.append(temp.val);
                sb.append("\"");
            }
            temp = temp.next;
        }

        return sb.append(" ]").toString();
    }
}