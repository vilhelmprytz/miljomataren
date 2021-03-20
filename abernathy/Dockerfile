# abernathy (frontend)
FROM node:14-buster
LABEL author="Vilhelm Prytz" maintainer="vilhelm@prytznet.se"

COPY . /var/www/app
WORKDIR /var/www/app
RUN npm install
RUN npm run build

EXPOSE 3000
CMD npm run start
