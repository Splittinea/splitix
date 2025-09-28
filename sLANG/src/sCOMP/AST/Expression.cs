// AST -> Expressions

namespace sCOMP.AST
{
    public abstract class  Expression : ASTNode
    {
        //pass
    }

    public class StringLiteral : Expression
    {
        public string Value { get; set; }
        public StringLiteral(string value) { Value = value; }
        public override void Accept(IVisitor visitor) { visitor.VisitStringLiteral(this); }
    }

    public class NumberLiteral : Expression
    {
        public double Value { get; }
        public NumberLiteral(double value) { Value = value; }
        public override void Accept(IVisitor visitor) { visitor.VisitNumberLiteral(this); }
    }

    // Identifier (Variable Reference)
    public class IdentifierNode : Expression
    {
        public string Name { get; set; }
        public IdentifierNode(string name) { Name = name; }
        public override void Accept(IVisitor visitor) { visitor.VisitIdentifier(this); }
    }
}