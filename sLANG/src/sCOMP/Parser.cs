using System.Security.AccessControl;
using System.Security.Cryptography.X509Certificates;

namespace sCOMP
{
    public class Parser
    {
        public List<ASTNode> Parse(string[] code)
        {
            var stmts = new List<ASTNode>();

            foreach (var raw in code)
            {
                var line = raw.Trim();
                if (string.IsNullOrEmpty(line)) continue; // <- Skips spaces


                if (line.StartsWith("print(") && line.EndsWith(")"))
                {
                    // === print() statement ===
                    var innerContent = line.Substring(6, line.Length - 7);


                    if ((innerContent.StartsWith("\"")) && (innerContent.EndsWith("\"")))
                    {
                        // Case where a string is passed as an argument
                        var text = innerContent.Substring(1, innerContent.Length - 2);
                        stmts.Add(new PrintNode(new StringLiteral(text))); // <- Creates a print flush for the compiler to process yielding a string
                    }
                    else
                    {
                        // Case where something other than a string (number, char, variable) is passed as an argument
                        stmts.Add(new PrintNode(new IdentifierNode(innerContent))); // <- Creates a print flush for the compiler to process yielding a variable
                    }
                }
                else if (line.StartsWith("var "))
                {
                    // === var statement ===
                    string declaration = line.Substring(4).Trim();
                    string name = "";
                    string domain = null;
                    string expressionValue = "";

                    if (declaration.Contains(" in "))
                    {
                        // Treats the case where a variable is declared with a domain
                        var parts = declaration.Split(new[] { " in " }, StringSplitOptions.None);
                        name = parts[0].Trim();
                        
                        var dv = parts[1].Split('=');
                        if (dv.Length == 2)
                        {
                            domain = dv[0].Trim();
                            expressionValue = dv[1].Trim();
                        }
                        else
                        {
                            Console.Error.WriteLine($"[ERROR] Invalid Variable Declaration {line}");
                            continue;
                        }
                    }
                    else
                    {
                        // Treats the case where a variable is NOT delcared with a domain
                        var parts = declaration.Split('=');
                        if (parts.Length == 2)
                        {
                            name = parts[0].Trim();
                            expressionValue = parts[1].Trim();
                        }
                        else
                        {
                            Console.Error.WriteLine($"[ERROR] Invalid Variable Declaration {line}");
                            continue;
                        }
                    }

                    // Value type detection
                    if (double.TryParse(expressionValue, NumberStyles.Any, CultureInfo.InvariantCulture, out double num))
                    {
                        stmts.Add(new VariableDeclarationNode(name, domain, new NumberLiteral(num)));
                    }
                    else if (expressionValue.StartsWith("\"") && expressionValue.EndsWith("\""))
                    {
                        var text = expressionValue.Substring(1, expressionValue.Length - 2);
                        stmts.Add(new VariableDeclarationNode(name, domain, new StringLiteral(text)));
                    }
                    else { stmts.Add(new VariableDeclarationNode(name, domain, new IdentifierNode(expressionValue))); }

                }
                else { Console.Error.WriteLine($"Unrecognized Statement: {line}"); }                
            }
            
            return stmts;
        }
    }
}
