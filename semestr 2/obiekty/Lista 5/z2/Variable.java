//package z2;
import java.util.HashMap;

public class Variable extends Expression {
    protected String symbol;
    protected static HashMap<String, Integer> values = new HashMap<String, Integer>();

    public Variable(String symbol) {
        this.symbol = symbol;
    }

    public Variable(String symbol, int value) {
        this.symbol = symbol;
        values.put(symbol, value);
    }

    public static void assignValue(String symbol, int value) {
        values.put(symbol, value);
    }

    public int evaluate() throws IllegalArgumentException {
        if (values.get(symbol) == null) throw new IllegalArgumentException();
        return values.get(symbol);
    }

    public String toString() {
        return symbol;
    }
}