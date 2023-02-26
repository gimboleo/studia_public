//package z1;

public class RacketProgram extends ComputerProgram {
    public static Tier tier = Tier.S;
    
    public RacketProgram(String program) {
        prog = new String(program);
    }

    @Override
    public Tier getTier() {
        return RacketProgram.tier;
    }
}
