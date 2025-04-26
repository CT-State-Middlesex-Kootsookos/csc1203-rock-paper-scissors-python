from database_interface import database_interface

def test_creation():
    db = database_interface()
    assert db.read is not None
    assert db.store is not None
    assert db.file_name == "rock_paper_scissors.pl"

def test_read():
    db = database_interface()
    data = db.read()
    assert data is not None

    for key in data.keys():
        assert key is not None

def test_store():
    db = database_interface()
    data_to_store = {}
    data_to_store['EXAMPLE'] = 10
    db.store(data_to_store)

    retrieved_data = db.read()
    assert retrieved_data is not None
    assert 'EXAMPLE' in retrieved_data.keys()
    assert retrieved_data['EXAMPLE'] == 10
