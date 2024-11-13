# build stage image
FROM node:22-alpine AS build-stage

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm ci

COPY . .

RUN npm run build

# actual image
FROM nginx:alpine

# copy built files to nginx
COPY --from=build-stage /app/dist /usr/share/nginx/html
