//package z1;

public abstract class ComputerProgram implements Comparable<ComputerProgram> {
    protected enum Tier {
        S, A, B, C, D, E, F;
    }

    protected String prog;

    @Override
    public int compareTo(ComputerProgram program) {
        if (this.getTier() == program.getTier()) {
            return this.prog.compareTo(program.prog);
        } else {
            return this.getTier().ordinal() - program.getTier().ordinal();
        }
    }

    @Override
    public String toString() {
        return prog;
    }

    public abstract Tier getTier();
}