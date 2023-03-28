function leerArchivo() {
    // Obtener el archivo cargado
    var archivo = document.getElementById('archivo').files[0];
    
    // Crear un objeto FileReader
    var lector = new FileReader();
    
    // Definir lo que se va a hacer cuando se cargue el archivo
    lector.onload = function() {
      // Obtener el contenido del archivo como una cadena de texto
      var contenido = lector.result;
      
      // Dividir el contenido del archivo en líneas
      var lineas = contenido.split('\n');
      
      // Iterar por cada línea y agregar la imagen correspondiente al contenedor
      for (var i = 0; i < lineas.length; i++) {
        // Obtener el elemento contenedor
          
          const div = document.createElement('div');
          div.classList.add('col-lg-4');

          // Crear el elemento img con los atributos src, alt, y class
          var urlImagen = lineas[i];
          const img = document.createElement('img');
          img.src = urlImagen;
          img.alt = 'Imagenes';
          img.classList.add('rounded', 'img');
          img.addEventListener("click", function() {
            img.classList.toggle("ampliada");
            console.log('click')
          });

          // Agregar la imagen al div
          div.appendChild(img);

          // Agregar el div al contenedor
        
        document.querySelector('.row').appendChild(div);
      }
    };
    
    // Leer el archivo como una cadena de texto
    lector.readAsText(archivo);
  }
