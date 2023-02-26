import java.io.Serializable;

public abstract class Figure implements Serializable
{
    String name;

    public abstract boolean read(String path);
    public abstract boolean write(String path);
    public abstract String toString();

    public void set_name(String name)
    {
        this.name = name;
    }

    public String get_name()
    {
        return this.name;
    }    
}