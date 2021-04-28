let titulo = document.getElementById("titulo");
let subtitulo = document.getElementById("subtitulo");
let biografia = document.getElementById("biografia");
let lista = document.querySelectorAll('ul > li > p');

function colorRadom(min, max) {
    return Math.random() * (max - min) + min;
}

function cambiarColor(elemento){
    let rojo = colorRadom(0, 255);
    let verde = colorRadom(0, 255);
    let amarillo = colorRadom(0, 255);
    elemento.style = `color: rgb(${rojo}, ${verde}, ${amarillo});";`
}
function clickColor(elemento){
    elemento.addEventListener("click", ()=>{
        cambiarColor(elemento);
    });
}

function overColor(elemento){
    elemento.addEventListener("mouseover", ()=>{
        cambiarColor(elemento);
    });
    elemento.addEventListener("mouseout", ()=>{
        cambiarColor(elemento);
    });
}

clickColor(titulo);
overColor(subtitulo);
clickColor(biografia);

for (valor in lista){
    overColor(lista[valor]);
}