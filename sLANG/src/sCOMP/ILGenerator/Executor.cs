using System;
using System.Collections.Generic;
using System.Reflection;
using System.Reflection.Emit;

namespace sCOMP.ILGenerator
{
    public class Executor
    {
        // IL Lines storage
        private List<string> ilLINES = new List<string>();

        public interface IStatement
        {
        }

        public void Run(List<IStatement> cmds)
        {
            // Creation of a dynamic Assembly
            var asmName = new AssemblyName("sLANG_DynASM");
            var asmBuilder = AssemblyBuilder.DefineDynamicAssembly(asmName, AssemblyBuilderAccess.RunAndCollect);
            var moduleBuilder = asmBuilder.DefineDynamicModule("MainModule");
            var typeBuilder = moduleBuilder.DefineType("Program", TypeAttributes.Public | TypeAttributes.Class);
            var methodBuilder = typeBuilder.DefineMethod("Main", MethodAttributes.Public | MethodAttributes.Static, typeof(void), Type.EmptyTypes);
            var ilGenerator = methodBuilder.GetILGenerator();

            // Generate IL for each statement
            foreach (var stmt in cmds)
            {
                GenerateIL(stmt, ilGenerator);
            }

            // End Method
            ilGenerator.Emit(OpCodes.Ret);

            // Create type and execute method
            var programType = typeBuilder.CreateType();
            var mainMethod = programType.GetMethod("Main");
            mainMethod.Invoke(null, null);

            // Display generated IL lines
            Console.WriteLine("================== GENERATED IL ======================");
            foreach (var line in ilLINES)
            {
                Console.WriteLine("[IL] " + line);
            }
            Console.WriteLine("=====================================================");
        }

        public void GenerateIL(IStatement stmt, ILGenerator il)
        {
            switch (stmt)
            {
                case AssignmentStatement assign:
                    il.Emit(OpCodes.Ldc_I4, assign.Value); // Load constant
                    il.Emit(OpCodes.Stloc_0);              // Store inside local variable 0
                    ilLINES.Add($"Ldc_I4 {assign.Value} -> Stloc_0");
                    break;

                case PrintStatement printStmt:
                    // Get MethodInfo for Console.WriteLine(int)
                    var writeLine = typeof(Console).GetMethod("WriteLine", new Type[] { typeof(int) });
                    il.Emit(OpCodes.Ldc_I4, printStmt.Expression); // Load value
                    il.Emit(OpCodes.Call, writeLine);             // Call Console.WriteLine
                    ilLINES.Add($"Ldc_I4 {printStmt.Expression} -> Call Console.WriteLine");
                    break;

                default:
                    il.Emit(OpCodes.Nop);
                    ilLINES.Add($"NOP // Statement type {stmt.GetType().Name} not implemented");
                    break;
            }
        }
    }
}
