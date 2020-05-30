from src.main import run
from src.db import engine, Base
from src.model import Keyword

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    run()