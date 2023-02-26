//package z1;

public class JavaProgram extends ComputerProgram {
    public static Tier tier = Tier.C;

    public JavaProgram(String program) {
        prog = new String(program);
    }

    @Override
    public Tier getTier() {
        return JavaProgram.tier;
    }
}
