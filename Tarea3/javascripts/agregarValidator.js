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
    let regexCelular = /^(\+?56)?(\s?)(0?9)(\s?)[9876543]\d{7}$/;
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

function agregarFoto(index) {

    let fotos = parseInt(document.getElementById('cantidadFotos' + index).value);

    if (fotos > 4) {
        alert("Solo se puede un maximo de 5 fotos.");
        return;
    }
    // La variable newPhoto la hice para que cada foto agregada tenga un id nuevo
    let newPhoto = '<input id=' + 'inputFA' + fotos + ' type="file" name="fotos-avistamiento"/> <br>';
    let c = document.getElementById("divFotos" + index);
    document.getElementById('cantidadFotos' + index).value = fotos + 1;
    c.innerHTML += newPhoto;


}

let totalAvistamientos = 1;

function agregarAvistamiento() {
    let lugar = document.getElementById('divAvistamientosExtra');
    let inputHorario = '<input id=' + 'inputDHA' + totalAvistamientos + ' type="datetime-local" name="dia-hora-avistamiento" value="" size="20" required="required"/>';
    let inputTipo = '<select id=' + 'inputTA' + totalAvistamientos + ' name="tipo-avistamiento" required="required">';
    let inputEstado = '<select id=' + 'inputEA' + totalAvistamientos + ' name="estado-avistamiento" required="required">';
    let idDivFotos = '<div class="datos informacionAvistamiento" id=' + 'divFotos' + totalAvistamientos + ' >';
    let botonAgregaFoto = '<button id=' + 'agregaFoto' + totalAvistamientos + ' onclick=' + 'agregarFoto(' + totalAvistamientos + ') ' + 'class="boton" >Agregar Foto</button>';
    let cantidadFotos = '<input id=' + 'cantidadFotos' + totalAvistamientos + ' type="hidden" name="cantidad-fotos-avistamiento" value="1"/>';
    let inputFoto = '<input id=' + 'inputFA' + totalAvistamientos + ' type="file" name="fotos-avistamiento"/> <br>';
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
        '        <option value="no sé">No se</option>' +
        '         <option value="vivo">Vivo</option>' +
        '        <option value="muerto">Muerto</option>' +
        '    </select>' +
        ' </div>' +
        idDivFotos +
        '     <div class="instruccion">Fotos:</div>' +
        botonAgregaFoto +
        cantidadFotos +
        '   <br>' +
        inputFoto +
        ' </div>' +
        '  </div>'

    totalAvistamientos += 1;
}

function pedirConfirmacion() {
    if (validar()) {
        let container = document.getElementById('botonesInvisibles');
        container.style.visibility = "visible";
        container.style.display = "block";
    }
}

function esconderConfirmacion() {
    let container = document.getElementById('botonesInvisibles');
    container.style.visibility = "hidden";
    container.style.display = "none";
}

function receive_json() {
    let contenedor = document.getElementById("erroresusuario");
    contenedor.innerHTML = ""

    var form = document.getElementById("formulario");
    var formData = new FormData(form);
    let xhr = new XMLHttpRequest();
    xhr.open('POST', "guardar_avistamiento.py")
    xhr.send(formData);
    xhr.onload = function (data) {
        resp = data.currentTarget.responseText; // responseText es lo que aparece como response en webdev tools
        console.log(resp)
        if(resp.includes('Subido sin errores')) {
            window.location.href = 'index.py'
        }
        else{ // Si entra aqui tiene errores
            contenedor.innerHTML += "<ul>";
            contenedor.innerHTML += resp;
            contenedor.innerHTML += "</ul>";
            contenedor.style.display = "block";
        }
    }
}