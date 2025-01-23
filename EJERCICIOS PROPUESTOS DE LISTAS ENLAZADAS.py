#include <iostream>
#include <vector>
#include <numeric> // Para std::accumulate

int main() {
    int n;

    // Pedir al usuario la cantidad de datos
    std::cout << "Ingrese la cantidad de datos a ingresar: ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "Debe ingresar al menos un dato." << std::endl;
        return 1; // Indica error
    }

    std::vector<double> datosPrincipal(n);

    // Pedir al usuario que ingrese los datos
    std::cout << "Ingrese los datos reales:" << std::endl;
    for (int i = 0; i < n; i++) {
        std::cout << "Dato " << i + 1 << ": ";
        std::cin >> datosPrincipal[i];
    }

    // Calcular el promedio
    double suma = std::accumulate(datosPrincipal.begin(), datosPrincipal.end(), 0.0);
    double promedio = suma / n;

    // Crear las listas para valores menores/iguales y mayores al promedio
    std::vector<double> menoresIguales;
    std::vector<double> mayores;

    // Separar los datos según el promedio
    for (double dato : datosPrincipal) {
        if (dato <= promedio) {
            menoresIguales.push_back(dato);
        } else {
            mayores.push_back(dato);
        }
    }

    // Mostrar los resultados
    std::cout << "\na. Datos cargados en la lista principal:" << std::endl;
    for (double dato : datosPrincipal) {
        std::cout << dato << " ";
    }
    std::cout << std::endl;

    std::cout << "\nb. Promedio: " << promedio << std::endl;

    std::cout << "\nc. Datos menores o iguales al promedio:" << std::endl;
    if (menoresIguales.empty()) {
        std::cout << "Ninguno" << std::endl;
    } else {
    for (double dato : menoresIguales) {
        std::cout << dato << " ";
    }
    std::cout << std::endl;
    }

    std::cout << "\nd. Datos mayores al promedio:" << std::endl;
    if (mayores.empty()) {
        std::cout << "Ninguno" << std::endl;
    } else {
    for (double dato : mayores) {
        std::cout << dato << " ";
    }
    std::cout << std::endl;
    }

    return 0;
}