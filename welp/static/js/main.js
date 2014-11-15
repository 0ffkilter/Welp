function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition($.get(
    url="/",
    data = {location : [position.coords.latitude,position.coords.longitude]},
    success = function(data) 
      { alert('page content: ' + data);}););
  } else { 
    window.alert("Can't get your location!");  }
}

