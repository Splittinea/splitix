namespace sCOMP.AST
{
    public interface IVisitor
    {
        void VisitPrint(PrintNode print);
        void VisitStringLiteral(StringLiteral str);
        void VisitNumberLiteral(NumberLiteral num);

        // Variable related visitors
        void VisitVariableDeclaration(VariableDeclarationNode decl);
        void VisitVariableAssignment(VariableAssignmentNode assign);
        void VisitIdentifier(IdentifierNode identifier);
    }
}