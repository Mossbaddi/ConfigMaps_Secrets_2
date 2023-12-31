# Process de lancement

## Prérequis

- [Docker](https://docs.docker.com/get-docker/)

## Construction de l'image Docker

```bash
docker build -t flask-app .
```

## Lancement de l'application 

### Déployez votre BDD postgresql avec kubernetes

```bash
kubectl apply -f postgresql-depl.yaml
```

### Déployez votre secret postgresql avec kubernetes (avec les variables d'environnement requises que vous trouverez en bas de ce README)

```bash
kubectl apply -f postgresql-secret.yaml
```

### Connectez-vous à votre BDD postgresql

```bash
kubectl exec -it <nom-du-pod-postgresql> -- psql -U admin 
```

### Créez votre base de données "mydatabase"

```sql
CREATE DATABASE mydatabase;
```


### Déployez votre application flask avec kubernetes

```bash
kubectl apply -f flask-depl.yaml
```


### Ajoutez des users grâce à l'api

```bash
curl http://localhost/add_user/<nom> 
```



## Configuration de la base de données

### Variables d'environnement requises

- POSTGRES_USER=admin
- POSTGRES_PASSWORD=secret

## Configuration de la base de données

### Variables d'environnement requises

PG_USER=admin
PG_PASSWORD=secret
PG_HOST=postgresql
PG_DB=mydatabase