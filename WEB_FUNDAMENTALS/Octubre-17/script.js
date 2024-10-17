


function handleClick(elemento) {
    console.log(elemento);
    elemento.style.backgroundColor = "red";
}

function handleMouseOver(elemento) {
    // El elemento que disparó el evento
    console.log(elemento);
    /*Cuando mi mouse está dentro del elemento creo
     un evento que permite escuchar el movimiento del mouse */

     
    document.body.style.overflow = 'hidden';
    elemento.addEventListener('mouseleave', () => {
        document.body.style.overflow = 'auto';
    });

    let scale = 1;
    elemento.addEventListener('wheel', (e) => {
        // El evento que se disparó
        console.log(e);
        // el valor del evento
        console.log(e.wheelDelta);
        // Cambiar tamaño del elemento

        if (e.wheelDelta < 0) {
            scale -= 0.1;
            elemento.style.transform = `scale(${scale})`;
        }
        else {
            scale += 0.1;
            elemento.style.transform = `scale(${scale})`;
        }


    });

}