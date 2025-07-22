import fetch from 'node-fetch';

async function ejercicio2() {
    try {
        const res = await fetch('https://reqres.in/api/usens/23'); // URL incorrecta
        if (!res.ok) throw new Error("Usuario no se encontró");
        const data = await res.json();
        console.log("Ejercicio 2 - Usuario:");
        console.log(data.data);
    } catch (err) {
        console.error("Ejercicio 2 - Error:", err.message);
    }
}

ejercicio2();
