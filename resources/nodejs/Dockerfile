FROM node:9.11.1-slim

RUN npm install axios jest -g
RUN npm link axios
RUN npm link jest

CMD tail -f /dev/null