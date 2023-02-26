//package z2;

public class Constant extends Expression {
    private int val;

    public Constant(int val) {
        this.val = val;
    }

    public int evaluate() {
        return val;
    }

    public String toString() {
        return Integer.toString(val);
    }
}
