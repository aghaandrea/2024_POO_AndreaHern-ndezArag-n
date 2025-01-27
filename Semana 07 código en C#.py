using System;
using System.Collections.Generic;

public class BalanceoExpresiones
{
    public static bool EstaBalanceada(string expresion)
    {
        Stack<char> pila = new Stack<char>();

        foreach (char c in expresion)
        {
            if (c == '{' || c == '[' || c == '(')
            {
                pila.Push(c);
            }
            else if (c == '}' || c == ']' || c == ')')
            {
                if (pila.Count == 0)
                {
                    return false; // Cierre sin apertura correspondiente
                }

                char apertura = pila.Pop();
                if ((c == '}' && apertura != '{') ||
                    (c == ']' && apertura != '[') ||
                    (c == ')' && apertura != '('))
                {
                    return false; // No coinciden
                }
            }
        }

        return pila.Count == 0; // Debe estar vacía al final
    }

    public static void Main(string[] args)
    {
        string expresion1 = "{7+(8*5)-[(9-7)+(4+1)]}";
        string expresion2 = "{7+(8*5)-[(9-7)+(4+1]}"; // No balanceada
        string expresion3 = "(]"; // No balanceada

        Console.WriteLine($"{expresion1} => {(EstaBalanceada(expresion1) ? "Fórmula balanceada" : "Fórmula no balanceada")}");
        Console.WriteLine($"{expresion2} => {(EstaBalanceada(expresion2) ? "Fórmula balanceada" : "Fórmula no balanceada")}");
        Console.WriteLine($"{expresion3} => {(EstaBalanceada(expresion3) ? "Fórmula balanceada" : "Fórmula no balanceada")}");
    }
}