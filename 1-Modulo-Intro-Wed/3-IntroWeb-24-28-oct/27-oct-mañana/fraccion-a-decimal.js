/* Script para convertir fracciones en números decimales */

function convertir(){
    let numerador = document.getElementById("myInputA").valueAsNumber;
    let denominador = document.getElementById("myInputB").valueAsNumber;

    if( denominador ===  0 ){ alert("No se puede dividir por cero,\n acaba mal.")
    return ""
}

    let decimales = document.getElementById("decimales").options.selectedIndex;
    let resultado = numerador / denominador

    document.getElementById("resultados").innerText = String(resultado.toFixed(decimales))
}

function borrar() {

let inputA = document.getElementById("myInputA");
let inputB = document.getElementById("myInputB");
let resultado = document.getElementById("resultados");

    myInputA.value = "";
    myInputB.value = "";
    resultado.innerText = "";
}