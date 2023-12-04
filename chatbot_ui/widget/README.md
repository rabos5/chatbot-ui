### build the widget
*** must have nvm, node installed
```
cd ./widget
nvm install node
npm install
npm run build:dev
cp ./dist/index.js ../static/index.js
```
- start up the chatbot_ui.py server / application