package com.cc5002.ejercicio6;

import com.cc5002.ejercicio6.Doctor;

import java.io.*;
import jakarta.servlet.*;
import jakarta.servlet.http.*;


public class SaveDoctor extends HttpServlet {

    public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String region = request.getParameter("region-medico");
        String comuna = request.getParameter("comuna-medico");
        String nombre = request.getParameter("nombre-medico");
        String experiencia = request.getParameter("experiencia-medico");
        String especialidades = request.getParameter("especialidades-medico");
        String twitter = request.getParameter("twitter-medico");
        String email = request.getParameter("email-medico");
        String celular = request.getParameter("celular-medico");

        Doctor doctor = new Doctor(nombre, experiencia, region, comuna, especialidades, twitter, email, celular);

        request.setAttribute("doctor", doctor);
        request.getRequestDispatcher("list.jsp").forward(request, response); // AQUI FALTA PONER EL JSP

    }

}