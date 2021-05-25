/**
 * Imprime error
 * @param {string|number} msg
 */
function mostrarError(msg) {

    let contenedor = document.getElementById('error');

    contenedor.innerHTML = msg;
    contenedor.style.display = 'block';
    contenedor.style.fontWeight = '800';

}

/**
 * Chequea si un número es entero
 * @param value
 * @returns {boolean}
 */
function isInt(value) {
    let x = parseFloat(value);
    return !isNaN(value) && (x | 0) === x;
}

/**
 Envío del formulario
 */
function enviarFormulario() {

    // Este string va concatenando los errores
    let msgError = '';

    /**
     Validacion nombre
     */
    let nombre = document.getElementById('nombre').value;
    let regex = /^[a-zA-Z ]*$/;
    if (nombre.length < 4 || nombre.length > 100 || !regex.test(nombre)) {
        msgError += 'Nombre ';
    }

    /**
     * Validación edad
     */
    let edad = document.getElementById('edad').value;
    if (!isInt(edad) || parseInt(edad) <= 0 || parseInt(edad) > 120) {
        msgError += 'Edad incorrecta '
    }

    /*
    La idea sería ir añadiendo más validaciones aquí, e ir concatenando el mensaje
    de error si es que existe, para al final realizar "mostrarError(mensaje_error_concatenado)".
     */
    /**
     Validacion archivo
     */
    if (document.getElementById('archivo').files.length === 0) {
        msgError += ', Archivo no adjunto ';
    }

    /***
     Validacion comentario
     */
    let comentario = document.getElementById('comentario').value;
    if (comentario !== '') { // Ya que es opcional
        if (comentario.length > 1000) {
            msgError += 'Comentario excede el largo maximo ';
        }
    }

    /**
     Mostramos el error y retornamos el estado de la validacion
     */
    if (msgError.length > 0) {
        mostrarError('Tu formulario fallo en: ' + msgError);
        return false;
    }

    /**
     * Envío de ajax
     */
    console.log('Enviado formulario');
    let data = new FormData();
    data.append('nombre', nombre);
    data.append('edad', edad);
    data.append('file', document.getElementById('archivo').files[0]);
    data.append('comentario', comentario);

    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'hackbox_response.py', true);
    xhr.timeout = 300;
    xhr.onload = function (data) {
        alert('Enviado correctamente!');
        console.warn(data.currentTarget.responseText);
    };
    xhr.onerror = function () {
        mostrarError('No se pudo enviar el mensaje');
    }

    xhr.send(data);
    return false;

}

console.log('app v1.0');