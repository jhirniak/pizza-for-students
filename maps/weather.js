function weatherStats() {
      var my_city="Edinburgh, UK";
      var my_key="597e7211f7122344131802";
      var no_of_days=2;
      var uri="http://free.worldweatheronline.com/feed/weather.ashx?q="+my_city+"&key="+my_key+"&format=json&no_of_days="+no_of_days+"&includeLocation=yes&jsoncallback=?";
      uri=encodeURI(uri); 
      jQuery.get(uri,function(r){
      if(r.data.error) {
        alert(r.data.error[0].msg);
      }
      else {
        nearest_area = r.data.nearest_area[0].region[0].value;
        country = r.data.nearest_area[0].country[0].value;
        current_temp_F = r.data.current_condition[0].temp_F;
        current_temp_C = r.data.current_condition[0].temp_C;
        current_condition = r.data.current_condition[0].weatherDesc[0].value;
        max_temp_F = r.data.weather[0].tempMaxF;
        min_temp_F = r.data.weather[0].tempMinF;
        max_temp_C = r.data.weather[0].tempMaxC;
        min_temp_C = r.data.weather[0].tempMinC;
        humidity = r.data.current_condition[0].humidity;
        precipitation = r.data.current_condition[0].precipMM;
        pressure = r.data.current_condition[0].pressure;
        wind_speed_kmph = r.data.current_condition[0].windspeedKmph;
        wind_speed_mph = r.data.current_condition[0].windspeedMiles;
        wind_dir = r.data.current_condition[0].winddirDegree;
        current_img = r.data.current_condition[0].weatherIconUrl.value;
        return(r.data.current_condition[0].temp_C);
      }
    },"json");
}

