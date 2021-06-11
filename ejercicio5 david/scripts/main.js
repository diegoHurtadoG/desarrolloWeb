
function sendForm(){

    let form = document.getElementById("myform");
    let fdata = new FormData(form);
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'cgi-bin/save_doctor.py');
    xhr.timeout = 300;
    xhr.onload = function (data){
        alert('Formulario enviado correctamente :D')
    }
    xhr.onerror = function (){
        alert('Hubo un error, estamos trabajando para solucionarlo :D')
    }
    xhr.send(fdata);
    return false;
}

function loadFromDB(){
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'cgi-bin/doctor_list.py');
    xhr.timeout = 500;
    xhr.onload = function (data){
        let div = document.getElementById("main")
        div.innerHTML += data.currentTarget.responseText
    }
    xhr.onerror = function() {
        alert('Algo falló D:')
    }
    xhr.send()
}