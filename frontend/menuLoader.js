var mlParent,
    mlObjData,
    mlFirstDate,
    mlWidth;

var mlScriptNum = 4,
    mlScriptDone = 0;

function loadMenu(parent, object, firstDate, width)
{
    genObject();
    fixObject(mlObjData);
    $.getScript("slider.js", mlLoaded);
    $.getScript("sliderContent.js", mlLoaded);
    $.getScript("menu.js", mlLoaded);
    $.getScript("table.js", mlLoaded);

    mlParent = parent;
    //mlObjData = object;
    mlFirstDate = firstDate;
    mlWidth = width;
}

function fixObject(o) {
    for (var di = 0; di < o.length; di++) {

        o[di].path = o[di].path.map(function (d) {
            return { size: d.size, name: d.name, objects: d.objects, position: 0 };
        });
        for (var i = 1; i < o[di].path.length; i++)
            o[di].path[i].position = o[di].path[i - 1].position + o[di].path[i - 1].size;

    }
    //alert('fixd');
    fillWeatherForDay(o);
}

function mlLoaded() {
    mlScriptDone++;
    if (mlScriptDone == mlScriptNum) {
        createBar(mlParent, mlObjData, mlFirstDate, mlWidth);
    }
}

function fillWeatherForDay(o) {
    var my_city = "Edinburgh, UK";
    var my_key = "597e7211f7122344131802";
    var no_of_days = 5;
    var uri = "http://free.worldweatheronline.com/feed/weather.ashx?q=" + my_city + "&key=" + my_key + "&format=json&no_of_days=" + no_of_days + "&includeLocation=yes&callback=?";
    uri = encodeURI(uri);
    var x = jQuery.get(uri, function (r) {
        if (r.data.error) {
            alert(r.data.error[0].msg);
        }
        else {
            for (var i = 0; i < o.length; i++) {
                //-20 to 40 celsius
                o[i].weather = ((r.data.current_condition[i].tempMinC + r.data.current_condition[i].tempMaxC) / 2 + 20) / 60;
            }
            //alert(r.data.current_condition[num].temp_C);
            //return r.data.current_condition[num].temp_C;
            //return {
            //    temp_F: r.data.current_condition[num].temp_F,
            //    temp_C: r.data.current_condition[num].temp_C,
            //    condition: r.data.current_condition[num].weatherDesc[0].value,
            //    max_temp_F: r.data.weather[num].tempMaxF,
            //    max_temp_C: r.data.weather[num].tempMaxC,
            //    min_temp_F: r.data.weather[num].tempMinF,
            //    min_temp_C: r.data.weather[num].tempMinC,
            //    humidity: r.data.current_condition[num].humidity,
            //    precipitation: r.data.current_condition[num].precipMM,
            //    pressure: r.data.current_condition[num].pressure,
            //    wind_speed_kmph: r.data.current_condition[num].windspeedKmph,
            //    wind_speed_mph: r.data.current_condition[num].windspeedMiles,
            //    wind_dir: r.data.current_condition[num].winddirDegree,
            //    img: r.data.current_condition[num]["weatherIconUrl"][0].value
            //};
        }
    }, "json");
}



function genObject() {
    mlObjData = [{ //day 0
        weather: 0.1,
        path:
        [
            { //path 0
                size: 3,
                name: 'Path A',
                objects:
                [
                    {
                        name: 'objAA',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objAB',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objAC',
                        desc: 'tup obekt'
                    }
                ]
            },
            { //path 0
                size: 4,
                name: 'Path B',
                objects:
                [
                    {
                        name: 'objBA',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objBB',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objBC',
                        desc: 'tup obekt'
                    }
                ]
            },
            { //path 0
                size: 3,
                name: 'Path C',
                objects:
                [
                    {
                        name: 'objCA',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objCB',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objCC',
                        desc: 'tup obekt'
                    }
                ]
            }
        ]
    },
    { //day 0
        weather: 0.5,
        path:
        [
            { //path 0
                size: 3,
                name: 'Path A',
                objects:
                [
                    {
                        name: 'objAA',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objAB',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objAC',
                        desc: 'tup obekt'
                    }
                ]
            },
            { //path 0
                size: 3,
                name: 'Path A',
                objects:
                [
                    {
                        name: 'objAA',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objAB',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objAC',
                        desc: 'tup obekt'
                    }
                ]
            },
            { //path 0
                size: 3,
                name: 'Path A',
                objects:
                [
                    {
                        name: 'objAA',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objAB',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objAC',
                        desc: 'tup obekt'
                    }
                ]
            }
        ]
    },
    { //day 0
        weather: 0.9,
        path:
        [
            { //path 0
                size: 1,
                name: 'Path A',
                objects:
                [
                    {
                        name: 'objAA',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objAB',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objAC',
                        desc: 'tup obekt'
                    }
                ]
            },
            { //path 0
                size: 5,
                name: 'Path A',
                objects:
                [
                    {
                        name: 'objAA',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objAB',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objAC',
                        desc: 'tup obekt'
                    }
                ]
            },
            { //path 0
                size: 3,
                name: 'Path A',
                objects:
                [
                    {
                        name: 'objAA',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objAB',
                        desc: 'tup obekt'
                    },
                    {
                        name: 'objAC',
                        desc: 'tup obekt'
                    }
                ]
            }
        ]
    }]
}