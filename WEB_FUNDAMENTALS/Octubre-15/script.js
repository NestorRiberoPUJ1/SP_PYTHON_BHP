/* VARIABLES */

var nombre = "Perter"; // Global, se puede acceder desde cualquier parte del código
let apellido = "Parker"; // Local, solo se puede acceder dentro del scope donde se declaró
const edad = 18; // Constante, no se puede reasisgnar su valor


/* TIPOS DE DATOS */

// Primitivos
let string = "Hola mundo"; // Cadena de texto
let number = 18; // Número
let boolean = true; // Booleano
let nullValue = null; // Valor nulo
let undefinedValue = undefined; // Valor indefinido

// Compuestos
let array = [1, 2, 3]; // Arreglo, suelen contener valores del mismo tipo
let object = { key: "value" }; // Objeto, suelen contener valores de distinto tipo

let gruposDeBanda = ["Grupo Firme", "Banda MS", "Banda El Recodo"]
console.log(gruposDeBanda[0]) // Grupo Firme

let grupoFirme = {
    nombre: "Grupo Firme",
    integrantes: 5,
    genero: "Banda",
    exitos: ["El Güero", "El Roto", "El Amor No Fue Pa' Mi"],
    premios: {
        grammys: 0,
        billboard: 0
    }
}
console.log(grupoFirme.nombre) // Grupo Firme
console.log(grupoFirme["integrantes"]) // 5

console.log(grupoFirme.exitos[2]) // El Amor No Fue Pa' Mi
console.log(grupoFirme.premios.grammys) // 0

// De los objectos en javascript nace el formato JSON

// Anidados
let nestedArray = [1, [2, 3]]; // Arreglo anidado
let nestedObject = { key: { key: "value" } }; // Objeto anidado
let mixed = [1, { key: "value" }]; // Arreglo con objeto anidado




/* CONDICIONALES */
edad = 18;

if (edad >= 18) {
    console.log("Puede comprar licor");
} else {
    console.log("No puede comprar licor");
}

if (edad >= 21) {
    console.log("Puede votar en las elecciones presidenciales");
} else if (edad >= 18) {
    console.log("Puede votar en las elecciones municipales");
} else {
    console.log("No puede votar");
}

/* OPERADORE DE COMPARACION0 */

1 > 2 // false
1 < 2 // true
1 >= 2 // false
1 <= 2 // true
1 == 2 // false // Comparación de valores
1 === 2 // false // Comparación de valores y tipos de datos
1 == "1" // true
1 === "1" // false  
1 != 2 // true
1 !== 2 // true











