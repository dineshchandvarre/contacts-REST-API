### Pull Flask image from Docker hub
**********************************
sudo docker pull jcdemo/flaskapp
**********************************
### Run the container along with volume mapping and port mapping
***********************************************************
sudo docker run -v absolute_src_path:/src -p 5000:5000 -d jcdemo/flaskapp
***********************************************************
### Service is up and running now - to check
******************
sudo docker ps -a
******************
### Test service
#### GET
*****************************
curl -i http://0.0.0.0:5000/contact/<id>
*****************************
#### POST
******************************
curl -H "Content-Type: application/json" -X POST -d '{ "name": "your name", "phone": "1234567899" }' http://0.0.0.0:5000/contact/

*****************************
