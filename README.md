### Prerequisites

To run test you need to have kubectl, helm and minikuube installed on you computer. It's assumed that there's a fresh cluster

### Installation

Here are the steps 
1. Clone the repo and move into the helm charts folder: ```https://github.com/skel84/salutator.git && cd salutator/helm-charts```
2. Initialize Helm: ```helm init```
3. Wait until Helm is ready 
4. Install the salutator: ```helm install .```
5. Wait until the pods are ready. The fronted pod might fail in the first try if the DB is not ready. The process can be sped up by scaling down and up the service:
```sh
kubectl scale deployment salutator --replicas=0
kubectl scale deployment salutator --replicas=1
```
5. To get the url to use in the browser run: ```minikube service salutator --url```

### Docker files

Within the **webapp** and **database** folders there's the source code and the Dockerfiles to build the containers and reproduce the steps

