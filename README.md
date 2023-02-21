# Sanarip_test

An app for farmers and local administration to collect and monitor the plots and cultures.

1. Pull the repository
2. Build a docker image:
``` docker build .```
3. Start a docker-compose:
``` docker-compose up  ```
4. After all dependencies are set you can enter: ```http://0.0.0.0:8000/```
  - list of plots can be seen only for authorised users (API)
  - users can be added by admin inside of admin panel
  - after a user has been created, you can login by clicking the button on the right corner, or enter the lhe link:```api-auth/ login/```
  - each user can see and update only the plots that belongs to him
5. You can enter admin: ```http://0.0.0.0:8000/admin/```
  - username=admin
  - password=admin
  - admin can filter and search by farmer name and culture
  - admin can set contour points (geodjango)
