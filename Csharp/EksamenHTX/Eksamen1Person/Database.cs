/*
using System.ComponentModel.DataAnnotations;
using Microsoft.EntityFrameworkCore;
using MySql.EntityFrameworkCore;


namespace MyDatabase
{
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
        public int? Zipcode { get; set; }
 
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
*/