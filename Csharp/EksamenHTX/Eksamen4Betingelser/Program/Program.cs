
namespace ProgramShit
{
    class Program
    {
        int tal1;
        int tal2;
        static void Main(string[] args)
        {
            Console.WriteLine("Indtast to tal og find det største");
            Console.WriteLine("1.Tal:");
            var tal1 = Int32.Parse(Console.ReadLine());
            Console.WriteLine("2.Tal:");
            var tal2 = Int32.Parse(Console.ReadLine());

            if (tal1 > tal2)
            {
                Console.WriteLine("Tal1 er størst: " + tal1);
            } else
            {
                Console.WriteLine("Tal2 er størst: " + tal2);
            }
        }
    }
}