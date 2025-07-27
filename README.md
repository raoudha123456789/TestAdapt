TestAdapt Concurrent System Dataset

Overview

This dataset supports the TestAdapt framework for adaptive testing of intelligent concurrent systems, as described in the paper "TestAdapt: An Adaptive Dataset for Configuration and Testing of Intelligent Systems." It contains 10,200 labeled snapshots from 170 scenarios, simulating a system with 6 agents sharing 10 resources. The dataset captures task states, resource availability, hold/wait matrices, and deadlock labels, enabling research in deadlock detection and concurrent system testing.

Dataset Details
Total Snapshots: 10,200
Deadlock Snapshots: 5,100 (50%)
Non-Deadlock Snapshots: 5,100 (50%)
Scenarios: 170
Agents per Scenario: 6
Resources per Scenario: 10
Temporal Resolution: 100 ms
Scenario Duration: 600–900 ms
Format: CSV

Load the dataset using Python libraries like Pandas or Polars:

import pandas as pd
df = pd.read_csv("testadapt_snapshots.csv")
# Example: Filter deadlock snapshots
deadlock_data = df[df['deadlock_label'] == 1]

Citation

If you use this dataset, please cite:

R. Romdhani, O. Mosbahi, and M. Khalgui, "TestAdapt: An Adaptive Dataset for Configuration and Testing of Intelligent Systems," in Proc. 2025 Int. Symp. on iNnovative Informatics of Biskra (ISNIB), 2025.

License

This dataset is licensed under CC0-1.0 (Public Domain). You are free to use, modify, and distribute it without restriction.

Contact

For questions, contact romdhani.raoudha6@gmail.com.
