from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA

def tets_blockchain_instance():
    blockchain = Blockchain()

    #Check that the first element of the blockchain is a genesis block
    assert blockchain.chain[0].hash == GENESIS_DATA['hash']

def test_add_block():
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.add_block(data)

    assert blockchain.chain[-1].data == data