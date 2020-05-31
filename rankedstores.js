import locations from './getlocation.js';
console.log((locations));
let liststring = '<nav>' + 
'<ul>';

for(let count = 0; count < locations.length; count++){
    //this adds another item to the list.
    liststring = liststring + '<li class = "firstHeading">' + locations[count][0] + 
    ': Safety Score = ' + locations[count][3] + '</li>';
}
console.log(liststring);
//sets the html item to be liststring.
document.getElementById('list').innerHTML = liststring;
