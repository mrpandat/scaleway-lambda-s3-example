# scaleway-lambda-s3-example 

This repository is an exemple of a scaleway lambda.

The lambda aims to migrate files of more than a week to a different bucket.

## Requirements
	
- Install node.js
- Install [Serverless](https://serverless.com) CLI `npm install serverless -g`
- Install node Packages `npm install serverless -g`
- Install all python packages with `pip3 install -r requirements.txt --target ./package`
- You can now deploy the lambda live with `serverless deploy`
- You can see the logs with `serverless logs --function moveoldbackups`
