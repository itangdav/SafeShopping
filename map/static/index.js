

var names = document.getElementById("names").value;
var lats = parseFloat(document.getElementById("lats").value);
var longs = parseFloat(document.getElementById("longs").value);
var scores = parseInt(document.getElementById("scores").value);
var lat = document.getElementById("lat").value;
var longi = document.getElementById("longi").value;

let locations = new Array(names.length);
for(let num = 0; num < names.length; num++){
    locations[num] = [names[num], lats[num], longs[num], scores[num]];
}
let curlat = lat, curlong = longi;
let center = {lat: curlat, lng: curlong};
console.log(center)
console.log(names)
console.log(lats)
console.log(longs)
let map;
function initMap() {
    //sets up the map
    map = new google.maps.Map(document.getElementById('map'), {
        center: center,
        zoom: 14
    });
    let infowindow =  new google.maps.InfoWindow({});
    let marker, count;
    for (count = 0; count < locations.length; count++) {
        let score = parseInt(locations[count][3]/110*255);
        //determines the colour of the marker;
        let str = '';
        let temp1 = Number(2*score).toString(16), temp2 = Number(2*score-255).toString(16);
        if(temp1 == 'NaN')temp1 = '00';
        if(temp2 == 'NaN')temp2 = '00';
        if(score <= 127){
            str += 'FF' + temp1;
            if(str.length < 4)str = str + '0';
        }else{
            str += temp2 + 'FF';
            if(str.length < 4)str = '0' + str;
        }
        str = str + '00';
        //creates a marker at the specified location
        marker = new google.maps.Marker({
          position: new google.maps.LatLng(locations[count][1], locations[count][2]),

            
          map: map,
          //the first hex code determines the colour of the icon.
          icon:'http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=|' + str +'|000000',
          title: locations[count][0],
        });
        //console.log(locations[count][2])
        //console.log(locations[count][1])
        console.log(lat)
        console.log(lats)


        //this string sets up the pop up box when you click on the icon
        let contentString = '<div id="content">'+
        '<div id="siteNotice">'+
        '</div>'+
        '<h1 id="firstHeading" class="firstHeading">' + locations[count][0] + '</h1>'+
        '<div id="bodyContent">'+
        '<p>Safety Score = ' + locations[count][3]
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
