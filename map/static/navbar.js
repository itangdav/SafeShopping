let typearray = [
    ['supermarket', 'Supermarkets'],
    ['doctor', 'Clinics'],
    ['drugstore','Drugstore'],
    ['pharmacy', 'Pharmacy'],
    ['park', 'Parks'],
    ['bank', 'Banks'],
    ['convenience_store', 'Convenience Stores'],
    ['shopping_mall', 'Shopping Malls'],
    ['library', 'Libraries'],
    ['restaurant', 'Restaurants'],
    ['cafe', 'Cafes'],
    ['church', 'Churches'],    
];
  let type = "supermarkets_and_groceries";
  function changeType(event) {
    type = event.target.getAttribute("type");
    console.log(type);
  }

  let navHtml = document.createElement('div');
  navHtml.setAttribute('class', 'topnav');

  for (let count = 0; count < typearray.length; count++) {
    let btn = document.createElement("button");
    btn.setAttribute("type", typearray[count][0]);
    btn.setAttribute("title", typearray[count][1]);
    btn.innerText = typearray[count][1];
    btn.addEventListener("click", changeType);
    navHtml.appendChild(btn);
  }
  document.getElementById("navbar").appendChild(navHtml);