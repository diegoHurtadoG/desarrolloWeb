function loadGraficos() {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '../cgi-bin/estadisticas-graficos.py');
    xhr.timeout = 10000;
    xhr.onload = function (data) {
        let response = data.currentTarget.responseText.replaceAll("\'", "\"");
        let responseJSON = JSON.parse(response); // [[[2, '26-5-2021'], [1, '05-6-2021']], [[2, 'arácnido'], [1, 'miriápodo']], [[2, 'vivo', '5'], [1, 'vivo', '6']]]

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
                xaxis: {ticks: graf_1_ticks, show: true},
                yaxis: {show: true, tickDecimals: 0},
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
        let data_graf_3 = responseJSON[2]; // [2,vivo,5],[4,vivo,6],[1,muerto,6]
        //div.innerHTML += data_graf_3; //  2,vivo,5,4,vivo,6,1,muerto,6
        // Se lee como: 2 vivos en mes 5, 4 vivos en mes 6, 1 muerto en mes 6
        let graf_3_tipo_vivo = [];
        let graf_3_tipo_muerto = [];
        let graf_3_tipo_nose = [];
        for (let i = 1; i < 13; i++) { //Parto de la base que van a ser 12 ticks, por cada mes
            graf_3_tipo_vivo.push([i, 0]);
            graf_3_tipo_muerto.push([i, 0]);
            graf_3_tipo_nose.push([i, 0]);
        }



        for (let i = 0; i < data_graf_3.length; i++) {
            let actual = data_graf_3[i];
            if (actual[1] === "vivo") {
                let numeroMes = actual[2] - 1;
                graf_3_tipo_vivo[numeroMes][1] += actual[0];
            } else if (actual[1] === "muerto") {
                let numeroMes = actual[2] - 1;
                graf_3_tipo_muerto[numeroMes][1] += actual[0];
            } else {
                let numeroMes = actual[2] - 1;
                graf_3_tipo_nose[numeroMes][1] += actual[0];
            }
        }

        $.plot($("#grafico3"),
            [{  data: graf_3_tipo_vivo,
                label: "Vivo",
                bars: {
                    show: true,
                    barWidth: 0.2,
                    align: "left"
                }
            },
            {
                data: graf_3_tipo_nose,
                label: "No Sé",
                bars: {
                    show: true,
                    barWidth: 0.2,
                    align: "right"
                }
            },
            {
                data: graf_3_tipo_muerto,
                label: "Muerto",
                bars: {
                    show: true,
                    barWidth: 0.2,
                    align: "center"
                }
            }
            ],
            {
                legend: {
                    position: "ne",
                    show: true
                },
            }
        );

    };
    xhr.onerror = function () {
        alert('Algo falló D:')
    }
    xhr.send();

}