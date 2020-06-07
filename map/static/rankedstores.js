var names2 = document.getElementById("names").value;
var names = JSON.parse(names2.replace(/'/g, "\""));
var lats = JSON.parse(document.getElementById("lats").value);
var longs = JSON.parse(document.getElementById("longs").value);
var scores = JSON.parse(document.getElementById("scores").value);
var lat = document.getElementById("lat").value;
var longi = document.getElementById("longi").value;

let list = document.getElementById('list');
for(let count = 0; count < names.length; count++){
    let dis = (Math.sqrt(Math.pow(lat - lats[count], 2) + Math.pow(longi - longs[count], 2),2))*111;
    let item = document.createElement('li');
    let itemtext = document.createTextNode(names[count]);
    item.appendChild(itemtext);
    list.appendChild(item);
    console.log(item);
    let info = document.createElement('ul');
    let score = document.createElement('li');
let scoreinfo = document.createTextNode('Safety Score = ' + parseInt(scores[count]));
    score.appendChild(scoreinfo);
    info.appendChild(score);
    let distance = document.createElement('li');
    let distanceinfo = document.createTextNode('Distance = ' + dis.toFixed(2) + 'km');
    distance.appendChild(distanceinfo);
    info.appendChild(distance);
    list.appendChild(info);
    console.log(distance.textContent);
}
