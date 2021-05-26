function rowHandler(element){
    window.open(src='detalleAvistamiento.py', "_self");
}

function zoomear(imagen) {
    if (imagen.width == 320 && imagen.height == 240) {
        imagen.width = 800;
        imagen.height = 600;
    } else {
        imagen.width = 320;
        imagen.height = 240;
    }
}