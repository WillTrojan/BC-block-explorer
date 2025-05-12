import requests

# API Constants
BLOCKSTREAM_API_BASE = 'https://blockstream.info/api'

def get_block_info(block_hash):
    """
    Get block information from Blockstream API
    
    Args:
        block_hash (str): The hash of the block to retrieve
        
    Returns:
        dict: Block information if successful, None otherwise
    """
    url = f'{BLOCKSTREAM_API_BASE}/block/{block_hash}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_block_by_height(height):
    """
    Get block information by height from Blockstream API
    
    Args:
        height (int): The height of the block to retrieve
        
    Returns:
        dict: Block information if successful, None otherwise
    """
    url = f'{BLOCKSTREAM_API_BASE}/block-height/{height}'
    response = requests.get(url)
    if response.status_code == 200:
        block_hash = response.text.strip('"')
        return get_block_info(block_hash)
    return None

def get_transaction_info(tx_id):
    """
    Get transaction information from Blockstream API
    
    Args:
        tx_id (str): The ID of the transaction to retrieve
        
    Returns:
        dict: Transaction information if successful, None otherwise
    """
    url = f'{BLOCKSTREAM_API_BASE}/tx/{tx_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_address_info(address):
    """
    Get address information from Blockstream API
    
    Args:
        address (str): The Bitcoin address to retrieve information for
        
    Returns:
        dict: Address information if successful, None otherwise
    """
    url = f'{BLOCKSTREAM_API_BASE}/address/{address}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None