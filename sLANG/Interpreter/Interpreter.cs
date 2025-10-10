using System;
using System.Collections.Generic;

//------------------ CUSTOM LIBRARIES ------------------
using sLANG.Parser;
//------------------------------------------------------

namespace sLANG.Interpreter
{
    public class Interpreter
    {
        private readonly Dictionary<string, object> _variables = new();

        public void Execute(ASTNode node)
        {
            switch (node)
            {
                case ProgramNode prog:
                    foreach (var stmt in prog.Statements) { Execute(stmt); }
                    break;

                case VarAssignNode varAssign:
                    var value = Evaluate(varAssign.Value);
                    _variables[varAssign.VarName] = value;

                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine($"[INFO] Variable '{varAssign.VarName}' = {value}");

                    Console.ResetColor();
                    break;

                case CallNode call:
                    Console.ForegroundColor = ConsoleColor.Cyan;
                    Console.WriteLine($"[CALL] {call.FunctionName}({string.Join(", ", call.Arguments.ConvertAll(Evaluate))})");

                    Console.ResetColor();
                    break;

                default:
                    throw new Exception($"Unknown Node : {node.GetType().Name}");
            }
        }

        private object Evaluate(ASTNode expr)
        {
            switch (expr)
            {
                case NumberNode n:
                    return n.Value;

                case StringNode s:
                    return s.Value;

                case IdentifierNode id:
                    if (_variables.TryGetValue(id.Name, out var val)) { return val; }
                    throw new Exception($"Undefined Variable : {id.Name}");

                case CallNode call:
                    return $"Call({call.FunctionName})"; //Placeholder

                default:
                    throw new Exception($"Unknow Expression : {expr.GetType().Name}");
            }
        }
    }
}
