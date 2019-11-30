SET PATH=%PATH%;C:\Users\Nikhil\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin
SET BUILD_NUMBER=12
SET IMAGE_NAME=gcr.io/customer-v1/customer-image:%BUILD_NUMBER%
cd C:\Users\Nikhil\Desktop\customer_service
gcloud builds submit --tag %IMAGE_NAME% .