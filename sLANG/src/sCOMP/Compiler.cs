using System.Collections.Specialized;
using System.Security.Cryptography.X509Certificates;
using Microsoft.CodeAnalysis.CSharp.Syntax;

namespace sCOMP
{
    public class Compiler
    {
        public void Compile(string filePath)
        {
            // Checks if the given file exists
            if (!File.Exists(filePath))
            {
                Console.WriteLine($"File not found: {filePath}");
                return;
            }

            Console.WriteLine($"[INFO] Compiling {filePath}");

            var code = File.ReadAllLines(filePath);

            // AST Root -> Simple list of stmts
            var stmts = new System.Collections.Generic.List<AST.ASTNode>();

            // Flag to indicate compilation completion
            bool hasCompiled = true;

            Console.WriteLine("[INFO] Parsing...");
            var parser = new Parser();
            var commands = parser.Parse(File.ReadAllLines(filePath));

            // IL Generation / AST Execution
            Console.WriteLine("[INFO] Generating IL and executing...\n");

            var executor = new ConsoleVisitor();

            // Visual Separator
            Console.WriteLine("================== S CODE RESULTS ======================");

            // Executing each instruction
            foreach (var stmt in commands)
            {
                try
                {
                    // Executes the commands one by one
                    stmt.Accept(executor);
                }
                catch (Exception e)
                {
                    Console.WriteLine("\n");
                    Console.Error.WriteLine($"[ERROR] at {stmt} \n {e} \n");
                    Console.WriteLine("[INFO] An error has occured, ending compilation now");
                    hasCompiled = false;
                    break;
                }
            }
            Console.WriteLine("========================================================\n");
            if (hasCompiled)
            {
                Console.WriteLine("[INFO] Compilation finished.\n");
                Console.WriteLine("[INFO] Displaying generated IL code");

                // Visual Separator
                Console.WriteLine("================== IL GENERATED CODE ======================");
                Executor.GenerateIL(commands);
            }
            else { Console.Error.WriteLine($"[ERROR] Compiler was aborted"); }
        }
    }

    public class ConsoleVisitor : AST.IVisitor
    {
        // Variables storage
        private readonly Dictionary<string, object> _variables = new();

        // Visitor methods implementation
        public void VisitPrint(AST.PrintNode printNode) { printNode.Expr.Accept(this); }

        public void VisitStringLiteral(AST.StringLiteral str) { Console.WriteLine(str.Value); }

        public void VisitNumberLiteral(AST.NumberLiteral num) { Console.WriteLine(num.Value); }

        public void VisitIdentifier(AST.IdentifierNode identifier)
        {
            if (_variables.TryGetValue(identifier.Name, out var value))
            {
                Console.WriteLine(value);
            }
            else
            {
                Console.Error.WriteLine($"[ERROR] '{identifier.Name}' is not defined");
            }
        }

        // Variable declaration management
        public void VisitVariableDeclaration(AST.VariableDeclarationNode decl)
        {   
                var value = EvaluateExpression(decl.InitialValue);
                // Validation depending of provided domain
                if (decl.Domain != null)
                {
                    if (!ValidateDomain(decl.Domain, value))
                    {
                        Console.Error.WriteLine($"[ERROR] Value '{value}' is not valid for domain {decl.Domain}");
                        throw new InvalidDomainException($"Invalid domain for '{value}' (using the domain {decl.Domain})");
                    }
                }
                _variables[decl.Name] = value;
                Console.WriteLine($"[DEBUG] Declared variable with name '{decl.Name}', initalized to '{value}' using the domain '{decl.Domain ?? "any"}'");           
        }

        private bool ValidateDomain(string domain, object value)
        {
            switch (domain)
            {
                case "N":
                    return value is double d1 && d1 >= 0 && d1 % 1 == 0;

                case "Z":
                    return value is double d2 && d2 % 1 == 0;

                case "Q":
                    return value is double; // Approx

                case "R":
                    return value is double;

                case "C":
                    // For now, only real numbers are supported
                    return value is double;

                default:
                    return false;
            }
        }

        // Variable assignment management
        public void VisitVariableAssignment(AST.VariableAssignmentNode assign)
        {
            if (!_variables.ContainsKey(assign.Name))
            {
                Console.Error.WriteLine($"[ERROR] '{assign.Name}' is not defined");
                return;
            }

            var value = EvaluateExpression(assign.NewValue);
            _variables[assign.Name] = value;
            Console.WriteLine($"[DEBUG] Variable '{assign.Name}' assigned to new value '{value}'");
        }

        // Evaluation expression helper
        private object EvaluateExpression(Expression expr)
        {
            if (expr is StringLiteral str) { return str.Value; }
            if (expr is NumberLiteral num) { return num.Value; }

            return null;
        }
    }
}