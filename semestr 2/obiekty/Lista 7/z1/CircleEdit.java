import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.File;

public class CircleEdit extends FigureEdit 
{
    private Circle circle;
    private JTextField radius;
    private JTextField x;
    private JTextField y;
    private JTextField name;
    private String path;

    public CircleEdit(JFrame frame, String path) throws IllegalArgumentException
    {
        this.circle = new Circle();
        this.path = path;

        //Ten kod zapobiega otwarciu pliku zawierajacego obiekt innej klasy, niz podal uzytkownik
        //Dodatkowo jesli plik nie istnieje, program nawet nie podejmuje sie otwierania go,
        //uzytkownik otrzyma obiekt z konstruktora domyslnego
        if (new File(path).isFile())
        {
            if (!this.circle.read(this.path)) throw new IllegalArgumentException("Given object is not a circle: " + path);
        }

        this.cont = frame.getContentPane();

        this.name = new JTextField(this.circle.get_name());
        this.radius = new JTextField(Double.toString(this.circle.get_r()));
        this.x = new JTextField(Double.toString(this.circle.get_x()));
        this.y = new JTextField(Double.toString(this.circle.get_y()));

        JButton save = new JButton("Save object");
        save.addActionListener(this);

        cont.setPreferredSize(new Dimension(640, 240));
        cont.setLayout(new GridLayout(4, 3));

        cont.add(new JLabel("Name: "));
        cont.add(this.name);
        cont.add(new JLabel(""));

        cont.add(new JLabel("Radius: "));
        cont.add(this.radius);
        cont.add(new JLabel(""));

        cont.add(new JLabel("(x, y): "));
        cont.add(this.x);
        cont.add(this.y);
        cont.add(new JLabel(""));

        cont.add(save);
    }

    private void update(String name, double r, double x, double y)
    {
        this.circle.set_name(name);
        this.circle.set_r(r);
        this.circle.set_x(x);
        this.circle.set_y(y);
    }

    public void actionPerformed(ActionEvent e)
    {
        String name;
        double r;
        double x;
        double y;

        try
        {
            name = this.name.getText();
            r = Double.parseDouble(this.radius.getText());
            x = Double.parseDouble(this.x.getText());
            y = Double.parseDouble(this.y.getText());

            update(name, r, x, y);
            this.circle.write(path);
        }
        catch (Exception ex)
        {
            JFrame frame = new JFrame();
            JOptionPane.showMessageDialog(frame, ex.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        }
    } 
}
