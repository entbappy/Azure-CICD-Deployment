# AZURE-CICD-Deployment-with-Github-Actions

## Save pass:

PaO3V3AhADX+Iw9/E95uQ4rs1ilaCjcT2ZS+ZzXHa8+ACRCLRPa1


## Run from terminal:

docker build -t simpleapp24.azurecr.io/mltest:latest .

docker login simpleapp24.azurecr.io

docker push simpleapp24.azurecr.io/mltest:latest


## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 