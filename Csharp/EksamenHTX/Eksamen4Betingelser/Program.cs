
namespace ProgramShit
{
    class Program
    {
        int tal1;
        int tal2;
        static void Main(string[] args)
        {
            Console.WriteLine("Indtast to tal og find det største tal");
            Console.WriteLine("1.Tal:");
            var val1 = Int32.Parse(Console.ReadLine());
            Console.WriteLine("2.Tal:");
            var val2 = Int32.Parse(Console.ReadLine());

            int min = val1 < val2 ? val1 : val2;
            int max = val1 > val2 ? val1 : val2;
            Console.WriteLine($"Maximum: {max}");

            List<int> numbers = new();
            for (int i = 0; i < min; i++)
            {
                numbers.Add(i);
            }
            
            Console.WriteLine(numbers);
            foreach (var num in numbers){
                Console.WriteLine(num);
            }
        }

    }
}