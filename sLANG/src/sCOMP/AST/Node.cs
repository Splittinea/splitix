// AST -> Nodes
namespace sCOMP.AST
{
    public abstract class ASTNode
    {
        public abstract void Accept(IVisitor visitor);
    }
}