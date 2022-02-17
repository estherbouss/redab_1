"""
    addition
"""
import random
import numpy as np
from peer import Peer, MIN_CONNECTION_DURATION, MAX_CONNECTION_DURATION
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram

class PeerQ4(Peer):

    def send_data_to_backend(self):
        return np.array(list(self.peer_pool.values()))
        """
            Question 4: implement this method
        """
        

class SimulationQ4(Simulation):

    def generate_network(self):
        self.network = [PeerQ4() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        self.backend_database= np.array(self.backend_database, dtype= object)
        print(self.backend_database)
        self.backend_database= self.backend_database.flatten()
        print(self.backend_database)
        count=6
        width= int((MAX_CONNECTION_DURATION- int(MIN_CONNECTION_DURATION))/ count)
        bins= np.array([int(MIN_CONNECTION_DURATION)])
        for i in range(1, count+1):
            bins= np.append(bins, bins[i-1]+width )
        return bins
        
        

if __name__ == "__main__":

    s = SimulationQ4(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
