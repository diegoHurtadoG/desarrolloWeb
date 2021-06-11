package cc5002.model;

public class HackBox {

    private final String nombre;
    private final String apellido;
    private final String select;

    public HackBox(String nombre, String contrasena, String select) {
        this.nombre = nombre;
        this.apellido = contrasena;
        this.select = select;
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public String getSelect() {
        return select;
    }
}
