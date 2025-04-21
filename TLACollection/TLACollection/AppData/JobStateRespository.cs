using TLACollection.Data;
using TLACollection.Models;

namespace TLACollection.AppData
{

    public interface IJobStateRespository
    {
        Task<long> GetCurrentId();
        Task SetGetCurrentId(long Id);
    }
    public class JobStateRespository : IJobStateRespository
    {
        private readonly ApplicationDbContext _context;

        public JobStateRespository(ApplicationDbContext context)
        {
            _context = context;
        }

        public async Task<long> GetCurrentId()
        {
            var item = await _context.JobStates.FindAsync("CurrentId");
            if (item == null) return 0;
            return item.CurrentId;
        }


        public async Task SetGetCurrentId(long currentId)
        {
            var item = await _context.JobStates.FindAsync("CurrentId");
            if (item == null)
            {
                await _context.JobStates.AddAsync(new JobState { CurrentId = currentId });
            }
            else
            {
                item.CurrentId = currentId;
                _context.JobStates.Update(item);
            }
            _context.SaveChanges();

        }

    }
}
