Tech Stack Used:
- Python 3.7
- Django 3.0 (Django templating for Frontend)

Deployment
- AWS EC2
- Docker

Database
- Sqlite

User Authentication
- Session Based


Django Admin Url:
- http://3.81.119.244/admin
- Username: admin
- Password: pass1234


Manager Account Credentials:
- url: http://3.81.119.244/users/
- Username: manager
- Password: pass1234

Associate Account Credentials:
- url: http://3.81.119.244/users/
- Username: associate
- Password: pass1234


How to test ?

I have added some sample data for review. Please follow the steps below.

1. Please login to associate account using above mentioned Credentials for associate.
2. Please note down the client details like email, date_joined

3. Now, Login to manager account using above mentioned Credentials for manager 
4. You will find some data to review for same client. 
5. Please review the data (Approve, Reject). And see the respective changes in the associate dashboard again.
