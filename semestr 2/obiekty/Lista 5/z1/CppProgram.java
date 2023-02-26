//package z1;

public class CppProgram extends ComputerProgram {
    protected static Tier tier = Tier.F;

    public CppProgram(String program) {
        prog = new String(program);
    }

    @Override
    public Tier getTier() {
        return CppProgram.tier;
    }
}