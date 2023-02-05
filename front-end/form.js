var Item = document.getElementById('item');
var Quantity = document.getElementById('quantity');
var units = document.getElementById('units');
var date = document.getElementById('date');
const table = document.querySelectorAll('tbody')[0];

var fridge = [];

function fillTable(dict){
    var quant = dict['Quantity'] + ' ' + dict['Units'];
    let date1 = new Date(dict['Expiration Date']);
    let date2 = new Date();
    let days = Math.floor((date1.getTime() - date2.getTime())/86400000);
    table.innerHTML = table.innerHTML + '<tr><td>' + object['Item'] + '</td><td>' + quant + '</td><td>' + days + '</td></tr';
}

var object = {};

submit.addEventListener('click', function(){
    object['Item'] = item.value;
    object['Quantity'] = quantity.value;
    object['Units'] = units.value;
    object['Expiration Date'] = date.value;
    fillTable(object);
    object = {};
    
})
// table.innerHTML = table.innerHTML + '<tr><td>' + object['Item'] + '</td><td>' + quant + '</td><td>' + days + '</td></tr';

// fillTable(object);

console.log(table.innerHTML);

