# Student Math Score Predictor - Deployment Using AWS Elastic Beanstalk and Code Pipeline

## [Live](http://studentperformance-env.eba-5cgkamrs.eu-north-1.elasticbeanstalk.com/)

This repository contains the **Student Math Score Predictor**, a machine learning application that predicts student math scores based on various input features. This guide explains how to deploy the application using **GitHub**, **AWS Elastic Beanstalk**, and **AWS CodePipeline**.

## Prerequisites

Before proceeding, ensure you have the following:

- A GitHub account with this repository pushed.
- An AWS account.
- AWS CLI installed and configured on your machine.
- Basic knowledge of Python, Flask (or FastAPI), and AWS services.

## Project Structure

```
student-math-score-predictor/
├── application.py               # Main application script (Flask-based API)
├── model/
│   └── student_model.pkl # Trained ML model
├── static/
├── templates/
│   └── index.html       # Frontend for predictions
├── requirements.txt     # Python dependencies
├── .ebextensions/       # Elastic Beanstalk configuration files
├── buildspec.yml        # CodePipeline build instructions
└── README.md            # Deployment guide
```

## Deployment Steps

### Step 1: Push Code to GitHub

1. Clone the repository to your local machine (if not already done):

   ```bash
   git clone <repo-url>
   cd student-math-score-predictor
   ```

2. Add your project files and commit the changes:

   ```bash
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git push -u origin main
   ```
   
   ![image](https://github.com/user-attachments/assets/061277cb-25bc-43e7-a356-8177456a6eb1)


---

### Note:

Before starting deployment, create a role and a user with the steps mentioned below in AWS:

   1. To create a Role with the Required Permissions
   
   2. Go to IAM Management Console:
      - Log in to your AWS account.
      - Navigate to IAM (Identity and Access Management).
   
   3. Create a Role:
      - In the Roles section, click Create Role.
      - Select AWS Service as the trusted entity.
      - Choose EC2 as the service.
   
   4. Attach the Required Policies:
      - AWSElasticBeanstalkWebTier
      - AWSElasticBeanstalkWorkerTier
      - AWSElasticBeanstalkMulticontainerDocker
   
   5. Click Next and name the role aws-elasticbeanstalk-ec2-role
   
   6. Review the settings and click Create Role.

      ![image](https://github.com/user-attachments/assets/2d8190ae-9898-4632-a498-283f1d5ba7ab)

   6. Similarly, create a user with the same name and assign same policies. Repeat steps 3 to 5 for a user.

      ![image](https://github.com/user-attachments/assets/00abee60-3a64-43f5-89c4-d109b981b673)

   `•	The instance profile (aws-elasticbeanstalk-ec2-role) is critical because it grants permissions for Elastic Beanstalk to manage resources on behalf of your application, such as EC2 instances, CloudWatch logs, and more.`
   
   `•	The trust relationship ensures that EC2 instances can assume the role, allowing them to access the required AWS services.`
   
---


### Step 2: Set Up AWS Elastic Beanstalk

1. **Create an Elastic Beanstalk Environment**:
   - Log in to AWS Management Console.
   - Navigate to **Elastic Beanstalk**.
   - Click **Create Application**.
   - Provide a name (e.g., `student-math-score-predictor`).
   - Select **Platform** as Python and use the latest version.

2. **Upload Your Application Code**:
   - Choose **Upload your code**.
   - Upload a zipped version of your project files or configure GitHub integration.

   **Note**: Ensure the `requirements.txt` file lists all Python dependencies (e.g., Flask, scikit-learn).

3. **Deploy**:
   - Create and deploy the environment.
   - Note the environment URL provided by Elastic Beanstalk.

   ![image](https://github.com/user-attachments/assets/d70cd9a6-982e-49d9-bc92-6d6993ff6069)


---

### Step 3: Set Up AWS CodePipeline

1. **Create a Pipeline**:
   - Navigate to **AWS CodePipeline**.
   - Click **Create Pipeline**.
   - Enter a name (e.g., `StudentMathScorePipeline`).

2. **Configure Source Stage**:
   - Choose **GitHub** as the source provider.
   - Connect your GitHub account and select this repository and the `main` branch.

   ![image](https://github.com/user-attachments/assets/6e4cae9b-5e30-4a23-a80f-9915d48fadce)


3. **Add Build Stage**:
   - Use **AWS CodeBuild** to create a build project.
   - Add a `buildspec.yml` file in your project root to define build steps.

     Example `buildspec.yml`:

     ```yaml
     version: 0.2
     phases:
       install:
         commands:
           - pip install -r requirements.txt
       build:
         commands:
           - echo "Build successful!"
     ```
  
4. **Add Deploy Stage**:
   - Select **Elastic Beanstalk** as the deploy provider.
   - Choose the application and environment created in Step 2.

   
     ![image](https://github.com/user-attachments/assets/ce8b55ae-ba18-4309-a4f1-c0f5ba98b017)


5. **Review and Create**:
   - Review the pipeline stages and create the pipeline.

---

### Step 4: Test the Deployment

1. Push any change to your GitHub repository to trigger the pipeline:

   ```bash
   git add .
   git commit -m "Updated app logic"
   git push
   ```

2. Monitor the pipeline progress in AWS CodePipeline.
3. Validate the deployment by accessing the Elastic Beanstalk environment URL.

    ![image](https://github.com/user-attachments/assets/ab225296-2ba7-4314-aec0-61e58058acff)

---

### Step 5: Optional Enhancements

1. **Containerization**:
   - Use the provided `Dockerfile` to containerize your app for better portability.

     Example `Dockerfile`:
     ```dockerfile
     FROM python:3.9-slim
     WORKDIR /app
     COPY . .
     RUN pip install -r requirements.txt
     CMD ["python", "app.py"]
     ```

2. **Notifications**:
   - Set up Amazon SNS to get email notifications for pipeline status changes.

3. **Monitoring**:
   - Use Elastic Beanstalk health metrics and CloudWatch logs for monitoring and debugging.

---

## Additional Notes

- **Environment Variables**: Configure environment variables in Elastic Beanstalk for any API keys or secrets.
- **CI/CD**: The pipeline ensures continuous deployment for every GitHub push.
- **Scaling**: Elastic Beanstalk supports auto-scaling if your app needs to handle higher traffic.

---

## Connect
Connect with me on [LinkedIn](https://www.linkedin.com/in/vishalsinghblr/).

---

Feel free to raise any issues or suggestions in the repository's **Issues** tab.
