
//First argument is day number 0-4
//Second argument is function, see example
function getWeatherForDay(num, callback) {
      var my_city="Edinburgh, UK";
      var my_key="597e7211f7122344131802";
      var no_of_days=5;
      var uri="http://free.worldweatheronline.com/feed/weather.ashx?q="+my_city+"&key="+my_key+"&format=json&no_of_days="+no_of_days+"&includeLocation=yes&callback=?";
      uri=encodeURI(uri); 
      var x = jQuery.get(uri,function(r){
        if (r.data.error) {
          document.write(r.data.error[0].msg);
        }
        else {
         if (r.data.current_condition[num].precimMM < 2){
            good = true;
         }
         else {
            good = false;
         }
         callback({temp_F: r.data.current_condition[num].temp_F, 
                temp_C: r.data.current_condition[num].temp_C,
                condition: r.data.current_condition[num].weatherDesc[0].value,
                max_temp_F : r.data.weather[num].tempMaxF,
                max_temp_C : r.data.weather[num].tempMaxC,
                min_temp_F : r.data.weather[num].tempMinF,
                min_temp_C : r.data.weather[num].tempMinC,
                humidity : r.data.current_condition[num].humidity,
                precipitation : r.data.current_condition[num].precipMM,
                pressure : r.data.current_condition[num].pressure,
                wind_speed_kmph : r.data.current_condition[num].windspeedKmph,
                wind_speed_mph : r.data.current_condition[num].windspeedMiles,
                wind_dir : r.data.current_condition[num].winddirDegree,
                img : r.data.current_condition[num]["weatherIconUrl"][0].value,
                prediction : good 
                });
         }
      }, "json");
}



