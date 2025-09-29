// AST -> Nodes
using System.Linq.Expressions;
using System.Reflection.Emit;
using sCOMP.ILGenerator;

namespace sCOMP.AST
{

    public abstract class ASTNode
    {
        public abstract void Accept(IVisitor visitor);
    }

    // Print Statement Node
    public class PrintNode : ASTNode, IStatement
{
        // Global expression declaration
        public Expression Expr { get; set; }

        // Print Node
        public PrintNode(Expression expr) { Expr = expr; }

        public override void Accept(IVisitor visitor) { visitor.VisitPrint(this); }

    }

    // Variable Declaration Node
    public class VariableDeclarationNode : ASTNode, IStatement
    {
        // Variable informations
        public string Name { get; set; }
        public string Domain { get; }
        public Expression InitialValue { get; }

        public VariableDeclarationNode(string name, string domain, Expression initialValue)
        {
            Name = name;
            Domain = domain;
            InitialValue = initialValue;
        }

        public override void Accept(IVisitor visitor) { visitor.VisitVariableDeclaration(this); }
    }

    // Variable Assignment Node
    public class VariableAssignmentNode : ASTNode, IStatement
    {
        // Variable informations
        public string Name { get; set; }
        public Expression NewValue { get; set; }
        public VariableAssignmentNode(string name, Expression newValue)
        {
            Name = name;
            NewValue = newValue;
        }
        public override void Accept(IVisitor visitor) { visitor.VisitVariableAssignment(this); }
    }
}