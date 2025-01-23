#include <iostream>
#include <vector>
#include <algorithm> // Para std::equal

using namespace std;

int main() {
    int n1, n2;

    // Pedir la cantidad de datos para la primera lista
    cout << "Ingrese la cantidad de datos para la primera lista: ";
    cin >> n1;

    if (n1 <= 0) {
        cout << "Debe ingresar al menos un dato para la primera lista." << endl;
        return 1; // Indica error
    }

    vector<int> lista1(n1);

    cout << "Ingrese los datos para la primera lista:" << endl;
    for (int i = 0; i < n1; i++) {
        cout << "Dato " << i + 1 << ": ";
        cin >> lista1[i];
    }


    // Pedir la cantidad de datos para la segunda lista
    cout << "\nIngrese la cantidad de datos para la segunda lista: ";
    cin >> n2;

    if (n2 <= 0) {
        cout << "Debe ingresar al menos un dato para la segunda lista." << endl;
        return 1; // Indica error
    }

    vector<int> lista2(n2);

    cout << "Ingrese los datos para la segunda lista:" << endl;
    for (int i = 0; i < n2; i++) {
        cout << "Dato " << i + 1 << ": ";
        cin >> lista2[i];
    }

    // Comparar las listas
    if (lista1.size() == lista2.size()) { // Primero verificar el tamaño
        if (equal(lista1.begin(), lista1.end(), lista2.begin())) { // Luego el contenido
            cout << "\na. Las listas son iguales en tamaño y en contenido." << endl;
        } else {
            cout << "\nb. Las listas son iguales en tamaño pero no en contenido." << endl;
        }
    } else {
        cout << "\nc. No tienen el mismo tamaño ni contenido." << endl;
    }

        //Mostrar las listas
    cout << "\nLista 1: ";
    for(int valor : lista1){
        cout << valor << " ";
    }
    cout << endl;

    cout << "Lista 2: ";
    for(int valor : lista2){
        cout << valor << " ";
    }
    cout << endl;

    return 0;
}