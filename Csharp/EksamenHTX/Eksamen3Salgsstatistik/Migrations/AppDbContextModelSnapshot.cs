﻿// <auto-generated />
using Eksamen3Salgsstatistik;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;

#nullable disable

namespace Eksamen3salgsstat.Migrations
{
    [DbContext(typeof(AppDbContext))]
    partial class AppDbContextModelSnapshot : ModelSnapshot
    {
        protected override void BuildModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "7.0.5")
                .HasAnnotation("Relational:MaxIdentifierLength", 64);

            modelBuilder.Entity("Eksamen3Salgsstatistik.Book", b =>
                {
                    b.Property<int>("BookId")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    b.Property<int>("BookStoreId")
                        .HasColumnType("int");

                    b.Property<string>("Name")
                        .IsRequired()
                        .HasColumnType("longtext");

                    b.Property<int>("Price")
                        .HasColumnType("int");

                    b.Property<int>("Quantity")
                        .HasColumnType("int");

                    b.HasKey("BookId");

                    b.HasIndex("BookStoreId");

                    b.ToTable("Books");
                });

            modelBuilder.Entity("Eksamen3Salgsstatistik.BookStore", b =>
                {
                    b.Property<int>("BookStoreId")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    b.Property<string>("Adresse")
                        .IsRequired()
                        .HasColumnType("longtext");

                    b.Property<string>("Name")
                        .IsRequired()
                        .HasColumnType("longtext");

                    b.HasKey("BookStoreId");

                    b.ToTable("BookStores");
                });

            modelBuilder.Entity("Eksamen3Salgsstatistik.Book", b =>
                {
                    b.HasOne("Eksamen3Salgsstatistik.BookStore", "BookStore")
                        .WithMany("Books")
                        .HasForeignKey("BookStoreId")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("BookStore");
                });

            modelBuilder.Entity("Eksamen3Salgsstatistik.BookStore", b =>
                {
                    b.Navigation("Books");
                });
#pragma warning restore 612, 618
        }
    }
}