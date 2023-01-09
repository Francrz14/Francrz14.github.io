console.log("Ejercicio 2")
console.log("-----------")

/* Suma */
let suma = document.getElementById("suma")//<p id="suma"   class="inline">Suma: </p>
let a = Number(prompt("Introduce primer operando"))
let b = Number(prompt("Introduce segundo operando"))
let resultado = a + b
console.log("suma: " + resultado)
suma.innerText += resultado
//      suma.innerText = suma.innerText + resultado

    /*****************************/
    

/*resta */
let resta = document.getElementById("resta")//<p id="resta" class="inline">Resta: </p>
a = Number(prompt("Introduce primer operando"))
b = Number(prompt("Introduce segundo operando"))
resultado = a - b
console.log("resta: " + resultado)
resta.innerText += resultado

/*prod*/
let prod = document.getElementById("prod")//<p id="prod"  class="inline">Producto: </p>
a = Number(prompt("Introduce primer operando"))
b = Number(prompt("Introduce segundo operando"))
resultado = a * b
console.log("prod: " + resultado)
prod.innerText += resultado

/*divi*/
let divi = document.getElementById("divi")//<p id="divi"  class="inline">División: </p>
a = Number(prompt("Introduce primer operando"))
b = Number(prompt("Introduce segundo operando"))
resultado = a / b
console.log("divi: " + resultado)
divi.innerText += resultado