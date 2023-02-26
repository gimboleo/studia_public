//package z1;

public class PythonProgram extends ComputerProgram {
    public static Tier tier = Tier.D;

    public PythonProgram(String program) {
        prog = program;
    }

    @Override
    public Tier getTier() {
        return PythonProgram.tier;
    }
}
