
There is no spoon 
===========
There is no spoon is an application to generate adversarial images.

To use the app:
- put the image you want to change in your current directory
- run the following command and change MY_IMAGE.PNG with the name of your image
```
 sudo docker run -v $(pwd):/data there_is_no_spoon --input /data/MY_IMAGE.PNG
```