function show_map(map) {
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1
    }).addTo(map);
}

// L.marker([51.5, -0.09]).addTo(mymap); // Con esto agrego un marker en coordenadas

function show_markers(map, info) {
    for (let i = 0; i < info.length; i++) {
        L.marker([info[i][8], info[i][7]], {title: info[i][0]}).addTo(map)
            .bindPopup("<b> Avistamientos en: " + info[i][0] + "</b></br>" +
            "<ul>" +
                "<li>" +
                "Fecha: "+ info[i][3] +
                "</li>" +
                "<li>" +
                "Tipo: " + info[i][4] +
                "</li>" +
                "<li>" +
                "Estado: " + info[i][5] +
                "</li>" +
                "<li>" +
                "Foto(s): <img src=." + info[i][6] + " width='60px' height='60px'>" +
                "</li>" +
                "<li>" +
                "<button class='boton' onclick='location.href=" + '"detalleAvistamiento.py";' + "'>Ver Mas</button>" +
                "</li>" +
                "</ul>");
    }
}

function show_data() {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '../cgi-bin/map-data.py', true);
    xhr.timeout = 10000;
    xhr.onload = function (data) {
        let div = document.getElementById("main")
        let response = data.currentTarget.responseText.replaceAll("\'", "\"");
        let responseJSON = JSON.parse(response);
        //console.log(responseJSON);

        let mymap = L.map('mapid').setView([-35, -75], 3);
        show_map(mymap);
        show_markers(mymap, responseJSON);
    };
    xhr.send();
}