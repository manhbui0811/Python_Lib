using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using TLACollection.AppData;

namespace TLACollection
{
    public class Worker : BackgroundService
    {
        private readonly ILogger<Worker> _logger;
        private readonly IJobStateRespository _jobState;

        public Worker(ILogger<Worker> logger, IJobStateRespository jobState)
        {
            _logger = logger;
            _jobState = jobState;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            _logger.LogInformation("Worker bắt đầu.");


            while (!stoppingToken.IsCancellationRequested)
            {
                var log =await _jobState.GetCurrentId();

                _logger.LogInformation("log" + log);

                await _jobState.SetGetCurrentId(30);
                await Task.Delay(5000, stoppingToken);
            }
        }
    }
}
