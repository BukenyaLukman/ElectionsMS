'use strict'

let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: {lat: 0.347596, lng: 32.582520},
    zoom: 8
  });
}

