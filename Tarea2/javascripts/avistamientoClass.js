class Avistamiento {
    constructor() {
        this.region = "";
        this.comuna = "";
        this.sector = "";
        this.nombreContacto = "";
        this.emailContacto = "";
        this.numeroCelular = "";
        this.horario = "";
        this.tipoAvistamiento = "";
        this.estadoAvistamiento = "";
        this.fotosAvistamiento = [];

        this.information = {
            "Avistamiento": [
                {"Region": this.region},
                {"Comuna": this.comuna},
                {"Sector": this.sector},
                {"Nombre Contacto": this.nombreContacto},
                {"Email Contacto": this.emailContacto},
                {"Numero Celular": this.numeroCelular},
                {"Horario": this.horario},
                {"Tipo Avistamiento": this.tipoAvistamiento},
                {"Estado Avistamiento": this.estadoAvistamiento},
                {"Fotos": this.fotosAvistamiento}
            ]
        }
    }

    constructor(horario, comuna, sector, tipo, fotos) {
        this.comuna = comuna;
        this.sector = sector;
        this.horario = horario;
        this.tipoAvistamiento = tipo;
        this.fotosAvistamiento = fotos; //Aqui falta asegurarse que sea lista
    }

    constructor(horario, comuna, sector, contacto, totalAvistamientos, fotos) {
        this.horario = horario;
        this.comuna = comuna;
        this.sector = sector;
        this.nombreContacto = contacto;
        this.totalAvistamientos = totalAvistamientos;
        this.fotosAvistamiento = fotos;
    }

    constructor(region, comuna, sector, nombreContacto, emailContacto, numeroCelular, horario, tipoAvistamiento, estadoAvistamiento, fotos) {
        this.region = region;
        this.comuna = comuna;
        this.sector = sector;
        this.nombreContacto = nombreContacto;
        this.emailContacto = emailContacto;
        this.numeroCelular = numeroCelular;
        this.horario = horario;
        this.tipoAvistamiento = tipoAvistamiento;
        this.estadoAvistamiento = estadoAvistamiento;
        this.fotosAvistamiento = fotos;
    }
}



function display(avistamiento) {
    lista = document.getElementById('listaDetalles');
    for(let llave in avistamiento){
        lista.innerHTML += '<li class="elemento">' + llave + avistamiento[llave] + '</li>';
    }
}