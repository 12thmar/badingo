# Stage 1: Build the React app
FROM node:18 AS build

WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn install

COPY . ./
RUN yarn build

# Stage 2: Serve the React app with nginx
FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
