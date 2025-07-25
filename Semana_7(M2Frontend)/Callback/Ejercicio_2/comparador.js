const fs = require('fs');

const compararPalabras = (archivo1, archivo2, callback) => {
    fs.readFile(archivo1, 'utf8', (err1, contenido1) => {
        if (err1) throw err1;

        fs.readFile(archivo2, 'utf8', (err2, contenido2) => {
            if (err2) throw err2;

            const palabras1 = contenido1.split('\n').map(p => p.trim());
            const palabras2 = contenido2.split('\n').map(p => p.trim());

            const repetidas = palabras1.filter(p => palabras2.includes(p));
            callback(repetidas);
        });
    });
};

compararPalabras('archivo1.txt', 'archivo2.txt', (coincidencias) => {
    console.log("Repeated words:", coincidencias);
    console.log("¡Thats the secret message!");
});
