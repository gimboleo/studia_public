//package z1;

public class CProgram extends ComputerProgram {
    protected static Tier tier = Tier.S;

    public CProgram(String program) {
        prog = new String(program);
    }

    @Override
    public Tier getTier() {
        return CProgram.tier;
    }
}
