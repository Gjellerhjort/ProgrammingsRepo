// See https://aka.ms/new-console-template for more information
using ConsoleTables;
using System;
using System.Linq;
using System.ComponentModel.DataAnnotations;
using Microsoft.EntityFrameworkCore;
using MySql.EntityFrameworkCore;
namespace Eksamen3Salgsstatistik
{
    internal class Program
    {
        private static void GetAllBooks(AppDbContext dbContext, int ID)
        {
            var result = dbContext.Books.ToList();

            var table = new ConsoleTable(
                new ConsoleTableOptions
                {
                    Columns = new[] { "Bookname", "Quantity" },
                    EnableCount = false
                }
            );

            foreach (Book book in result)
            {
                table.AddRow(book.Name, book.Quantity);
            }

            table.Write();
        }

        public static void FindBook(AppDbContext dbContext)
        {
            Console.WriteLine("bogHandler ID: ");
            int Idinput = Int32.Parse(Console.ReadLine()?.Trim());
            Console.WriteLine("Søg efter bog: ");
            string? input = Console.ReadLine()?.Trim();

            if (input.Length == 0)
            {
                GetAllBooks(dbContext, Idinput);
                return;
            }
            else
            {
                var table = new ConsoleTable("Bookname", "Quantity");
                var book = dbContext.Books.Where(x => x.Name == input && x.BookStore.BookStoreId == Idinput).FirstOrDefault();
                if (book != null)
                {
                    table.AddRow(book.Name, book.Quantity);
                    table.Write();
                }
                else
                {
                    Console.WriteLine("Bogen med navnet {0} findes ikke", input);
                }

            }
        }


        static void Main(string[] args)
        {
            using var dbContext = new AppDbContext();
            try
            {
                FindBook(dbContext);
            }
            finally
            {
                Console.WriteLine("Done");
            }
        }
    }
    public class BookStore
    {
        [Key]
        public int BookStoreId { get; set; }
        public string Name { get; set; }
        public string Adresse { get; set; }
        public virtual List<Book>? Books { get; set; }
    }
    public class Book
    {
        [Key]
        public int BookId { get; set; }
        public string Name { get; set; }
        public int Quantity { get; set; }
        public int Price { get; set; }
        public virtual BookStore BookStore { get; set; }

    }
    public class AppDbContext : DbContext
    {
        public DbSet<BookStore> BookStores { get; set; }
        public DbSet<Book> Books { get; set; }
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            string connectionString = "server=127.0.0.1;port=3306;database=Books;user=root;password=toor;";
            optionsBuilder.UseMySQL(connectionString);
        }
    }

}