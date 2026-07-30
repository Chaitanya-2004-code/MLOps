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
- Kubeflow Pipelines v2
- Docker
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

# Workflow

## 1. Collect

Generates the movie dataset.

Output

```
Dataset
```

---

## 2. Clean

- Removes duplicates
- Removes null values

Output

```
Clean Dataset
```

---

## 3. Feature Engineering

Creates additional features.

Example

```
engagement = watch_time × liked_movie
```

---

## 4. Train

Trains a Random Forest Classifier.

Algorithm

```
RandomForestClassifier
```

Model is stored as a Kubeflow Model artifact.

---

## 5. Evaluate

Calculates

- Accuracy

Stores metrics as Kubeflow Metrics artifact.

---

## 6. Deploy

Simulates deployment of the trained model.

This component can later be extended to:

- FastAPI
- MLflow
- KServe
- AWS SageMaker

---

# Installation

## Clone

```bash
git clone <repository-url>
cd movie-ai-model1
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

1. Upload

```
movie_ai_pipeline.yaml
```

2. Create Run

3. Execute

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

# Skills Demonstrated

- MLOps
- Kubeflow Pipelines
- Kubernetes
- Docker
- Machine Learning
- Model Deployment
- Pipeline Orchestration
- Artifact Management
- Model Evaluation
- Python Development

---

# Future Improvements

- MLflow Integration
- FastAPI Deployment
- CI/CD using GitHub Actions
- Prometheus Monitoring
- Grafana Dashboard
- Model Registry
- Real-world Dataset
- Hyperparameter Tuning
- Automatic Retraining
- Cloud Deployment (AWS/GCP/Azure)

---

# Author

Chaitanya Katare
