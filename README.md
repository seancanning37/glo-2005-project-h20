# glo-2005-project-h20

## Table of content

- [Getting Started](#getting-started)

	- [To run the app](#to-run-the-app)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine

### To run the app

``` bash
# install front-end
cd frontend
npm install

# serve with hot reload at localhost:8080
npm run serve


# install back-end
cd ../backend
virtualenv -p python3 venv
source venv/bin/activate
cd ..

# serve back-end at localhost:5000
python3 run.py
```

Source: <https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532>


## Notes
Le frontend run sur localhost/8080 tandis que le backend run sur localhost/5000. 

Peu importe sur lequel vous allez, vous allez voir la même chose. La seule chose différente, c'est l'icon de l'app dans le browser. Si vous voyez l'icon de Vue.js, c'est que vous êtes dans le frontend. Vous pouvez consulter la source link plus haut pour lire là-dessus



