using System.Diagnostics;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Eksamen6elev.Models;
using Eksamen6elev.Data;
using Microsoft.AspNetCore.Identity;
namespace Eksamen6elev.Controllers;

public class HomeController : Controller
{
    private readonly ILogger<HomeController> _logger;
    private readonly ApplicationDbContext _dbContext;
    private readonly UserManager<IdentityUser> _userManager;
    public HomeController(UserManager<IdentityUser> userManager, ILogger<HomeController> logger, ApplicationDbContext dbContext)
    {
        _logger = logger;
        _dbContext = dbContext;
        _userManager = userManager;

    }
    [HttpGet]
    public IActionResult Index()
    {
        return View();
    }

    [Authorize]
    [HttpPost]
    public async Task<IActionResult> CreateParty(Party party)
    {
        if (ModelState.IsValid)
        {
            var currentUser = await _userManager.GetUserAsync(User);
            party.CreatedByUserId = currentUser.Id;
            party.Name = "MyParti";
            party.Location = "random place";
            
            _dbContext.Parties.Add(party);
            await _dbContext.SaveChangesAsync();

            return RedirectToAction("Index", "Home");
        }

        return View(party); // Return to the view with validation errors
    }

    [HttpGet]
    [Authorize]
    public IActionResult Participants()
    {
        var data = _dbContext.Parties.ToList();
        return View(data);
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
