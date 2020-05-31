let locations = [
    ['Metro', 43.666709, -79.404155, 100],
    ['Whole Foods', 43.672023, -79.394915, 0]
];
let curlat = 43.667665, curlong = -79.399636;
let center = {lat: curlat, lng: curlong};
let map;
console.log('ok');
function initMap() {
    console.log('ok');
    //sets up the map
    map = new google.maps.Map(document.getElementById('map'), {
        center: center,
        zoom: 14
    });
    let infowindow =  new google.maps.InfoWindow({});
    let marker, count;
    for (count = 0; count < locations.length; count++) {
        //creates a marker at the specified location
        marker = new google.maps.Marker({
          position: new google.maps.LatLng(locations[count][1], locations[count][2]),
          map: map,
          //the first hex code determines the colour of the icon.
          icon:'http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=|FFFFFF|000000',
          title: locations[count][0],
        });
        //this string sets up the pop up box when you click on the icon
        let contentString = '<div id="content">'+
        '<div id="siteNotice">'+
        '</div>'+
        '<h1 id="firstHeading" class="firstHeading">' + locations[count][0] + '</h1>'+
        '<div id="bodyContent">'+
        '<p>Safety Score = '+
        '</p>'+
        '</div>'+
        '</div>';
        //this implements the clicking on the icon action.
        google.maps.event.addListener(marker, 'click', (function (marker, count) {
            return function () {
            infowindow.setContent(contentString);
            infowindow.open(map, marker);
          }
        })(marker, count));
    }
}
