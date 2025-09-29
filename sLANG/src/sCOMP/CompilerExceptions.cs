using System;

namespace sCOMP
{
    // Custom error exceptions class
    [Serializable]
    public class InvalidDomainException : Exception
    {
        public InvalidDomainException() : base() {}
        public InvalidDomainException(string message) : base(message) {}
        public InvalidDomainException(string message, Exception inner) : base(message, inner) {}
    }
}