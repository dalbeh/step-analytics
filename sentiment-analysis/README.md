# Sentiment-Analysis API
### Resume

I used Python FastAPI to create the endpoint and uvicorn to host the app into a docker container over an EC2 Instance on AWS.

The model is running as an api at 
`http://3.130.255.15:8000/sentiment/$(word)`

And it's based on the following repository
`https://github.com/cloudacademy/sentiment-analysis-aws-lambda`



### How-To: Technical Information

Deploy Model:
1. Run docker compose to build/up container with all dependencies
2. Run model.py to create the model
3. Run deploy-model.sh to upload the .gz model to S3 bucket
 
Deploy Code:
1. Pull requests to this folder will trigger github actions to deploy files on s3 bucket.
2. An s3 trigger will execute the lambda `deploy-to-ec2-instance` and deploy the files into the EC2 instance where the API is running.
