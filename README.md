# ☁️ Cloud Fun Fact Generator (AWS Serverless Project)

## 📌 Project Overview
A serverless application that generates random cloud-related fun facts using AWS Lambda, API Gateway, and DynamoDB.

## 🛠 AWS Services Used
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- AWS IAM

## 🧱 Architecture
User → API Gateway → Lambda → DynamoDB

## ⚙️ How It Works
1. User sends a GET request to API Gateway
2. API Gateway triggers Lambda
3. Lambda fetches a random fact from DynamoDB
4. Response is returned in JSON format

## 🚀 Deployment Steps
1. Create DynamoDB table `CloudFunFacts`
2. Insert sample cloud fun facts
3. Create Lambda function and attach IAM role
4. Connect Lambda to API Gateway (GET method)
5. Deploy API and test endpoint

## 🧪 Sample Output
```json
{
  "id": "3",
  "fact": "AWS Lambda automatically scales based on incoming requests."
}
