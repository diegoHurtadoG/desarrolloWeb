<%@ page import="com.cc5002.ejercicio6.Doctor" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!-- HTML5 -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8"/> <!-- Declaring enconding as UTF 8-->
    <title>Auxiliar 8</title> <!-- Title in pestaña -->
    <link rel="stylesheet" type="text/css" media="screen" href="css/index.css"/>    <!-- CSS: -->

</head>
<body>


<ul class="topnav">
    <li><a class="active" href="index.html">Inicio</a></li>
    <li><a href="add_new_doctor.html">Agregar Datos de Médico</a></li>
    <li><a href="list.html">Ver Médicos</a></li>
</ul>
<div>
    <h3>DISCLAIMER: La especialidad sale como numero porque es el valor que tienen el html, para que salga el texto
        tendria que cambiar el value o tratar de hacer un mapeo numero-especialidad</h3>
</div>
<div>
    <!-- Body of page -->
    <h1> Ver Médicos </h1>
    <% Doctor doctor = (Doctor) request.getAttribute("doctor"); %>
    <table>
        <tr>
            <th><% out.println(doctor.getNombre()); %></th>
            <th><% out.println(doctor.getEspecialidad()); %></th>
            <th><% out.println(doctor.getComuna()); %></th>
            <th><% out.println(doctor.getEmail()); %> <br>
                <% out.println(doctor.getCelular()); %> <br>
                <% out.println(doctor.getTwitter()); %></th>
        </tr>
        <!-- First row -->
        <tr>
            <td><a href="medico_jorge_p1.html">Jorge Pérez</a></td>
            <td>Neurología</td>
            <td>Santiago Centro</td>
            <td>jorgeperez@medicina.cl <br>
                @JorgePerez___ <br>
                569 95770936
            </td>
        </tr>
        <!-- Second row -->
        <tr>
            <td>Lucho Matthei</td>
            <td>Cardiología, Gastroenterología</td>
            <td>Ñuñoa</td>
            <td>luismate@yahoo.cl <br>
                569 99370977
            </td>
        </tr>

        <tr>
            <td>Elverto Presli</td>
            <td>Infectología, Epidemiología</td>
            <td>Padre Las Casas</td>
            <td>no.estoy.muerto@hotmail.com <br>

            </td>
        </tr>

        <tr>
            <td>Fulano Kodric</td>
            <td>Psiquiatría</td>
            <td>Chillán</td>
            <td>kodrikc@gmail.com <br>

            </td>
        </tr>

        <tr>
            <td>Juan Cuevas</td>
            <td>Medicina de urgencias, Traumatología</td>
            <td>Concepción</td>
            <td>jcuevas85@gmail.com <br>
                569 97112233

            </td>
        </tr>
    </table>
</div>

</body>
</html>
