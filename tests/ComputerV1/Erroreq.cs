using System;

namespace ComputerV1
{
    class Erroreq : Exception
    {
        public Erroreq(string message) : base(message) { }
    }
}