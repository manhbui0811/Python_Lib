using Microsoft.EntityFrameworkCore;

namespace TLACollection.AppData
{
    public class JobState
    {
        public string Id { get; set; } = "CurrentId";
        public long CurrentId { get; set; }
    }
    public class ApplicationDbContext : DbContext
    {

        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
           : base(options)
        {
        }

        public DbSet<JobState> JobStates { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);
            modelBuilder.Entity<JobState>()
                .HasKey(j => j.Id);
        }
    }


}
