FROM node:25.7.0-alpine3.23
WORKDIR /sample-sp
COPY ./sample-sp/package.json ./
COPY ./sample-sp/package-lock.json ./
RUN npm ci
CMD ["npm", "run", "dev"]
