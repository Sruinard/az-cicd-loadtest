# az-cicd-loadtest
Load test your applications with the Azure Load Testing service, Azure Functions and Github Actions.

## Summary 
This tutorial shows you how to run a loadtest using the Azure Load Testing service. We'll show how to deploy an azure function using a custom build Flights API to retrieve information about flights.
Our CICD pipeline will move through various stages, including Build, test, deploy load-test-environment, and load test on load-test-environment 

```
.
├── application
│   ├── flights
│   │   ├── flights_data.py
│   │   ├── flights_domain.py
│   │   ├── function.json
│   │   └── __init__.py
│   ├── host.json
│   ├── requirements.txt
│   ├── setup.py
│   └── tests
│       ├── __init__.py
│       └── test_flight_domain.py
├── LICENSE
├── loadtest
│   ├── config.yaml
│   └── loadtest-trips-api.jmx
└── README.md
```

## Steps to run in your own environment

### 1. Create a Service Principal and assign the correct role

create a service principal (insert values for service-principal-name and subscription-id):
```
az ad sp create-for-rbac --name "<service-principal-name>" --role contributor \
                         --scopes /subscriptions/<subscription-id> \
                         --sdk-auth
```
Copy the output and make sure you store it somewhere as we will need it later.

Assign the correct rights (i.e. Load Test Contributor) to the service principal (you can retrieve the sp-object-id from Azure Active Directory or by query):
```
az role assignment create --assignee "<sp-object-id>" \
    --role "Load Test Contributor" \
    --scope /subscriptions/<subscription-id>/resourceGroups/<resource-group-name> \
    --subscription "<subscription-id>"

```

to retrieve the sp-object-id by query:
```
az ad sp list --filter "displayname eq '<service-principal-name>'" -o table
```

### 2. Deploy application through portal, cli or IaC
- Create a loadtesting service in the azure portal
- Create an Azure function in the azure portal with python 3.8 runtime and application insights configured.

### 3. Update configurations

Update secrets:
Create a secret called AZURE_CREDENTIALS and copy the value from step `1. Create a Service Principal and assign the correct role` in it.

Create a second secret called AZURE_FUNCTIONAPP_PUBLISH_PROFILE and insert the publish profile value from your azure function. You can get this from the Azure Portal

##### [.github/workflows/main.yaml]:
Change the following values in the env section:
- AZURE_FUNCTIONAPP_NAME
- LOADTEST_RESOURCE
- RESOURCE_GROUP

#### [loadtest/loadtest-trips-api.jmx]:
Update line 33 in  with your own url from your azure function.
