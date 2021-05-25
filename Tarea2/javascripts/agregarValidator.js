// Vamos a empezar con la validacion desde el primer campo hasta el ultimo

function validar() {
    let contenedor = document.getElementById("erroresusuario");
    contenedor.innerHTML = ""
    let errores = [];
    let campoRegion = document.getElementById("regiones");
    let campoComuna = document.getElementById("comunas");
    let campoSector = document.getElementById("inputSector");
    let campoNombre = document.getElementById("inputNombre");
    let campoEmail = document.getElementById("inputEmail");
    let regexEmail = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
    let campoCelular = document.getElementById("inputCelular");
    let regexCelular = /^[+]*[(]{0,1}[0-9]{3}[)]{0,1}[\s/0-9]{9}$/i;
    let campoDHA = document.getElementById("inputDHA");
    let campoTA = document.getElementById("inputTA");
    let campoEA = document.getElementById("inputEA");
    let campoFA = document.getElementsByName("fotos-avistamiento");


    if (campoRegion.value === "sin-region") {
        errores.push("Falta seleccionar la region.");
    }
    if (campoComuna.value === "sin-comuna") {
        errores.push("Falta seleccionar la comuna.");
    }
    if (campoSector.value !== '' && campoSector.value.length > 100) {
        errores.push("El nombre del sector no puede superar los 100 caracteres.");
    }
    if (campoNombre.value.length === 0 || campoNombre.value.length > 200) {
        errores.push("El nombre es obligatorio y debe ser menor a 200 caracteres.");
    }
    if (campoEmail.value.length === 0 || !regexEmail.test(campoEmail.value)) {
        errores.push("El email esta mal escrito.");
    }
    if (campoCelular.value.length !== 0 && !regexCelular.test(campoCelular.value)) {
        errores.push("El celular no cumple con el formato '+569 12345678'");
    }

    if ((campoDHA.value.length === 0)) {
        errores.push("La informacion de tiempo no esta bien escrita.");
    }
    if (campoTA.value === "" || campoEA.value === "") {
        errores.push("Es obligacion seleccionar un tipo y un estado.");
    }

    let noHayFoto = true;
    for (let j = 0; j < campoFA.length; j++) {
        if (campoFA[j].value !== "") {
            noHayFoto = false;
        }
    }
    if (noHayFoto) {
        errores.push("Es requisito agregar minimo 1 foto.")
    }


    if (errores.length > 0) {
        console.log(errores);
        contenedor.innerHTML += "<ul>";
        for (let i = 0; i < errores.length; i++) {
            contenedor.innerHTML += "<li>" + errores[i] + "</li>";
        }
        contenedor.innerHTML += "</ul>";
        contenedor.style.display = "block";
        return false;
    } else {
        //return confirm('Estas seguro que quieres enviar el formulario?');
        return true;
    }
}

let fotos = 1;

function agregarFoto(index) {

    if (fotos > 4) {
        alert("Solo se puede un maximo de 5 fotos.");
        return;
    }
    // La variable newPhoto la hice para que cada foto agregada tenga un id nuevo
    let newPhoto = '<input id=' + 'inputFA' + fotos + ' type="file" name="fotos-avistamiento" value=""/> <br>';
    let c = document.getElementById("divFotos" + index);
    c.innerHTML += newPhoto;
    fotos += 1;

}

let totalAvistamientos = 1;

function agregarAvistamiento() {
    let lugar = document.getElementById('divAvistamientosExtra');
    let inputHorario = '<input id=' + 'inputDHA' + totalAvistamientos + ' type="datetime-local" name="dia-hora-avistamiento" value="" size="20" required="required"/>';
    let inputTipo = '<select id=' + 'inputTA' + totalAvistamientos + ' name="tipo-avistamiento" required="required">';
    let inputEstado = '<select id=' + 'inputEA' + totalAvistamientos + ' name="estado-avistamiento" required="required">';
    let idDivFotos = '<div class="datos informacionAvistamiento" id=' + 'divFotos' + totalAvistamientos + ' >';
    let botonAgregaFoto = '<button id=' + 'agregaFoto' + totalAvistamientos + ' onclick=' + 'agregarFoto(' + totalAvistamientos + ') + >Agregar Foto</button>';
    let inputFoto = '<input id=' + 'inputFA' + totalAvistamientos + ' type="file" name="fotos-avistamiento" value=""/> <br>';
    lugar.innerHTML +=
        '<div class="divInformacionAvistamiento">' +
        ' <div class="datos informacionAvistamiento">' +
        '<div class="instruccion">Dia y Hora:</div>' +
        inputHorario +
        '</div>' +
        ' <div class="datos informacionAvistamiento">' +
        '    <div class="instruccion">Tipo:</div>' +
        inputTipo +
        '     <option value="no sé">No sé</option>' +
        '     <option value="insecto">Insecto</option>' +
        '     <option value="arácnido">Arácnido</option>' +
        '     <option value="miriápodo">Miriápodo</option>' +
        ' </select>' +
        ' </div>' +
        ' <div class="datos informacionAvistamiento">' +
        '     <div class="instruccion">Estado:</div>' +
        inputEstado +
        '        <option value="no sé">No sé</option>' +
        '         <option value="vivo">Vivo</option>' +
        '        <option value="muerto">Muerto</option>' +
        '    </select>' +
        ' </div>' +
        idDivFotos +
        '     <div class="instruccion">Fotos:</div>' +
        botonAgregaFoto +
        '   <br>' +
        inputFoto +
        ' </div>' +
        '  </div>'

    totalAvistamientos += 1;
}

function pedirConfirmacion(){
    if(validar()){
        let container = document.getElementById('botonesInvisibles');
        container.style.visibility="visible";
        container.style.display="block";
    }
}

function esconderConfirmacion(){
    let container = document.getElementById('botonesInvisibles');
    container.style.visibility="hidden";
    container.style.display="none";
}