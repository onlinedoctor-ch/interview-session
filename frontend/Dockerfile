FROM node:17

COPY ./app /app

WORKDIR /app

RUN npm install

EXPOSE 1234

CMD [ "npm", "run", "dev" ]