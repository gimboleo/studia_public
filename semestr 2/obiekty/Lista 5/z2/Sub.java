//package z2;

public class Sub extends Expression {
    protected Expression l;
    protected Expression r;

    public Sub(Expression left, Expression right) {
        l = left;
        r = right;
    }
    
    public int evaluate() {
        return l.evaluate() - r.evaluate();
    }
    
    @Override
    public String toString() {
        return "(" + l.toString() + " - " + r.toString() + ")"; 
    }
}
