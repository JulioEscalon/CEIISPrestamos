window.onload=function(){
    document.getElementById("botonRegistrar").onclick = registrarAlumno;
    document.getElementById("botonRecuperar").onclick = recuperarClave;
    document.getElementById("boton").onclick = validarDatos;
    document.getElementById("closeRegistro").onclick = borrarDatosRegistro;
    document.getElementById("closeRecupero").onclick = borrarDatosRecupero;
}
function obtenerClase(v){
    return document.getElementsByClassName(v);
}
function obtenerId(v){
    return document.getElementById(v);
}
function cerrar(){
    var error=obtenerClase("error"); /*Por si acaso :'v*/
    n=error.length;
    for(i=0;i<n;i++){
        error[i].style.display="none";
    }
}
function activar(divInitial){
    return document.getElementById(divInitial).style.display="flex";
}
function ocultar(divNone){
    return document.getElementById(divNone).style.display="none";
}

function borrarDatosRegistro(){
    obtenerId("registrarNombre").value="";
    obtenerId("registrarApellido").value="";
    obtenerId("registrarCodigo").value="";
    obtenerId("registrarEmail").value="";
    obtenerId("registrarEmailAlternativo").value="";
    obtenerId("registrarClave").value="";
    cerrar();
}
function borrarDatosRecupero(){
    obtenerId("recuperarCodigo").value="";
    obtenerId("recuperarEmail").value="";
    obtenerId("recuperarClave").value="";
    obtenerId("recuperarClave2").value="";
    cerrar();
}
function validarDatos(){
    var user = obtenerId("login_codUni").value;
    var psw = obtenerId("login_clave").value;
    if(user=="" || psw==""){
        activar("faltaCampo");
        return false;
    }else{
        //falta la condición de si son iguales a la base datos para que pase al main.
        alert("Supongamos que funciona xd");
    }
}

function registrarAlumno(){
    var nuevoNombre = obtenerId("registrarNombres").value;
    var nuevoApellido = obtenerId("registrarApellidos").value;
    var nuevoCodigoUNI = obtenerId("registrarCodigo").value;
    var nuevoEmailUNI = obtenerId("registrarEmail").value;
    var nuevoEmailAlternativo = obtenerId("registrarEmailAlternativo").value;
    var nuevoPassword = obtenerId("registrarClave").value;
    if(nuevoNombre=="" || nuevoApellido=="" || nuevoCodigoUNI=="" || nuevoEmailUNI=="" || nuevoEmailAlternativo=="" || nuevoPassword==""){
        activar("rellenarCampos1");
        return false;
    }else{
        //falta la condición de si son iguales a la base datos para que pase al main.
        alert("Supongamos que funciona xd");
        return false;
    }
}
function recuperarClave(){
    var codUNI = obtenerId("recuperarCodigo").value;
    var emailUNI = obtenerId("recuperarEmail").value;
    var psw = obtenerId("recuperarClave").value;
    var psw2 = obtenerId("recuperarClave2").value;
    if(codUNI==""||emailUNI==""||psw==""||psw2==""){
        activar("rellenarCampos2");
        return false;
    }else if( psw!==psw2){
        ocultar("rellenarCampos2");
        psw="";psw2="";
        activar("coincidirClaves");
        return false;
    }else if(codUNI=="" || emailUNI==""){
        alert("Revisa el código, login.js buscalo como Fxd");
        //se verifica con la base de datos el email y el correo para ver si está registrado o no.
        activar("no-coincide");
        return false;
    }
}