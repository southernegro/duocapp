
document.getElementById('btnEnviar').addEventListener('click', (event) => {

    var email = document.getElementById('txtEmail').value;

    var run = document.getElementById('txtRun').value;

    var nombre = document.getElementById('txtNombre').value;

    var fechaNacimiento = document.getElementById('datepicker').value;

    var telefono = document.getElementById('txtTelefono').value;

    var region = document.getElementById('regiones').value;

    var ciudad = document.getElementById('comunas').value;

    var tipoVivienda = document.getElementById('cmbTipoVivienda').value;

    validarEmail(email);
    validaRut(run);
    validarNombre(nombre);
    validarFechaNacimiento(fechaNacimiento);
    ValidaSoloNumeros(telefono);  
    validarRegion(region);
    validarCiudad(ciudad);
    validarTipoVivienda(tipoVivienda);

    event.preventDefault();
})

function validarEmail(valor) {
    var mensajeEmail = document.getElementById('mensajeEmail');
    if(!valor){      
        mensajeEmail.classList.add('text-danger');
        mensajeEmail.innerHTML='El campo Email no puede estar vacío.';
        return;
    }
    if (/^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i.test(valor)) {
        mensajeEmail.classList.remove('text-danger');
        mensajeEmail.classList.add('text-success');
        mensajeEmail.innerHTML="La dirección de email " + valor + " es correcta.";
        //alert("La dirección de email " + valor + " es correcta.");
    } else {
        mensajeEmail.classList.add('text-danger');
        mensajeEmail.innerHTML='La dirección de email es incorrecta.';
        //alert("La dirección de email es incorrecta.");
    }
}

function validaRut(run) {
    var mensajeRun = document.getElementById('mensajeRun');
    if(!run){
        mensajeRun.classList.add('text-danger');
        mensajeRun.innerHTML='El campo RUN no puede quedar vacío.';
        return;
    }

    //minimo y maximo caracteres
    if(run.length<9){
        mensajeRun.classList.add('text-danger');
        mensajeRun.innerHTML='El campo RUN debe tener mínimo 9 caracteres.';
        return;
    }else if(run.length>10){
        mensajeRun.classList.add('text-danger');
        mensajeRun.innerHTML='El campo RUN debe tener máximo 10 caracteres.';
        return;
    }

    //verificar si la parte numerica contiene sólo numeros
    for (i = 0; i < run.length-2; i++)
    {
        if (!((run.charAt(i) >= "0") && (run.charAt(i) <= "9"))){
            mensajeRun.classList.add('text-danger');
            mensajeRun.innerHTML='La primera parte del RUN, antes del guión, sólo debe contener números.';
            return;
        }
    }

    var cadenaRun = run.toString().toLowerCase();

    if(!cadenaRun.endsWith('1') && !cadenaRun.endsWith('2') && !cadenaRun.endsWith('3') && !cadenaRun.endsWith('4') 
    && !cadenaRun.endsWith('5') && !cadenaRun.endsWith('6') && !cadenaRun.endsWith('7') && !cadenaRun.endsWith('8') 
    && !cadenaRun.endsWith('9') && !cadenaRun.endsWith('k') && !cadenaRun.endsWith('0')){
        mensajeRun.classList.add('text-danger');
        mensajeRun.innerHTML='El formato del RUN es incorrecto.';
        return;
    }
    var suma = 0;
    var arrRut = run.split("-");
    var rutSolo = arrRut[0];
    var verif = arrRut[1];
    var continuar = true;
    for (i = 2; continuar; i++) {
        suma += (rutSolo % 10) * i;
        rutSolo = parseInt((rutSolo / 10));
        i = (i == 7) ? 1 : i;
        continuar = (rutSolo == 0) ? false : true;
    }
    resto = suma % 11;
    dv = 11 - resto;
    if (dv == 10) {
        if (verif.toUpperCase() == 'K')
            //return true;
            mensajeRun.classList.remove('text-danger');
            mensajeRun.classList.add('text-success');
            mensajeRun.innerHTML="El run " + run + " es correcto. ";
    }
    else if (dv == 11 && verif == 0){
        mensajeRun.classList.remove('text-danger');
        mensajeRun.classList.add('text-success');
        mensajeRun.innerHTML="El run " + run + " es correcto. ";
    }   
    else if (dv == verif){
        mensajeRun.classList.remove('text-danger');
        mensajeRun.classList.add('text-success');
        mensajeRun.innerHTML="El run " + run + " es correcto. ";
    }    
    else{
        mensajeRun.classList.add('text-danger');
        mensajeRun.innerHTML="El run " + run + " es incorrecto. ";
    }
        
}

