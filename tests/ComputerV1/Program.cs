using System;

namespace ComputerV1
{
 internal static class Program
    {
        public static void Main(string[] args)
        {
            string eq = "";
            if (args.Length != 0)
            {
                if (args.Length == 1) 
                { 
                    eq = args[0];
                }
                else 
                { 
                    Console.WriteLine("il faut seulement un argument");
                    return; 
                }
            }
            else
            {
                Console.WriteLine("veuillez entrer une equation");
                eq = Console.ReadLine();
            }
            try { 
                var newEq = new Polynome(eq);
                newEq.Calculate();
                }
            catch (Exception e) 
            { 
                Console.WriteLine(e.Message);
            }
        }
    }
}
