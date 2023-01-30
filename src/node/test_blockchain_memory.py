from src.common.initialize_default_blockchain import initialize_default_blockchain
from src.common.io_blockchain import get_blockchain_from_memory


def test_given_two_memory_reads_from_blockchain_both_yield_same_value():
    initialize_default_blockchain()
    first_block_read = get_blockchain_from_memory()
    second_block_read = get_blockchain_from_memory()
    print(first_block_read)
    assert first_block_read == second_block_read
