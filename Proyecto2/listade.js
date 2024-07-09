let numeros = [];
for (let i = 0; i < 10; i++) {
    numeros.push(Math.floor(Math.random() * 1000) + 1);
}

let numeroMenor = Math.min(...numeros);
let numeroMayor = Math.max(...numeros);
let diferencia = numeroMayor - numeroMenor;

alert(`El número menor es: ${numeroMenor}\nEl número mayor es: ${numeroMayor}\nLa diferencia entre ambos es: ${diferencia}`);