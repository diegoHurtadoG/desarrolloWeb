class Avistamiento {
    constructor() {
        this.region = "";
        this.comuna = "";
        this.sector = "";
        this.nombreAvistamiento = "";
        this.emailContacto = "";
        this.numeroCelular = "";
        this.horario = "";
        this.tipoAvistamiento = "";
        this.estadoAvistamiento = "";
        this.fotosAvistamiento = [];
    }
    constructor(horario, comuna, sector, tipo, fotos) {
        this.comuna = comuna;
        this.sector = sector;
        this.horario = horario;
        this.tipoAvistamiento = tipo;
        this.fotosAvistamiento = fotos; //Aqui falta asegurarse que sea lista
    }
}