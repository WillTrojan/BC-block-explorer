import requests

def get_block_info(block_hash):
    """Get block information from Blockstream API"""
    url = f'https://blockstream.info/api/block/{block_hash}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_block_by_height(height):
    """Get block information by height from Blockstream API"""
    url = f'https://blockstream.info/api/block-height/{height}'
    response = requests.get(url)
    if response.status_code == 200:
        block_hash = response.text.strip('"')
        return get_block_info(block_hash)
    return None

def get_transaction_info(tx_id):
    """Get transaction information from Blockstream API"""
    url = f'https://blockstream.info/api/tx/{tx_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_address_info(address):
    """Get address information from Blockstream API"""
    url = f'https://blockstream.info/api/address/{address}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None