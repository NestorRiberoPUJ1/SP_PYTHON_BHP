
const persona1 = {
    rut: "12345678-4",
    nombre: "Franco",
    apellido: "Armani",
    cuentaBancaria: {
        banco: "Banco de Chile",
        tipoCuenta: "Cuenta Corriente",
        saldo: 1000
    }
}
const persona2 = {
    rut: "87654321-1",
    nombre: "John",
    apellido: "Cordoba",
    cuentaBancaria: {
        banco: "Banco Itau",
        tipoCuenta: "Cuenta Corriente",
        saldo: 750
    }
}
const persona3 = {
    rut: "1928375-6",
    nombre: "Martín",
    apellido: "Palermo",
    cuentaBancaria: {
        banco: "Banco Santander",
        tipoCuenta: "Cuenta Corriente",
        saldo: 2000
    }
}

/* TRANSACCIONES BÁSICAS */

function verSaldo(persona) {
    console.log(persona.cuentaBancaria.saldo);
}

function depositar(persona, monto) {
    persona.cuentaBancaria.saldo += monto;
}

verSaldo(persona1); // 1000
depositar(persona1, 500);
verSaldo(persona1); // 1500
depositar(persona2, 1000);
verSaldo(persona2);


const transferir = (personaOrigen, personaDestino, monto) => {

    /* console.log("valor", valor); */
    personaOrigen.cuentaBancaria.saldo -= monto;
    personaDestino.cuentaBancaria.saldo += monto;
    /* var valor; */
}

transferir(persona1, persona2, 500);

/* console.log(valor); */

/* TIPOS DE FUNCIONES */

//Procedimentales
//Sin parametros
function saludar() {
    console.log("Hola");
}
//Con parametros
function saludarPersona(nombre) {
    console.log("Hola " + nombre);
}

saludar();
saludarPersona("Juan");

// Funciones que retornan un valor
//Sin parametros
function obtenerFecha() {
    return new Date();
}
//Con parametros
function sumar(a, b) {
    return a + b;
}

console.log(obtenerFecha());
console.log(sumar(5, 3));


const numerosRandom = [1, 62, 635, 64, 98, 13, 7, 22];
function duplicarNumero(numero) {
    console.log(numero * 2);
}
numerosRandom.forEach(duplicarNumero);
// funcion anonima

numerosRandom.forEach(function (numero) {
    console.log(numero * 2);
});

numerosRandom.forEach((numero) => {
    console.log(numero * 2);
});
