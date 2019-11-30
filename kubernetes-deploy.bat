SET PATH=%PATH%;C:\Users\Nikhil\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin
SET BUILD_NUMBER=53
SET IMAGE_NAME=gcr.io/handle-books/gpymicro-image:%BUILD_NUMBER%
cd C:\Users\Nikhil\Desktop\Microservices
kubectl set image deployment/py-gmicro py-gmicro=%IMAGE_NAME%