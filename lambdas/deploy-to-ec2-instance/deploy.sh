# #!/bin/bash

BUCKET="lambdas-python-source-code" 
FILENAME="lambda-deploy-ec2-instance.zip" 

LAMBDA_FOLDER="$HERE/code/"
OUTPUT_FILE="zip/$FILENAME" 


# echo "Installing Dependencies"
# pip3 install -r ./code/requirements.txt -t ./code


echo "Zipping Files"
cd code
zip -r -q $FILENAME ./*
mv $FILENAME ../zip/$FILENAME
cd -


# echo "Removing Dependencies"
# mv ./code/lambda_function.py ./lambda_function.py
# mv ./code/requirements.txt ./requirements.txt
# rm -r ./code
# mkdir code
# mv ./lambda_function.py ./code/lambda_function.py 
# mv ./requirements.txt ./code/requirements.txt 


echo "Uploading to S3"
aws s3 cp $OUTPUT_FILE s3://$BUCKET/$FILENAME
echo "Done"
echo "https://s3.amazonaws.com/$BUCKET/$FILENAME"


echo "Updating Lambda Source Code"
aws lambda update-function-code --function-name deploy-to-ec2-instance --region us-east-1 --s3-bucket $BUCKET --s3-key $FILENAME
echo "Done"

echo "Removing zip File"
rm -r zip #/$OUTPUT_FILE



