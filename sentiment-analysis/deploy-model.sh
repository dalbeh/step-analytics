# #!/bin/bash

BUCKET="sentiment-analysis-gz-model" 
FILENAME="data/model.dat.gz" 

echo "Uploading to S3"
aws s3 cp $FILENAME s3://$BUCKET/$FILENAME
echo "Done"
echo "https://s3.amazonaws.com/$BUCKET/$FILENAME"