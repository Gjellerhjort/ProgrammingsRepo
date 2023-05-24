using System;
using System.ComponentModel.DataAnnotations;
using Microsoft.EntityFrameworkCore;
using MySql.EntityFrameworkCore;
//using MyDatabase;

/*

-> dotnet ef migrations add <Name> --context AppDbContext

-> dotnet ef database update --context AppDbContext

-> dotnet run 

*/

namespace PersonSearch 
{
    class Program
    {
        static void Main(string[] args)
        {
            bool Run = true;
            string ConsoleRead;
            using var dbContext = new AppDbContext();

            while (Run == true) 
            {
                ConsoleRead = Console.ReadLine();
                switch(ConsoleRead) 
                {
                    case "help":
                        Console.WriteLine("Nope");
                        break;
                    case "search":
                        Console.Write("Name:");
                        var result = dbContext.Persons.Where(x => x.Name == Console.ReadLine()).ToList();
                        foreach (Person person in result)
                        {
                            Console.WriteLine(person.Name);
                            Console.WriteLine(person.Age);
                        }
                        break;
                    case "addPerson":
                        var newPerson = new Person();

                        Console.WriteLine("Name:");
                        newPerson.Name = Console.ReadLine();
                        Console.WriteLine("Age:");
                        newPerson.Age = Int32.Parse(Console.ReadLine());
                        Console.WriteLine("City:");
                        var cities = dbContext.Cities.Where(x => x.Name == Console.ReadLine()).First();
                        City city = cities;
                        newPerson.City = city;
                        dbContext.Add(newPerson);
                        dbContext.SaveChanges();
                        break;
                    case "quit":
                        Run = false;
                        break;
                    default:
                        Console.WriteLine("What can i help with type help if needed");
                        break;
                }

            }
        }
    }
    public class Person 
    {
        [Key]
        public int PersonId { get; set; }
        public string Name { get; set; }
        public int Age { get; set; }

        public virtual City? City { get; set; }
    }
    public class City
    {
        [Key]
        public int CityId { get; set; }
        public string Name { get; set; }
        public string? Zipcode { get; set; }
 
    }
    public class AppDbContext : DbContext
    {
        public DbSet<Person> Persons { get; set; }
        public DbSet<City> Cities { get; set;}
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            string connectionString = "server=127.0.0.1;port=3306;database=Person;user=root;password=toor;";
            optionsBuilder.UseMySQL(connectionString);
        }
    }
}

