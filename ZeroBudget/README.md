```bash

aws cloudformation create-stack --stack-name free-tier-monitor --template-body file://./zero-dollar-budget.yaml --parameters ParameterKey=Email,ParameterValue="{MAIL ADDRESS}"


```