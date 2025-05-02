## <---------- IMPORTING REQUIRED MODULES ---------->
## Importing Flask core functions and request tools
from flask import Flask, Blueprint

 # Import Blueprint from controller
from postText.controller.controller import sentiment_bp

## <---------- INITIALIZE FLASK APP ---------->
## Creating an instance of the Flask app
app = Flask(__name__)

# ✅ Register your Blueprint
app.register_blueprint(sentiment_bp)

## <---------- APP ENTRY POINT ---------->
## Start the Flask app with debug mode enabled
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", debug=True, port=5000)


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))  # Use Render-provided port or fallback for local dev
    app.run(host='0.0.0.0', port=port, debug=True)
