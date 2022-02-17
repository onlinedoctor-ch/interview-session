FROM mcr.microsoft.com/vscode/devcontainers/typescript-node

COPY ./app /app

WORKDIR /app

RUN npm install

EXPOSE 1234

CMD set -x && npm install && npm run dev