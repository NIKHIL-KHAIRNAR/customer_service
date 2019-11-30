SET PATH=%PATH%;C:\Users\Nikhil\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin
SET IMAGE_NAME=gcr.io/customer-v1/customer-image:%BUILD_NUMBER%
cd C:\Users\Nikhil\Desktop\Microservices
gcloud builds submit --tag %IMAGE_NAME% .