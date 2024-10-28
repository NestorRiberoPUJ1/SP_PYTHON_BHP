

/* Función asincrónica */
async function loadCategories () {
    try {
        //Peticion a la API
        const response = await fetch('https://swapi.dev/api/');
        const data = await response.json();
        console.log(data);

        const select = document.getElementById('categoriesIpt');
        const categories = Object.keys(data);

        categories.forEach((category) => {
            const opt = `<option value="${data[category]}">${category}</option>`;
            select.innerHTML += opt;
        })

    } catch (error) {
        console.log(error);
    }

}


/* Promesas then */

function loadCategoriesThen() {

    fetch('https://swapi.dev/api/')
        .then(response => response.json())
        .then(data => {
            console.log(data);

            const select = document.getElementById('categoriesIpt');
            const categories = Object.keys(data);

            categories.forEach((category) => {
                const opt = `<option value="${data[category]}">${category}</option>`;
                select.innerHTML += opt;
            })
        })
        .catch(error => console.log(error));

}

loadCategories();

const handleCargarPerrito= async ()=>{
    const response= await fetch('https://dog.ceo/api/breeds/image/random');
    const data= await response.json();
    console.log(data);
    const url = data.message;
    console.log(url);
    const img= document.getElementById('dogImg');
    img.src= url;
}