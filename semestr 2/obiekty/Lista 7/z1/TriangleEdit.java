import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.File;

public class TriangleEdit extends FigureEdit 
{
    private Triangle triangle;
    private JTextField[] x;
    private JTextField[] y;
    private JTextField name;
    private String path;

    public TriangleEdit(JFrame frame, String path)
    {
        this.triangle = new Triangle();
        this.path = path;

        //Ten kod zapobiega otwarciu pliku zawierajacego obiekt innej klasy, niz podal uzytkownik
        //Dodatkowo jesli plik nie istnieje, program nawet nie podejmuje sie otwierania go,
        //uzytkownik otrzyma obiekt z konstruktora domyslnego
        if (new File(path).isFile())
        {
            if (!this.triangle.read(this.path)) throw new IllegalArgumentException("Given object is not a triangle: " + path);
        }

        this.cont = frame.getContentPane();

        this.name = new JTextField(this.triangle.get_name());
        this.x = new JTextField[3];
        this.y = new JTextField[3];

        for (int i = 0; i < 3; i++)
        {
            this.x[i] = new JTextField(Double.toString(this.triangle.get_x(i)));
            this.y[i] = new JTextField(Double.toString(this.triangle.get_y(i)));
        }

        JButton save = new JButton("Save object");
        save.addActionListener(this);

        cont.setPreferredSize(new Dimension(640, 240));
        cont.setLayout(new GridLayout(5, 3));

        cont.add(new JLabel("Name: "));
        cont.add(this.name);
        cont.add(new JLabel(""));
        cont.add(new JLabel(""));

        for (int i = 0; i < 3; i++)
        {
        cont.add(new JLabel("(x" + i +", y" + i + "): "));
        cont.add(this.x[i]);
        cont.add(this.y[i]);
        cont.add(new JLabel(""));
        }

        cont.add(new JLabel(""));
        cont.add(save);
    }

    private void update(String name, double[] x, double[] y)
    {
        this.triangle.set_name(name);
        for (int i = 0; i < 3; i++) this.triangle.set_point(i, x[i], y[i]);
    }

    public void actionPerformed(ActionEvent e)
    {
        String name;
        double[] x = new double[3];
        double[] y = new double[3];

        try
        {
            name = this.name.getText();
            for (int i = 0; i < 3; i++)
            {
                x[i] = Double.parseDouble(this.x[i].getText());
                y[i] = Double.parseDouble(this.y[i].getText());
            }

            if (!Triangle.are_valid(x, y)) throw new IllegalArgumentException("These 3 points can't make a triangle: " +
                                                                            "(" + x[0] + ", " + y[0] + "); " +
                                                                            "(" + x[1] + ", " + y[1] + "); " +
                                                                            "(" + x[2] + ", " + y[2] + ")");

            update(name, x, y);
            this.triangle.write(path);
        }
        catch (Exception ex)
        {
            JFrame frame = new JFrame();
            JOptionPane.showMessageDialog(frame, ex.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        }
    } 
}
