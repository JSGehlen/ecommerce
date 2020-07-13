# E-Commerce Coffee shop

This project was built using **Django** and **Bootstrap**.

The payments are handled using a **Paypal sandbox account** and a testing account for **Stripe**.

Users can choose which payment method to use for the payments.

The project is hosted at **DigitalOcean** and the files are using **DigtalOcean's Spaces** for object storage.

Checkout the live version here:
https://ecommerce.jeremygehlen.com/

## If you would like to try this project yourself, feel free to follow these steps:

### Workflow for running the project on your local machine:
 
* Run ```pip3 install -r requirements.txt``` to install the requirements for this project
* Create a folder called "static_in_env" in the src folder
* Rename the **template.env** file to **.env** and fill in your credentials. 

```
SECRET_KEY='yoursecretkey'
DEBUG=False

DEFAULT_FROM_EMAIL= 'youremail'
NOTIFY_EMAIL= 'youremail'

// Get these keys from the PayPal Developer Dashboard

PAYPAL_CLIENT_ID='yourpaypalclientid'
PAYPAL_SECRET_KEY='yourpaypalclientid'

// Get these keys from the Stripe Dashboard

STRIPE_PUBLIC_KEY='yourstripeid'
STRIPE_SECRET_KEY='yourstripesecret'
STRIPE_WEBHOOK_SECRET='yourstripewebhooksecret'

// Get these keys from DigitalOcean API dashboard if you choose to use DigitalOceans Spaces

AWS_ACCESS_KEY_ID='yourawsacceskeyid'
AWS_SECRET_ACCESS_KEY='yoursecretaccesskeyid'
AWS_STORAGE_BUCKET_NAME='yourstoragebucketname'
AWS_S3_ENDPOINT_URL='yourendpointurl'
AWS_LOCATION= 'yourawslocation'

// Get this info from your chosen email provider

EMAIL_BACKEND = 'backendofyourchoosing'
EMAIL_USE_TSL = ''
EMAIL_HOST = 'youremailhosting provider'
EMAIL_HOST_USER = 'youremailusername'
EMAIL_HOST_PASSWORD = 'youremailhostpassword'
EMAIL_PORT = 'portnumber provided by your email provider'
EMAIL_USE_TLS = ''
```

The SECRET_KEY is a 32 character long string that is usually located in ```settings.py```, but since this project has a ```.env``` file, this key is not visible anywhere.

* Create the ```SECRET_KEY``` by running the following ``` python manage.py shell```
Then type the following commands:

```
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
'[GENERATED KEY]'
```

* Once you have the ```SECRET_KEY```, copy paste it to the ```.env``` file and run ```python manage.py migrate``` to apply the correct migrations.

 * After this you should be good to go and continue with your project
