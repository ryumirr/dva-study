#!/usr/bin/env python3
from aws_cdk import App, Environment
# from lambda_s3_stack_L2 import LambdaS3Stack
from lambda_s3_stack_L3 import LambdaS3Stack

app = App()
LambdaS3Stack(app, "LambdaS3Stack",
                env=Environment(account="account-id", region="us-east-1"))
app.synth()