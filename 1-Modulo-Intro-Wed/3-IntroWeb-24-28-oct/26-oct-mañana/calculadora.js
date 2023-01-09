/* Calculadora */ 
function calc(){    
    let numA = document.getElementById("myInputA")
    let numB = document.getElementById("myInputB")

     numA = numA.valueAsNumber //número
     numB = numB.valueAsNumber //número

 

  // Tomar valores del select cuando se llame calc()
  let operacionesSel = document.getElementById("operaciones") // select
  // let posicion = operacionesSel.options.selectedIndex // equivalente a la sig líres
  let posicion = operacionesSel.options['selectedIndex'] // entero, posición en array
  // posicion -> 0 es Suma, 1 es Resta ... 6 es Logaritmo 10
  
  // Llamar a la fn seleccionada
    if( posicion === 0 ){
        let res = suma(numA, numB)
        EscribirResultado(res)
        console.log("Suma: " + res)
    } else if( posicion === 1 ){
        let res = resta(numA, numB)
        EscribirResultado(res)
        console.log("Resta: " + res)
    } else if( posicion === 2 ){
        let res = producto(numA, numB)
        EscribirResultado(res)
        console.log("Prod: " + res)
    } else if( posicion === 3 ){
        let res = division(numA, numB)
        EscribirResultado(res)
        console.log("División: " + res)
    } else if( posicion === 4 ){
        let res = raizCuadrada(numA)
        EscribirResultado(res)
        console.log("Raíz: " + res)
    } else if( posicion === 5 ){
        let res = potencia(numA, numB)
        EscribirResultado(res)
        console.log("Pow: " + res)
    } else {
        let res = log10(numA)
        EscribirResultado(res)
        console.log("Log10: " + res)
    }
  
  // Escribir el resultado en textarea

}
  // Fn para escribir un dato en el textarea
function 
EscribirResultado(num){ 
    let textarea = document.getElementById("resultados")
    textarea.innerText = String(num)
}
    // Funciones para operaciones básicas + - * / ** % sqrt() log() 
    //suma
function suma(a, b){
    return a + b;
}
    //resta
function resta(a, b){
    return a - b;
}
    //producto
function producto(a, b){
    return a * b;
}
    //division
function division(a, b){
    if( b === 0){
        alert("No se puede dividir por 0")
        return NaN;
    }
    return a / b;
}
    // Raíz cuadrada -> Math.sqrt(num)
function raizCuadrada(num){
    if( num < 0){
        alert("No existe la raíz cuadrada de número negativos")
        return NaN;
    }
    return Math.sqrt(num);
}
    // Potencia -> Math.pow(base, exponente)
function potencia(base, exponente){
    if( base === 0 & exponente === 0 ){
        alert("0 elevado a 0 es indeterminado")
        return NaN;
    }
    return Math.pow(base, exponente);
}
    // Log -> Math.log(num)
function log10(num){
    if( num <= 0 ) {
        alert("No existe log para números no positivos")
        return NaN;
    }
    return Math.log10(num);
}
    // Botones para realizar cálculos

    // inputs para ingresar datos

    // Estilos

