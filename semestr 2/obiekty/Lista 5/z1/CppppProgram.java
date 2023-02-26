//package z1;

public class CppppProgram extends ComputerProgram {
    protected static Tier tier = Tier.A;

    public CppppProgram(String program) {
        prog = new String(program);
    }

    @Override
    public Tier getTier() {
        return CppppProgram.tier;
    }
}
