# reactapp/Dockerfile
FROM node:14

WORKDIR /app

COPY bunna/package.json ./
COPY bunna/package-lock.json ./
RUN npm install

COPY bunna/. .

EXPOSE 3000
CMD ["npm", "start"]
