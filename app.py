#!/usr/bin/env python3
from aws_cdk import App, Environment
from lambda_s3_stack import LambdaS3Stack

app = App()
LambdaS3Stack(app, "LambdaS3Stack",
              env=Environment(account="acount-id", region="us-east-1"))
app.synth()



#
# cdk bootstrap aws://account-id/us-east-1 CDK bootstrap
# 
# cdk deploy --app "python app.py" --region us-east-1