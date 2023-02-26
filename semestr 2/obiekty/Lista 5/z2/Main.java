//package z2;

public class Main {
    public static void main(String[] args) {
        Expression expr = new Multiply(new Variable("x"), new Constant(2));
        Expression expr1 = new Multiply(new Variable("x"), new Add(new Variable("x"), new Constant(5)));
        Expression expr2 = new Add(new Multiply(new Variable("y"), new Variable("y")), new Multiply(expr1, expr));
        Variable.assignValue("x", 5);
        System.out.println(expr.evaluate());
        System.out.println(expr1.evaluate());
        System.out.println(expr2);
        Variable.assignValue("y", 5);
        System.out.println(expr2.evaluate());
    }
}
