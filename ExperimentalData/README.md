# Experimental Data

This folder contains all scripts to individually run exact calculation/approximation of betweenness centrality of our approaches. The output of this is saved in JSON format and logged into stat.log.
Each folder contains all script and results for each of the used datasets.

### Folder contents

NetworkX: networkx_script.py

- This will exactly calculate the betweenness centrality and output to [date]\_networkx_exact.json
- This will do approximation of betweenness centrality using sampling/pivotting. The output of ten runs is written to [date]_networkx_approximation_[sample percentage]\_[0-10].json
- The results are saved into the subfolder "NetworkX_Results"
- Statistical results written to networkx_output.log/csv

NetworKit: networkit_script.py

- This will perform betweenness centrality estimation of all our proposed approaches:
  - Geisberger
  - Riondato
  - Kadabra
  - Bergamini
- The results are saved into the subfolder "NetworKit_Results"
- Statistical results written to networkit_output.log/csv

NetworKit: networkit_script_tuned.py

- This will perform tuned betweenness centrality estimation of all our proposed approaches.
- The results are saved into the subfolder "NetworKit_Results_Tuned"

Error Analysis:

- error_networkx.py: will calculate error measures for NetworkX estimations, output to networkit_error.csv
- error_networkit.py: will calculate error measures for NetworKit estimations, output to networkx_error.csv
- tuned.pu: will calculate error measures for tuned NetworKit estimations, output to tuned.csv

Betweenness Centrality Agreement using Tau Values:

- tau_networkx.py: will perform tau value calculation of networkx estimations, output to networkx_tau.csv
- tau_networkit.py: will perform tau value calculation of networkit estimations, output to networkit_tau.csv
- tuned.pu: will perform tau value calculation for tuned NetworKit estimations, output to tuned.csv
