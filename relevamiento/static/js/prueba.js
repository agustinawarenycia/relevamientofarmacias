console.log('Hola mundo')

/*

$.ajax({   
    url: '/farmacias/buscar_fcia/',    
    type: 'GET',
    ata: data,
    success: function(data){ 
    console.log(data.mystring);
    
                             }
                        })
*/

/*
$.ajax({
    type: 'GET',
    url: '/farmacias/data-json',
    sucess: function(response){
        console.log(response)
        const data = JSON.parse(response.data)
        console.log(data)
            data.array.forEach(el => {
            console.log(el.fields)
        });
    },
    error: function(error){
    console.log(error)
    
    }
})
console.log('Hola mundo')

$.ajax({
    type: "GET",
    url: "/farmacias/data-json/",
    dataType: "json",
    sucess: function(response){
        console.log(response);
    },
 
})

document.querySelector('#boton').addEventListener('click', traerDatos());
function traerDatos(){
    const xhhhtp = new XMLHttpRequest();
    xhhhtp.open('GET', '/farmacias/data-json/', true)
    xhhhtp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            console.log(this.responseText);
        }
    }
}

document.querySelector('#boton').addEventListener('click', listaPc());

function listaPc(){
    $.ajax({
        url: "/farmacias/data-json/",
        type: "get", 
        datatype: "json",
        success: function(response){
            console.log(response);
        }
    });
}
$(document).ready(function (){
    listarPC();
});


$.get('/farmacias/data-json/')
  .done(function( data ) {
     var content = JSON.parse(data);
     console.log(content)
     alert(content[0].nombre)
  });

function abrir_modal(url){
  $('#edicion').load(url, function(){
    $(this).modal('show')
  });
}
*/