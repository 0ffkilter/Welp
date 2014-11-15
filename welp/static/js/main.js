function sendLocation(location) { 
    success = $.get(
url="/",
data = {location : [position.coords.latitude,position.coords.longitude]},
success = function(data) 
{ alert('page content: ' + data);
}
);



}


function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(sendLocation);
    
  } else { 
    window.alert("Can't get your location!");  }
}

