C#

// Circulo.cs
public class Circulo
{
    private double radio;

    public Circulo(double radio)
    {
        this.radio = radio;
    }

    public double CalcularArea()
    {
        // Calcula el área de un círculo: π * radio^2
        return Math.PI * radio * radio;
    }

    public double CalcularPerimetro()
    {
        // Calcula el perímetro de un círculo: 2 * π * radio
        return 2 * Math.PI * radio;
    }
}

// Cuadrado.cs
public class Cuadrado
{
    private double lado;

    public Cuadrado(double lado)
    {
        this.lado = lado;
    }

    public double CalcularArea()
    {
        // Calcula el área de un cuadrado: lado * lado
        return lado * lado;
    }

    public double CalcularPerimetro()
    {
        // Calcula el perímetro de un cuadrado: 4 * lado
        return 4 * lado;
    }
}
C#

using System;

namespace Geometria
{
    class Program
    {
        static void Main(string[] args)
        {
            // Crear un círculo de radio 5
            Circulo miCirculo = new Circulo(5);

            // Crear un cuadrado de lado 3
            Cuadrado miCuadrado = new Cuadrado(3);

            // Calcular y mostrar el área y perímetro
            Console.WriteLine("Área del círculo: " + miCirculo.CalcularArea());
            Console.WriteLine("Perímetro del círculo: " + miCirculo.CalcularPerimetro());
            Console.WriteLine("Área del cuadrado: " + miCuadrado.CalcularArea());
            Console.WriteLine("Perímetro del cuadrado: " + miCuadrado.CalcularPerimetro());
        }
    }
}