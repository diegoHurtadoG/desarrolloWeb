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
    if (campoSector.value.length > 100) {
        errores.push("El nombre del sector no puede superar los 100 caracteres.");
    }
    if (campoNombre.value.length === 0 || campoNombre.value.length > 200) {
        errores.push("El nombre es obligatorio y debe ser menor a 200 caracteres.");
    }
    if (campoEmail.value.length === 0 || !regexEmail.test(campoEmail.value)) {
        errores.push("El email esta mal escrito.");
    }

    // Validar el formato de celular

    // Validar formato de la fecha
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
    if(noHayFoto){
        errores.push("Es requisito agregar minimo 1 foto.")
    }


    if (errores.length > 0) {
        console.log(errores);
        contenedor.innerHTML += "<ul>";
        for (let i = 0; i < errores.length; i++) {
            contenedor.innerHTML += "<li>" + errores[i] + "</li>";
        }
        contenedor.innerHTML += "</ul>";
        return false;
    }
}

let fotos = 1;

function agregarFoto() {

    if (fotos > 4) {
        alert("Solo se puede un maximo de 5 fotos.");
        return;
    }
    let c = document.getElementById("divFotos");
    c.innerHTML += '<input type="file" name="fotos-avistamiento" value=""/> <br>';
    fotos += 1;

}