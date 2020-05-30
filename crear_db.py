from src.db import engine, Base
from src.model import Keyword

def run():
    pass
if __name__ == '__main__':
    Base.metadata.create_all(engine)
    run()