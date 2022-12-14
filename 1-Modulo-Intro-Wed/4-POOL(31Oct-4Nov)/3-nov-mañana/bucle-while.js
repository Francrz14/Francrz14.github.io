// Script para hacer ejercicios de bucle While

// 1. Imprimir lista de números de 0 o 1 a N (número introducido por usuario)
    function ej1() {
    let el = document.getElementById("ej-1-resultados");
    let n = document.getElementById("input-1").valueAsNumber;
    let i = 0;
    let res = "";
    while( i < n ){
    res += i + ", ";
    i++;
    }
    el.innerText = res;
}
// 2. Se pide número en rango y se sigue pidiendo hasta recibirlo
    function ej2() {
    let el = document.getElementById("ej-2-resultados");
    let num = document.getElementById("input-2").valueAsNumber;
    let i = 0;
    let rango = 10;
    let res = 0;
    if(num < rango){
        res = "Número de rango"
    } else {
        res = "Número no está en rango"
    }
    el.innerText = res;
}
// 3. Se pregunta si continuamos programa -> n o N cierran bucle
    function ej3(){
    let el = document.getElementById("ej-3-resultados");
    el.innerText = "Has iniciado el programa."
    let bool = true; // implica continuar el programa
    while(bool){
        bool = confirm("¿Quieres continiar con el programa?");
        console.log(bool);
    }
    el.innerText = "Has acabado el programa.";
}
// 4. Determinar si el número introducido por usuario es primo
    // Número primo = divisible por si mismo y 1
    function ej4() {
        // Solución con IF
        let el = document.getElementById("ej-4-resultados");
        let num = document.getElementById("input-4").valueAsNumber;
        let i = 2;
        let esPrimo = true; // suponemos sea primo de entrada
        while(i < Math.floor(num/2)) {
            console.log(i, num % i)
            if( num % i == 0 ){
                esPrimo = false;
                break;
            }
            i++;
        }   
        if(esPrimo){
            el.innerText = "Es Número primo"   
        } else {
            el.innerText = "El Número no es primo"
        }
    }
// 5. Pide una contraseña y si:
    // Coincide -> Acceso concedido
    // No coincide -> 3 intentos
    // Después, mensaje de alerta
    function ej5(){
        let pwd = document.getElementById("input-5a").value; // contraseña
        let pwd2 = document.getElementById("input-5b").value; // repetida
        let res = document.getElementById("ej-5-resultados");
        let i = 0;
        while( pwd != pwd2 && i < 3 ){
            res.innerText = "Las contraseñas no coinciden";
            // Idea 1: usar <dialog> con input type=password
            pwd2 = prompt("Introduce la contraseña repetida:")
             // Idea 2: Actualizar value en input-5b de pwd2
            i++;
        }
        if(pwd == pwd2){
            res.innerText = "Las contraseñas coinciden"
        } else {
            res.innerText = "Las contraseñas no coinciden"
            // alert("Se han usado los 3 intentos!")
        }
    }

    // 6. Pedimos número con prompt hasta recibir 0 y devolvemos suma
    function ej6(){
        let el = document.getElementById("ej-6-resultados");
        let suma = 0;
        let num = 0;
        do{
            num = Number(prompt("Ingresa un número:"));
            suma += num;
        } while( num != 0 )
        el.innerText = "Suma: " + suma;
    }
    // 7. Similar pero calculamos min y max de la lista de números
    // con 0 se para el programa
    function ej7(){
        let el = document.getElementById("ej-7-resultados");
        let arr =[];
        let min = 0;
        let max = 0;
        let num = 0;
        do{
            num = Number(prompt("Ingresa un número:"));
            if(num != 0){ 
                arr.push(num)
            }
            
            console.log(arr)
        } while( num != 0 )
        // Buscamos mínimo
        min = arr[0];
        max = arr[0];
        for(let i = 1; i < arr.length; i++){
            if( arr[i] < min ){
                min = arr[i]
            }
            if(arr[i] > max){
                max = arr[i]
            }
            console.log(max)
        }
       
        // Math.max() y Math.min()
            // Usando Math y el operador spread "..." conseguimos lo mismo:
        //max = Math.max(...arr)
        //min = Match.min(...arr)

        el.innerText = "Mín: " + min + " y Máx: " + max;
    }
    // 8. Similar pero solo aceptamos pares. Si impar -> break;
        // Devolvemos númer de pares recibidos
    function ej8(){
        el = document.getElementById("ej-8-resultados");
        let num = 0;
        let pares = 0;
        do{
            num = Number(prompt("Ingresa un número par"));
            if(num % 2 == 0){
                pares++;
            }
        } while (num % 2 == 0)
        el.innerText = "Pares " + pares;
        
    }
    // 9. Pedimos número y mostramos menú
        // Mostramos opción recibida del 1 a la N (según menú)
        // Cualquier número (en rango) muestra la opción
            // Si no está en rango -> ERROR
        // N acaba el programa
        function ej9(){
        let el = document. getElementById("ej-9-resultados")
        const menu = `Menu:
                        1 - Opción A
                        2 - Opción B
                        3 - Opción C
                        4 - Opción D
                        5 - Fin
                        `;
        let num = 0;
        let msj = "";
        do{
            num = Number(prompt(msj + "\nIngresa una opción:"));
            switch(num){
                case 1:
                    msj = "Opción A";
                    break;
                case 2:
                    msj = "Opción B";
                    break;
                case 3:
                    msj = "Opción C";
                    break;
                case 4:
                    msj = "Opción D";
                    break; 
                default:
                    if(num == 5){
                    msj = " Programa finalizado";
                }else {
                    alert = ("Ese número no está en el rango")
                }             
            }
        } while (num != 5)
        el.innerText = msj;
    }    
    // 10. Pedimos números hasta recibir un 0
        // Si suma par (0 cuenta como par) -> repite
        // Si suma impar -> acaba el programa
        function ej10(){
            let el = document. getElementById("ej-10-resultados")
            let num = 0;
            let suma = 0;
            do{
                num = Number(prompt("Introduce un número:"))
                suma += num;
            }while(suma % 2 == 0)
            el.innerText = "Suma " + suma;
        }
