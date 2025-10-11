let celsius=document.getElementById ("celsius");
let fahrenheit=document.getElementById ("fahrenheit");
let kelvin=document.getElementById ("kelvin");
let reamur=document.getElementById ("reamur");
celsius.oninput = function(){
    let f = (parseFloat(celsius.value) * 9) / 5 + 32;
    fahrenheit.value = parseFloat(f.toFixed(2));
    let k = parseFloat(celsius.value) + 273.15;
    kelvin.value = parseFloat(k.toFixed(2));
    let r = (parseFloat(celsius.value) * 4) / 5;
    reamur.value = parseFloat(r.toFixed(2));
}

fahrenheit.oninput = function(){
    let c = ((parseFloat(fahrenheit.value) - 32) * 5) / 9;
    celsius.value = parseFloat(c.toFixed(2));
    let k = ((parseFloat(fahrenheit.value) - 32) * 5) / 9 + 273.15;
    kelvin.value = parseFloat(k.toFixed(2));
    let r = ((parseFloat(fahrenheit.value) - 32) * 4) / 9;
    reamur.value = parseFloat(r.toFixed(2));
}

kelvin.oninput = function(){
    let f = ((parseFloat(kelvin.value) - 273.15) * 9) / 5 + 32;
    fahrenheit.value = parseFloat(f.toFixed(2));
    let c = parseFloat(kelvin.value) - 273.15;
    celsius.value = parseFloat(c.toFixed(2));
    let r = ((parseFloat(kelvin.value) - 273.15) * 4) / 5;
    reamur.value = parseFloat(c.toFixed(2));
}

reamur.oninput = function(){
    let f = (parseFloat(reamur.value) * 9) / 4 + 32;
    fahrenheit.value = parseFloat(f.toFixed(2));
    let c = (parseFloat(reamur.value) * 5) / 4;
    celsius.value = parseFloat(c.toFixed(2));
    let k = (parseFloat(reamur.value) * 5) / 4 + 273.15; 
    kelvin.value = parseFloat(k.toFixed(2));
}