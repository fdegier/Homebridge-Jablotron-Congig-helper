# Jablotron config helper
Just a simple Swagger hosted on Heroku to help people get the config for their Homebridge Jablotron setup.

## How to use
1. Open https://jablotron-config-helper-api.herokuapp.com/docs
2. Click on `try out`
3. Enter email and password for Jablonet
4. Click `execute`
5. Be patient, it can take ~10 seconds
6. Scroll down and copy the parts needed for your config

## Gotchas
If you get an error, please make sure:
1. Email and password are correct
2. Accept the terms of Jablotron, make sure you at least logged in once with the used credentials

For the associated plugin see: https://github.com/fdegier/homebridge-jablotron-alarm

### Privacy concerns
Ofcourse there is the concern of sending your password over the internet, so preferably you would use the local nodejs 
config helper. To mitigate the concern:
- access logging has been turned off
- passwords are never stored or logged
- code is open source
