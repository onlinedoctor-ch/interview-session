# OnlineDoctor Interview Session


## Developing using VSCode

For your convenience we provide `devcontainer` configs for both
**backend** and **frontend**. 

First install the [remote container extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). To use the configs, open two VSCode windows.

Inside VSCode execute the command (via CTRL+P) and select _`Open folder in container`_.


## About this application

This is a very basic demo application for managing doctors. The purpose
of this demo is to have a simple enough starting point for our coding
interviews while still showcasing a tech stack that is close to what
we use in our actual applications. 

![Screenshot of the demo application](./docs/screenshot_doctor_list.png)

## Architecture

This application consists of a typical three tier setup with a
database, backend and frontend. Those pieces are orchestrated
and configured via [`docker-compose (devcontainer)`](./.devcontainer/docker-compose.yml) _for the simplicity of this interview_.

![Architecture diagram of demo application](./docs/demo_app_architecture.jpg)

### Database
The postgres database has a single table for storing doctor information. 

The database client extension is preconfigured to easily view the database in VSCode.

### Backend
The backend is written in python using the FastAPI framework. It connects
to the database using the SQLAlchemy ORM.

FastAPI provides a autogenerated API testing page. When running the application
you can access this page under http://localhost:5001/docs

To run the backend, run the following commands within the [./backend/app](./backend/app) directory:

```bash
pip install -r requirements.txt

# convenience script to run uvicorn
./start.sh 
```

The backend devcontainer has a `launch.json` file that allows you to run and debug the FastAPI backend service. 

### Frontend

The frontend is written in TypeScript using React. It is built using the
parcel bundler. When running the application, the frontend is served under http://localhost:1234/.

To build and develop the frontend run the npm script `dev` inside [./frontend/app](./frontend/app) directory:
```bash
npm install

npm run dev
```

The web app is available under http://localhost:1234
