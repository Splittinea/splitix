namespace sLANG.Parser
{
    public abstract class ASTNode { }

    public class NumberNode : ASTNode
    {
        public double Value { get; }
        public NumberNode(double value) => Value = value;
    }

    public class StringNode : ASTNode
    {
        public string Value { get; }
        public StringNode(string value) => Value = value;
    }

    public class IdentifierNode : ASTNode
    {
        public string Name { get; }
        public IdentifierNode(string name) => Name = name;
    }

    public class VarAssignNode : ASTNode
    {
        public string VarName { get; }
        public ASTNode Value { get; }

        public VarAssignNode(string name, ASTNode value)
        {
            VarName = name;
            Value = value;
        }

    }

    public class CallNode : ASTNode
    {
        public string FunctionName { get; }
        public List<ASTNode> Arguments { get; }

        public CallNode(string name, List<ASTNode> args)
        {
            FunctionName = name;
            Arguments = args;
        }
    }

    public class ProgramNode : ASTNode
    {
        public List<ASTNode> Statements { get; }
        public ProgramNode(List<ASTNode> statements) => Statements = statements;
    }
}
