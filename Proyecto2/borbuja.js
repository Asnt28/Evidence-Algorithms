private static void burbuja(int[] arreglo) {
    for (int x = 0; x < arreglo.length; x++) {
        // Aquí "y" se detiene antes de llegar
        // a length - 1 porque dentro del for, accedemos
        // al siguiente elemento con el índice actual + 1
        for (int y = 0; y < arreglo.length - 1; y++) {
            int elementoActual = arreglo[y],
                    elementoSiguiente = arreglo[y + 1];
            if (elementoActual > elementoSiguiente) {
                // Intercambiar
                arreglo[y] = elementoSiguiente;
                arreglo[y + 1] = elementoActual;
            }
        }
    }
}