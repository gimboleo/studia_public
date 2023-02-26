//package z1;

public class Main {
    public static void main(String[] args) {
        OrderedList<ComputerProgram> list = new OrderedList<ComputerProgram>();

        list.add(new RacketProgram("(define no yes)"));
        list.add(new JavaProgram("public static void main(String args[]) { System.out.println(\"Java\"); }"));
        list.add(new CProgram("piekny czysty C"));
        list.add(new CppProgram("cukierek kaszankowy"));
        list.add(new CppppProgram("Java but better but not Java"));
        list.add(new RacketProgram("(define yes no)"));
        list.add(new CppProgram("paczek z salcesonem"));
        list.add(new PythonProgram("lambda L: [] if L==[] else qsort([x for x in L[1:] if x< L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])"));
        list.add(new RacketProgram("(define aaaaaaaaaaaa +)"));

        System.out.println(list);
    }
}