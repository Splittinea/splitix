class Program
{
    static void Main(string[] args)
    {
        var compiler = new Compiler();
        compiler.Compile(args[0]);
    }
}