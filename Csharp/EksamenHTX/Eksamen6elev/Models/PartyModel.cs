using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Identity;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using Microsoft.AspNetCore.Http;
using System.Collections.Generic;

namespace Eksamen6elev.Models;

public class Party
{
    [Key]
    public int PartyId { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public string Location { get; set; }

    [NotMapped]
    [Display(Name = "Upload File")]
    [DataType(DataType.Upload)]
    public IFormFile Image { get; set; }
    public virtual IdentityUser CreatedByUser { get; set; }

    public virtual ICollection<IdentityUser> Attendees { get; set; }
}
