using System;
using System.Collections.Generic;
using System.Text;


namespace sLANG.Lexer
{
    public class Lexer
    {
        private readonly string _text;
        private int _pos = 0;

        private static readonly HashSet<string> Keywords = new()
        {
            "print",
            "var",
            "if",
            "else",
            "while",
            "do",
        };

        public Lexer(string text) { _text  = text; }

        public List<Token> Tokenize()
        {
            List<Token> tokens = new();

            while (_pos < _text.Length)
            {
                char current = _text[_pos];

                if (char.IsWhiteSpace(current)) { _pos++; continue; }

                if (char.IsLetter(current))
                {
                    string ident = ReadWhile(char.IsLetterOrDigit);
                    tokens.Add(Keywords.Contains(ident)
                        ? new Token(TokenType.Keyword, ident)
                        : new Token(TokenType.Identifier, ident));
                }
                else if (char.IsDigit(current))
                {
                    string number = ReadWhile(c => char.IsDigit(c) || c == '.');
                    tokens.Add(new Token(TokenType.Number, number));
                }
                else if (current == '"')
                {
                    _pos++;
                    StringBuilder sb = new();
                    while (_pos < _text.Length && _text[_pos] != '"') sb.Append(_text[_pos++]);
                    _pos++;
                    tokens.Add(new Token(TokenType.String, sb.ToString()));
                }
                else
                {
                    tokens.Add(new Token(TokenType.Symbol, current.ToString()));
                    _pos++;
                }
            }

            tokens.Add(new Token(TokenType.EndOfFile, ""));
            return tokens;
        }


        private string ReadWhile(Func<char, bool> condition)
        {
            StringBuilder sb = new();
            while(_pos < _text.Length && condition(_text[_pos]))
            {
                sb.Append(_text[_pos]);
                _pos++;
            }
            return sb.ToString();
        }
     }
}
