window.onload=function(){
    document.getElementById("deporte-menu").onclick = mostrarSlideDeporte;
    document.getElementById("academico-menu").onclick = mostrarSlideAcademico;
    document.getElementById("compra-menu").onclick = mostrarSlideCompra;
    document.getElementsByTagName("prestar-articulo").onclick = redirigir;
}
function id(v){
    return document.getElementById(v);
}
function mostrarSlideDeporte(){
    var principal = id("firstView");
    principal.style.display = "none";
    id("compra").style.display = "none";
    id("academico").style.display = "none";
    id("deporte").style.display = "flex";
}
function mostrarSlideAcademico(){
    var principal = id("firstView");
    principal.style.display = "none";
    id("deporte").style.display = "none";
    id("compra").style.display = "none";
    id("academico").style.display = "flex";    
}
function mostrarSlideCompra(){
    var principal = id("firstView");
    principal.style.display = "none";
    id("deporte").style.display = "none";   
    id("academico").style.display = "none";
    id("compra").style.display = "flex";
}
function redirigir(){
    alert("Se puede hacer");
}