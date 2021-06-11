function loadGraficos() {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '../cgi-bin/estadisticas-graficos.py');
    xhr.timeout = 10000;
    xhr.onload = function (data) {
        let div = document.getElementById("main")
        //div.innerHTML += data.currentTarget.responseText
        //console.log(data.currentTarget.responseText); // No imprime pero en webdev tools, response del .py, se ve lo que da
        // Aqui si puedo hacer por ejemplo:
        // let ejemplo = document.getElementById("estadistica1"); // Siendo estadistica1 un id que se agrega en linea 7
        let response = data.currentTarget.responseText.replaceAll("\'", "\"");
        let responseJSON = JSON.parse(response); // [[[2, '26-5-2021'], [1, '05-6-2021']], [[2, 'arácnido'], [1, 'miriápodo']], [[2, 'vivo', '5'], [1, 'vivo', '6']]]
        //div.innerHTML += responseJSON[0]; // Esto es [[2, '26-5-2021'], [1, '05-6-2021']], lo pasa sin parentesis
        //div.innerHTML += responseJSON[0][0]; // Esto seria [2, '26-5-2021'], lo pasa sin parentesis
        //div.innerHTML += responseJSON[0][0][0]; // Bueno y esto es 2

        // GRAFICO 1
        let data_graf_1 = responseJSON[0];
        let graf_1_ticks = []; // Aqui vamos a ir guardando [tick, fecha]
        let graf_1_info = []; // Aqui vamos a ir guardando [tick, numero]
        for (let i = 0; i < data_graf_1.length; i++) {
            let elem = data_graf_1[i];
            graf_1_info.push([i, elem[0]]);
            graf_1_ticks.push([i, elem[1]]);
        }

        $.plot($("#grafico1"), [graf_1_info],
            {
                xaxis: {ticks: graf_1_ticks, show: true, axisLabel: 'Fecha'},
                yaxis: {show: true, axisLabel: 'Numero de informados', tickDecimals: 0},
                series: {color: "cyan", lines: {show: true}, points: {show: true}}
            });

        // GRAFICO 2
        let data_graf_2 = responseJSON[1]; // [[2, 'arácnido'], [1, 'miriápodo']]
        let graf_2_pie_data = [];
        for (let i = 0; i < data_graf_2.length; i++) {
            graf_2_pie_data[i] = {
                label: data_graf_2[i][1],
                data: data_graf_2[i][0]
            }
        }
        $.plot($("#grafico2"), graf_2_pie_data,
            {
                series: {
                    pie: {
                        show: true,
                        label: {
                            show: true,
                            formatter: function (label, series) { // https://stackoverflow.com/questions/27883284/jquery-flot-pie-chart-label-formatting
                                let number = series.data[0][1]; // this is the y value of the first point
                                return ('&nbsp;<b>' + label + '(s): </b>' + number); // custom format
                            },
                        }
                    }
                }
            });

        // GRAFICO 3
        let data_graf_3 = responseJSON[2];
        let graf_3_tipo_1 = [],


    }
    xhr.onerror = function () {
        alert('Algo falló D:')
    }
    xhr.send()

}
// Para agregar los graficos puedo hacer una funcion que recibe el json de la info
// y para que se imprima el grafico, si no funciona tal como la de arriba, puedo ver si es factible
// agregarlo a la mala con document.getElementById().innerHTML += grafico