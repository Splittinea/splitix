using System;

//------------------ CUSTOM LIBRARIES ------------------
using sLANG.Lexer;
using sLANG.Parser;
using sLANG.Interpreter;
//------------------------------------------------------

namespace sLANG
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("== sLANG Interpreter v0.1 ==");

            var interpreter = new Interpreter.Interpreter(); 

            while (true)
            {
                Console.Write(">>> ");                      // Prompt REPL
                string source = Console.ReadLine();

                if (string.IsNullOrWhiteSpace(source))
                    continue;

                if (source.Trim().ToLower() == "exit")
                    break;

                try
                {
                    var lexer = new Lexer.Lexer(source);
                    var tokens = lexer.Tokenize();

                    var parser = new Parser.Parser(tokens);
                    var ast = parser.Parse();

                    interpreter.Execute(ast);
                }
                catch (Exception ex)
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine($"[ERROR] {ex.Message}");
                    Console.ResetColor();
                }
            }
        }
    }
}
