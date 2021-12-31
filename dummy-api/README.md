# Dummy-Api Usage

<!-- vim-markdown-toc GFM -->

* [Requirement](#requirement)
* [Application](#application)
* [Running the application](#running-the-application)
* [Docker](#docker)

<!-- vim-markdown-toc -->

## Requirement

- Python3.x
- pip3.x

## Application

This application we have only two end point

- "/": This will show up a page with simple detail of Hosting machine name, curren application verison and a Dummy quote

- "/ping": Will return "pong!" message, for healthcheck

## Running the application

We will need to install library Flask to run this application

```bash
pip install Flask
```

Start the application with command

```bash
python app.py
```

Then we will see the response as this
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://xxx.xxx.x.xxx:105/ (Press CTRL+C to quit) # This will be your internal ip, but it isn't matter
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 124-545-183
```

Then we can open this link in our browser http://localhost:105

## Docker

- Dockerrilze command
  
  ```bash
    docker build -t dummy-api .
  ```

- Run the build image

  ```bash
      docker run -d --name dummy-container -p 105:105 dummy-api
  ```
