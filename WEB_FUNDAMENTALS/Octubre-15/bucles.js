

/* BUCLE POR CANTIDAD FINITA DE VECES */

for (let iterador = 0; iterador < 10; iterador++) {
    console.log(iterador);
}


/* BUCLE POR CANTIDAD INDEFINIDA DE VECES */

let aleatorio = 0;
while (aleatorio < 1) {
    aleatorio = Math.random() * 10;
    console.log(aleatorio);
}


/* BUCLES Y LOS ARREGLOS */


let arteMarciales = ['Karate', 'Kung Fu', 'Judo', 'Taekwondo', 'Boxeo', 'Muay Thai', 'Jiu Jitsu', 'Aikido', 'Capoeira', 'Krav Maga'];

//Tradicionales
for (let i = 0; i < arteMarciales.length; i++) {
    console.log(arteMarciales[i]);
}

//Modernos
arteMarciales.forEach(arteMarcial => {
    console.log(arteMarcial);
});


//Metodos de los arreglos
let numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

//filter
let numerosPares = numeros.filter(numero => numero % 2 === 0);
console.log(numerosPares);

//find
let numeroEncontrado = numeros.find(numero => numero === 5);
console.log(numeroEncontrado);

//map
let numerosDuplicados = numeros.map(numero => numero * 2);
console.log(numerosDuplicados);

//reduce
let suma = numeros.reduce((acumulador, numero) => acumulador + numero, 0);
console.log(suma);

//some
let hayNumerosNegativos = numeros.some(numero => numero < 0);
console.log(hayNumerosNegativos);

//every
let todosSonPositivos = numeros.every(numero => numero > 0);
console.log(todosSonPositivos);

//sort
let numerosOrdenados = numeros.sort((a, b) => a - b);
console.log(numerosOrdenados);

//reverse
let numerosReversa = numeros.reverse();
console.log(numerosReversa);





