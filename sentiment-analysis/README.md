# Sentiment-Analysis API
### Resume

This model is running as a API at `http://3.130.255.15:8000/sentiment/$(word)`

I used Python FastAPI to create the endpoint and uvicorn to host the app into a docker container over an EC2 Instance on AWS.

### How-To: Technical Information

Deploy Model:
1. Run docker compose to up container with all dependencies
2. Run model.py to create the model
3. Run deploy-model.sh to upload model to S3 bucket
 
Deploy Code:
1. Pull requests will trigger actions to deploy files on s3.
2. A lambda will be executed on s3 trigger and deploy the files into an EC2 instance where the API is running.
