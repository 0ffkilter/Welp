function sendLocation(position) { 
    success = $.get(
url="/",
data = {"location" : [position.coords.latitude,position.coords.longitude]},
success = function(data) 
{ console.log("success!", position.coords.latitude, position.coords.longitude);
}
);



}


function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(sendLocation);
    
  } else { 
    window.alert("Can't get your location!");  }
}

