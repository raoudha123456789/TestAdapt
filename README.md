TestAdapt/
│── README.md                ← présentation du projet
│── LICENSE                  ← licence (MIT ou Apache 2.0)
│── requirements.txt          ← dépendances Python (tensorflow, pytorch, networkx, etc.)
│── dataset/                  ← ton dataset (ou un script pour le télécharger)
│   ├── scenarios/            ← 170 scénarios
│   ├── snapshots.csv         ← 10,200 échantillons
│   └── metadata.json         ← stats, doc dataset
│── models/                   ← code des modèles
│   ├── lstm.py
│   ├── gnn.py
│   ├── hybrid.py
│   └── petri_net.py
│── framework/                ← scripts d’évaluation
│   ├── train.py
│   ├── evaluate.py
│   └── utils.py
│── examples/                 ← notebooks ou exemples d’utilisation
│   └── deadlock_detection.ipynb
└── paper/                    ← PDF mon article 
<img width="316" height="608" alt="github" src="https://github.com/user-attachments/assets/64deb677-5fb9-46a1-b734-04dd3f01120f" />
