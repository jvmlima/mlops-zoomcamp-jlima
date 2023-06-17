FROM public.ecr.aws/lambda/python:3.9

# RUN pip install -U pip
# RUN pip install pipenv==2023.6.12

# COPY [ "Pipfile", "Pipfile.lock", "./" ]

# RUN pipenv install --system --deploy

# COPY [ "requirements.txt", "./" ]
# RUN pip install -r requirements.txt
RUN pip install scikit-learn==1.2.2 mlflow==2.3.1 boto3==1.26.67

COPY [ "lambda_function.py", "./" ]

CMD [ "lambda_function.lambda_handler" ]
