# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 11:52:12 2022

@author: bates
"""
from question2 import SimulationQ2
import histogram

s = SimulationQ2(number_of_peers=30, max_peer_pool_size=2)
s.generate_network()

s.connect_peers()

s.retrieve_data_from_peers()

a= s.process_backend_data()

b= histogram.compute_histogram_bins(s.backend_database, a)
histogram.plot_histogram(b)





