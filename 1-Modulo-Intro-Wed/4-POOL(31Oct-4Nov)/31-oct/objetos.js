/* Script para practicar los objetos en JS */

let obj ={"atributo":"valor del atributo", 
    "nombreDelMetodo": function(){(alert("Mensaje desde médodo"))},
    "otraPropiedad": "Valor de la otra propiedad",
    "escriberAtributos": function(){ console.log("atriburo:" + this.atributo) },
    "escribirOtraPropiedad": function(){ console.log("otraPropiedad: " + this.otraPropiedad) }
}


let calc = {
    "operaciones": " Suma, Resta, Producto, Division",
    "operadores": "+ - * /",
    "suma": function(a,b){ console.log(a+ b) },
    "resta": function(a,b){ console.log(a-b) },
    "prod": function(a,b){ console.log(a*b) },
    "divi": function(a,b){ console.log(a/b) }
}