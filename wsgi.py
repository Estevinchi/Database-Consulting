import os

from dotenv import load_dotenv

from app import create_app

from app.config import DevConfig, ProdConfig

env = os.environ.get("FLASK_ENV", "development")

if env == "production":
    app = create_app(ProdConfig)
else:
    load_dotenv()
    app = create_app(DevConfig)
        
if __name__ == "__main__":
    app.run()