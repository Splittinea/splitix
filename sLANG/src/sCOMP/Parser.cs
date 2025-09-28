using System.Security.AccessControl;

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
                    var contents = line.Substring(4).Split('=');
                    if (contents.Length == 2)
                    {
                        var name = contents[0].Trim();
                        var value = contents[1].Trim();

                        if (double.TryParse(value, NumberStyles.Any, CultureInfo.InvariantCulture, out double num)) { stmts.Add(new VariableDeclarationNode(name, null, new NumberLiteral(num))); } /* Adds a new variable declaration flush to the compiler
                                                                                                                                                    * With the name and the value
                                                                                                                                                    * Here, the domain is NOT provided
                                                                                                                                                    */
                        else if (value.StartsWith("\"") && value.EndsWith("\""))
                        {
                            var text = value.Substring(1, value.Length - 2);
                            stmts.Add(new VariableDeclarationNode(name, null, new StringLiteral(text)));
                        }
                        else { stmts.Add(new VariableDeclarationNode(name, null, new IdentifierNode(value))); }
                    }
                }
                else if (line.Contains("="))
                {
                    var parts = line.Split('=');
                    if (parts.Length == 2)
                    {
                        var name = parts[0].Trim();
                        var value = parts[1].Trim();

                        // Adds to the assign flush of the compiler, the value to be given to a variable matching with the given name
                        if (double.TryParse(value, NumberStyles.Any, CultureInfo.InvariantCulture, out double num)) { stmts.Add(new VariableAssignmentNode(name, new NumberLiteral(num))); }
                        else if (value.StartsWith("\"") && value.EndsWith("\""))
                        {
                            var text = value.Substring(1, value.Length - 2);
                            stmts.Add(new VariableAssignmentNode(name, new StringLiteral(text)));
                        }
                        else { stmts.Add(new VariableAssignmentNode(name, new IdentifierNode(value))); }
                    }
                }
                else { Console.Error.WriteLine($"Unrecognized Statement: {line}"); }
            }

            return stmts;
        }
    }
}
