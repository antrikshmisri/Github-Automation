# Github Automation
<img src ="https://i.imgur.com/KH1UjQq.png">
<br>

## Installation ⬇️

Download the setup for Github - Automation from [here](https://github.com/antrikshmisri/Github-Automation/releases/download/1.1/gauto.exe) or get the executable from [here](https://github.com/antrikshmisri/Github-Automation/releases/download/1.0/release-1.0.zip)

## What is it about?

Are you tired of writing the same git commands over and over again? If so, this project can help you reduce that effort significantly. The app does this by automating a lot of stuff for you. The user just has to enter the commit message for the changed file, rest the app handles everything for the user.

## Features of Github - Automation

1. Removes repition of entering same git commands
2. Displays the changed `file` along with its `diff` for making it easy to write commit messages
3. Auto pushes the files that have been commited
4. Stores the files in `JSON` file so, you can continue to commit changes later on.
5. Clean and clutter-free UI

## How does it work?

The front-end of Github - Automation is written in `ReactJS`, the logical/pseudo-backend is written in `python`. To integrate ReactJS and python script this app uses a module named `eel`. With the help of `eel`, any javascript code/framework can run a python function and get the return value if any. Learn more about eel for python [here](https://pypi.org/project/Eel/#eel).

This is not a browser based application, rather it is a standalone executable application. This is achieved by yet another module named `pyinstaller`, the `.exe` file runs the python scripts on top of the production build of the `React-App`.

## How to Run?

To run the app in development environment, follow the steps below:-

1. Get python dependencies:-
```bash
pip install -r requirements.txt
```
2. Get the node modules:-
```bash
npm install
```
3. Start the development server:-
```bash
yarn start
```

## Preview Images
<img src="./readme_images/splash.png">
<img src="./readme_images/home.png">
<img src="./readme_images/commit.png">
<img src="./readme_images/diff.png">
