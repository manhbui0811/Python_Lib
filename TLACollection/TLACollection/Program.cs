using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using TLACollection.AppData;

namespace TLACollection
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var host = CreateHostBuilder(args).Build();
            using (var scope = host.Services.CreateScope())
            {
                var services = scope.ServiceProvider;
                var dbContext = services.GetRequiredService<ApplicationDbContext>();
                var configuration = services.GetRequiredService<IConfiguration>();
                long initialId = configuration.GetValue<long>("InitialId", 1);

                InitializeDatabase(dbContext, initialId);
            }

            host.Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureServices((hostContext, services) =>
                {
                    services.AddDbContext<ApplicationDbContext>(options =>
                        options.UseSqlite($"Data Source=jobstate.db"));
                    services.AddScoped<IJobStateRespository, JobStateRespository>();
                    services.AddHostedService<Worker>();
                });

        private static void InitializeDatabase(ApplicationDbContext context, long initialId)
        {
            context.Database.EnsureCreated();
            if (!context.JobStates.Any())
            {
                context.JobStates.Add(new JobState
                {
                    Id = "CurrentId",
                    CurrentId = initialId
                });
                context.SaveChanges();
            }
        }
    }
}