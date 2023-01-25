# Jablotron config helper
Just a simple Swagger hosted on Heroku to help people get the config for their Homebridge Jablotron setup.

## How to use
1. Open the terminal and make sure you are in the repo
2. Make sure Docker is running
3. run `docker build . -t jablotron-config`
4. run `docker run -p 8080:8080 -e PORT=8080 jablotron-config`
5. Open http://0.0.0.0:8080
6. Click on `try out`
7. Enter email and password for Jablonet
8. Click `execute`
9. Be patient, it can take ~10 seconds
10. Scroll down and copy the parts needed for your config

## Gotchas
If you get an error, please make sure:
1. Email and password are correct
2. Accept the terms of Jablotron, make sure you at least logged in once with the used credentials

For the associated plugin see: https://github.com/fdegier/homebridge-jablotron-alarm
