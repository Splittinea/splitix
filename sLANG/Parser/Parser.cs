using System;
using System.Collections.Generic;
using sLANG.Lexer;

namespace sLANG.Parser
{
    public class Parser
    {
        private readonly List<Token> _tokens;
        private int _pos = 0;

        public Parser(List<Token> tokens)
        {
            _tokens = tokens ?? throw new ArgumentNullException(nameof(tokens));
            if (_tokens.Count == 0 || _tokens[^1].Type != TokenType.EndOfFile)
                _tokens.Add(new Token(TokenType.EndOfFile, ""));
        }

        private Token Current => _pos < _tokens.Count ? _tokens[_pos] : _tokens[^1];
        private Token Next() { if (_pos < _tokens.Count - 1) _pos++; return Current; }

        // -------------------- PARSE PROGRAM --------------------
        public ProgramNode Parse()
        {
            var stmts = new List<ASTNode>();
            while (Current.Type != TokenType.EndOfFile)
            {
                stmts.Add(ParseStatement());
            }
            return new ProgramNode(stmts);
        }

        // -------------------- PARSE STATEMENT --------------------
        private ASTNode ParseStatement()
        {
            if (Current.Type == TokenType.Keyword && Current.Value == "var")
                return ParseVarDeclaration();

            if (Current.Type == TokenType.Identifier)
                return ParseExpression();

            throw new Exception($"Unexpected instruction at '{Current.Value}'");
        }

        // -------------------- VAR DECLARATION --------------------
        private ASTNode ParseVarDeclaration()
        {
            Next();
            string name = Expect(TokenType.Identifier).Value;
            ExpectSymbol("=");
            var value = ParseExpression();
            return new VarAssignNode(name, value);
        }

        // -------------------- PARSE EXPRESSION --------------------
        private ASTNode ParseExpression()
        {
            if (Current.Type == TokenType.Number)
            {
                double val = double.Parse(Current.Value);
                Next();
                return new NumberNode(val);
            }

            if (Current.Type == TokenType.String)
            {
                string val = Current.Value;
                Next();
                return new StringNode(val);
            }

            if (Current.Type == TokenType.Identifier)
            {
                string name = Current.Value;

                if (_pos + 1 < _tokens.Count && _tokens[_pos + 1].Type == TokenType.Symbol && _tokens[_pos + 1].Value == "=")
                {
                    Next();
                    Next();
                    var value = ParseExpression();
                    return new VarAssignNode(name, value);
                }

                if (_pos + 1 < _tokens.Count && _tokens[_pos + 1].Type == TokenType.Symbol && _tokens[_pos + 1].Value == "(")
                {
                    Next();
                    return ParseFunctionCall(name);
                }

                Next();
                return new IdentifierNode(name);
            }

            throw new Exception($"Invalid expression at '{Current.Value}'");
        }

        // -------------------- FUNCTION CALL --------------------
        private ASTNode ParseFunctionCall(string name)
        {
            ExpectSymbol("(");
            var args = new List<ASTNode>();

            while (!(Current.Type == TokenType.Symbol && Current.Value == ")"))
            {
                if (Current.Type == TokenType.EndOfFile)
                    throw new Exception("Unexpected end of file in function call");

                args.Add(ParseExpression());

                if (Current.Type == TokenType.Symbol && Current.Value == ",")
                    Next();
            }

            ExpectSymbol(")");
            return new CallNode(name, args);
        }

        // -------------------- HELPERS --------------------
        private void ExpectSymbol(string symbol)
        {
            if (Current.Type != TokenType.Symbol || Current.Value != symbol)
                throw new Exception($"Expected token '{symbol}', found '{Current.Value}'");
            Next();
        }

        private Token Expect(TokenType type)
        {
            if (Current.Type != type)
                throw new Exception($"Expected {type}, found {Current.Type}");
            Token tok = Current;
            Next();
            return tok;
        }
    }
}
