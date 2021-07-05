FROM node:12.16.1 

# set working directory
WORKDIR /usr/src/app

ENV NEXT_PUBLIC_API_URL=0.0.0.0

# install app dependencies
COPY package.json ./
COPY package-lock.json ./

RUN export NODE_OPTIONS=--max_old_space_size=8192

RUN npm i

# RUN npm install react-scripts@3.4.1 -g --silent

# add app
COPY . ./

RUN npm run build

# start app
CMD ["npm", "run", "start"]
