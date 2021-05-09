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
 Validacion del formulario
 */
function validacionFormulario() {

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
    let comentario = document.getElementById('comentario');
    if (comentario.value !== '') { // Ya que es opcional
        if (comentario.value.length > 1000) {
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
    return true;

}

console.log('app v1.0'); // stack trace