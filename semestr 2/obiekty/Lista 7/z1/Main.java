import javax.swing.*;

public class Main 
{
    @SuppressWarnings("unused")

    public static void main(String[] args) throws IllegalArgumentException
    {
        if (args.length != 2) throw new IllegalArgumentException("Wrong input");
        if (!(args[1].equals("Circle") || args[1].equals("Triangle"))) throw new IllegalArgumentException("There is no such class as " + args[1]);

        JFrame frame = new JFrame("Editor");
        String path = args[0];
        FigureEdit editor;

        if (args[1].equals("Circle")) editor = new CircleEdit(frame, path);
        else editor = new TriangleEdit(frame, path);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.pack();
    }
}