function validarNombre(nombre) {
    var mensajeNombre = document.getElementById('mensajeNombre');
    if(!nombre){      
        mensajeNombre.classList.add('text-danger');
        mensajeNombre.innerHTML='El campo Nombre Completo no puede quedar vacío.';
        return;
    }
    if (/^[A-Za-z\_\-\.\s\xF1\xD1]+$/i.test(nombre)) {
        mensajeNombre.classList.remove('text-danger');
        mensajeNombre.classList.add('text-success');
        mensajeNombre.innerHTML='Campo Nombre Completo correcto.';
        return;
    } else {
        mensajeNombre.classList.add('text-danger');
        mensajeNombre.innerHTML='Campo Nombre Completo incorrecto.';
    }
}

function validarFechaNacimiento(fechaNacimiento){
    var mensajeFechaNacimiento=document.getElementById('mensajeFechaNacimiento');
    if(!fechaNacimiento){
        mensajeFechaNacimiento.classList.add('text-danger');
        mensajeFechaNacimiento.innerHTML='El campo Fecha de Nacimiento no puede quedar vacío.';
        return;
    }else{
        mensajeFechaNacimiento.classList.remove('text-danger');
        mensajeFechaNacimiento.classList.add('text-success');
        mensajeFechaNacimiento.innerHTML='El campo Fecha de Nacimiento fué ingresado correctamente.';
    }
}

function ValidaSoloNumeros(telefono) {
    var mensajeTelefono = document.getElementById('mensajeTelefono');
    if(!telefono){
        mensajeTelefono.classList.add('text-danger');
        mensajeTelefono.innerHTML='El campo Teléfono no puede estar vacío.';
        return;
    } 

    for (i = 0; i < telefono.length; i++)
    {
        if (!((telefono.charAt(i) >= "0") && (telefono.charAt(i) <= "9"))){
            mensajeTelefono.classList.add('text-danger');
            mensajeTelefono.innerHTML='El campo Teléfono admite sólo caracteres numéricos.';
            return;
        }
    }

    if(telefono.toString().length<8 || telefono.toString().length>8){
        mensajeTelefono.classList.add('text-danger');
        mensajeTelefono.innerHTML='El campo Teléfono admite sólo 8 caracteres numéricos.';
        return;
    }

    if(!isNaN(telefono)){
        mensajeTelefono.classList.remove('text-danger');
        mensajeTelefono.classList.add('text-success');
        mensajeTelefono.innerHTML='El campo Teléfono fué ingresado correctamente.';
    }
}

function validarRegion(region){
    var mensajeRegion=document.getElementById('mensajeRegion');
    if(region=='sin-region'){
        mensajeRegion.classList.add('text-danger');
        mensajeRegion.innerHTML='Debe seleccionar una Región del país.';
        return;
    }else{
        mensajeRegion.classList.remove('text-danger');
        mensajeRegion.classList.add('text-success');
        mensajeRegion.innerHTML='El campo Región fué ingresado correctamente.';
    }
}

function validarCiudad(ciudad){
    var mensajeCiudad=document.getElementById('mensajeCiudad');
    if(ciudad=='sin-region' || ciudad=='sin-comuna'){
        mensajeCiudad.classList.add('text-danger');
        mensajeCiudad.innerHTML='Debe escoger una Ciudad de la Región seleccionada.';
        return;
    }else{
        mensajeCiudad.classList.remove('text-danger');
        mensajeCiudad.classList.add('text-success');
        mensajeCiudad.innerHTML='El campo Ciudad fué ingresado correctamente.';
    }
}

function validarTipoVivienda(tipoVivienda){
    var mensajeTipoVivienda=document.getElementById('mensajeTipoVivienda');
    if(tipoVivienda=='Seleccione Tipo Vivienda'){
        mensajeTipoVivienda.classList.add('text-danger');
        mensajeTipoVivienda.innerHTML='Debe seleccionar una opción del comboBox.';
        return;
    }else{
        mensajeTipoVivienda.classList.remove('text-danger');
        mensajeTipoVivienda.classList.add('text-success');
        mensajeTipoVivienda.innerHTML='El campo Tipo de Vivienda fué ingresado correctamente.';
    }
}