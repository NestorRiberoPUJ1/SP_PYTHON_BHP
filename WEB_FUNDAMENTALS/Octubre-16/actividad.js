/* CALCULADORA ESTADÍSTICA */


/* 
VAMOS A CREAR FUNCIONES PARA OBTENER:
- El promedio
- Minimo
- Maximo
- Moda
- Desviación estandar
- Varianza
- Percentiles 0 25 50 75 100
*/

const generarNumeroAleatorio = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

const generarArregloAleatorio = (n, min, max) => {
    const arreglo = [];
    for (let i = 0; i < n; i++) {
        arreglo.push(generarNumeroAleatorio(min, max));
    }
    return arreglo;
}

const arreglo = generarArregloAleatorio(10, 1, 10);
//Promedio : suma de todos los elementos / cantidad de elementos
const promedio = (arreglo) => {
    /*  const suma = arreglo.reduce((acumulador, valorActual) => acumulador + valorActual, 0); */
    let suma = 0;
    for (let i = 0; i < arreglo.length; i++) {
        suma += arreglo[i];
    }
    return suma / arreglo.length;
}
console.log(promedio([1, 2, 3, 4, 5]));

//Minimo: el valor más pequeño del arreglo
const minimo = (arreglo) => {
    /* const min = Math.min(...arreglo); */
    let min = arreglo[0];
    for (let i = 1; i < arreglo.length; i++) {
        if (arreglo[i] < min) {
            min = arreglo[i];
        }
    }
    return min;
}
console.log(minimo([7, 2, 3, 4, 5]));

//Maximo: el valor más grande del arreglo
const maximo = (arreglo) => {
    /* const max = Math.max(...arreglo); */
    let max = arreglo[0];
    for (let i = 1; i < arreglo.length; i++) {
        if (arreglo[i] > max) {
            max = arreglo[i];
        }
    }
    return max;
}
console.log(maximo([7, 2, 9, 4, 5]));

//Moda: el valor que más se repite
const moda = (arreglo) => {
    const frecuencias = {};
    arreglo.forEach((elemento) => {
        //Si el elemento existe en el objeto, incrementamos su frecuencia
        if (frecuencias[elemento]) {
            frecuencias[elemento]++;
        }
        //Si no existe, lo agregamos con frecuencia 1
        else {
            frecuencias[elemento] = 1;
        }
    });
    //Buscar el valor con mayor frecuencia
    let mayorFrecuencia = 0;
    let moda = null;
    for (let frecuencia in frecuencias) {
        if (frecuencias[frecuencia] > mayorFrecuencia) {
            mayorFrecuencia = frecuencias[frecuencia];
            moda = frecuencia;
        }
    }
    return moda;
}

console.log(moda([1, 3, 4, 6, 3, 3, 6, 4, 2, 1, 3, 6, 6]))




for (let i = 0; i < 1000; i++) {
    const myArray = generarArregloAleatorio(1000, 1, 20);
    console.log(minimo(myArray), maximo(myArray), moda(myArray), promedio(myArray));
}