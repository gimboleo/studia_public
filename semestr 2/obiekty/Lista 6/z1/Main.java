import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class Main 
{
    public static void main(String[] args)
    {
        String filename = "file.ser";

        List<String> napisy2 = new List<String>();
        napisy2.PushBack("A");
        napisy2.PushFront("B");
        napisy2.PushBack("C");
        napisy2.PushFront("D");
        napisy2.PushBack("E");
        napisy2.PushFront("F");
        napisy2.PushBack("G");
        napisy2.PushFront("H");  


        try
        {
            FileOutputStream file = new FileOutputStream(filename);
            ObjectOutputStream out = new ObjectOutputStream(file);

            out.writeObject(napisy2);

            out.close();
            file.close();
        }
        catch (IOException exc)
        {
            System.out.println("Serialization failed.");
        }

        napisy2 = null;
        List<?> lista = null;

        try
        {
            FileInputStream file = new FileInputStream(filename);
            ObjectInputStream in = new ObjectInputStream(file);

            lista = (List<?>)in.readObject();

            in.close();
            file.close();
        }
        catch (IOException exc)
        {           
            System.out.println("Deserialization failed.");   
        }
        catch (ClassNotFoundException exc)
        {
            System.out.println("Class not found");
        }


        System.out.println(lista.IsEmpty());       //napisy2: H F D B A C E G
        System.out.println(lista.PopFront());
        System.out.println(lista.PopFront());
        System.out.println(lista.PopFront());
        System.out.println(lista.PopFront());
        System.out.println(lista.PopBack());
        System.out.println(lista.PopBack());
        System.out.println(lista.PopBack());
        System.out.println(lista.PopBack());
        System.out.println(lista.IsEmpty());
        System.out.println(lista.PopBack());       //Lista pusta, funkcja zwroci null
    }
}
