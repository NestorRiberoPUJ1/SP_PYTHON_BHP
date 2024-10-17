

// Query Selector
// 1. Seleccionar el primer elemento que cumpla con el selector
// 2. Utiliza el selector de CSS

const title = document.querySelector('h2');
console.log(title);

//Query Selector All
// 1. Selecciona todos los elementos que cumplan con el selector
// 2. Devuelve un NodeList
const parrafo = document.querySelectorAll('p');
console.log(parrafo);
const btns = document.querySelectorAll('.btn');
console.log(btns);


title.addEventListener('click', (event) => {
    const elemento = event.target;
    elemento.style.color = 'red';
});

btns.forEach((btn) => {
    btn.addEventListener('click', (_event) => {
        let currentValue = parseInt(btn.dataset.likes) + 1;
        btn.dataset.likes = currentValue;//Cambiar el valor del atributo data-likes
        btn.innerHTML = `${currentValue} likes`;
    });
})


/* ESTRUCTURA PARA CREAR UN ESCUCHADOR DE EVENTOS */

// 1. Seleccionar el elemento
// 2. Crear la función que se ejecutará
// 3. Agregar el evento al elemento

// const title = document.querySelector('h2');
// title.addEventListener('click', (event) => {
//     const elemento = event.target;
//     elemento.style.color = 'red';
// });
