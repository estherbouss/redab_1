from peer import Peer, MIN_CONNECTION_DURATION, MAX_CONNECTION_DURATION
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram
import math

class PeerQ2(Peer):

    def send_data_to_backend(self):
        return list(self.peer_pool.values())
        """
            Question 2:
            This method should return an _array_ of the peer's
            connection durations.
        """

class SimulationQ2(Simulation):

    def generate_network(self):
        self.network =  [PeerQ2() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        database=[]
        for i in self.backend_database:
            database= database + i
        self.backend_database= database
        counts= 6
        width= int((MAX_CONNECTION_DURATION- int(MIN_CONNECTION_DURATION))/ counts)
        bins=[]
        bins.append(int(MIN_CONNECTION_DURATION))
        for i in range(1,counts+1):
            bins.append(bins[i-1]+width)
        return bins
            
        
        """
            Question 2:
            This method should do all necessary processing to return
            the connection durations histogram bins counts.
            Don't call `plot_histogram` in this method, we just want
            to compute the histogram bins counts!
        """

if __name__ == "__main__":

    s = SimulationQ2(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()


    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
