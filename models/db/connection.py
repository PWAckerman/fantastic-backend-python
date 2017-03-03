from ming import Session, create_datastore


def connect():
    session = Session(create_datastore('mongodb://portfoliodb:a5e6e7f56c862747b51587727e1a8d3d@45.79.153.82:3431/portfoliodb'))
    return session

connection = connect()
