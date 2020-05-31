import locations from './getlocation.js';
let liststring = '<nav>' + 
'<ul>';

/*for(let count = 0; count < locations.length; count++){
    //this adds another item to the list.
    liststring = liststring + '<li class = "firstHeading">' + locations[count][0] + 
    ': Safety Score = ' + locations[count][3] + '</li>';
}*/
//sets the html item to be liststring.
document.getElementById('list').innerHTML = liststring;
