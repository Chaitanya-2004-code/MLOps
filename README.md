# 🎬 Movie AI MLOps Pipeline

An end-to-end Machine Learning Operations (MLOps) project built using Kubeflow Pipelines, Docker, Kubernetes (Kind), and Python.

This project demonstrates a complete ML workflow starting from data collection to model deployment using Kubeflow Pipeline components.

---

# Project Architecture

```
Collect Data
      │
      ▼
Clean Data
      │
      ▼
Feature Engineering
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Model Deployment
```

---

# Technologies Used

- Python 3.11
- Kubeflow Pipelines v2  https://www.kubeflow.org/docs/started/
- Docker  https://docs.docker.com/desktop/setup/install/
- Kubernetes (Kind)  
- Pandas
- Scikit-learn
- Joblib
- YAML

---

# Project Structure

```
movie-ai-model1/
│
├── components/
│   ├── collect.py
│   ├── clean.py
│   ├── feature.py
│   ├── train.py
│   ├── evaluate.py
│   └── deploy.py
│
├── pipeline.py
├── compile_pipeline.py
├── movie_ai_pipeline.yaml
│
├── Dockerfile
├── requirements.txt
├── README.md
```

---


# Installation

## Clone

```bash
git clone https://github.com/Chaitanya-2004-code/MLOps.git
cd MLOps
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

# Compile Pipeline

```bash
python compile_pipeline.py
```

This generates

```
movie_ai_pipeline.yaml
```

---

# Build Docker Image

```bash
docker build -t movie-ai:v1 .
```

---

# Create Kind Cluster

```bash
kind create cluster --name movie-ai
```

---

# Load Docker Image

```bash
kind load docker-image movie-ai:v1 --name movie-ai
```

---

# Install Kubeflow Pipelines

Install the standalone Kubeflow Pipelines manifests (follow the official Kubeflow Pipelines documentation for the version you are using).
- Kubeflow Pipelines v2  https://www.kubeflow.org/docs/started/

commands given in this is for linus convert it to windows by using any ai 
---

# Access Kubeflow UI

```bash
kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
```

Open

```
http://localhost:8080
```

---

# Run Pipeline


## How to Create / Upload Pipeline
![MLOps](https://github.com/Chaitanya-2004-code/MLOps/blob/main/asset/img1.png)

## 1. Upload

```
movie_ai_pipeline.yaml
```

##  Upload yaml
![MLOps](https://github.com/Chaitanya-2004-code/MLOps/blob/main/asset/img2.png)


## 2. Create Run

![MLOps](https://github.com/Chaitanya-2004-code/MLOps/blob/main/asset/img3.png)
## 3. Execute

![MLOps](https://github.com/Chaitanya-2004-code/MLOps/blob/main/asset/img4.png)


---

# Output

Pipeline Components

- Collect
- Clean
- Feature
- Train
- Evaluate
- Deploy

Artifacts

- Dataset
- Model
- Metrics

---

## Output
![MLOps](https://github.com/Chaitanya-2004-code/MLOps/blob/main/asset/op1.png)


![MLOps](https://github.com/Chaitanya-2004-code/MLOps/blob/main/asset/op2.png)

# Author

Chaitanya Katare
