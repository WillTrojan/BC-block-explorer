from flask import Flask, render_template, request
from api import get_block_info, get_transaction_info, get_address_info, get_block_by_height
import requests
from datetime import datetime

app = Flask(__name__)

@app.template_filter('datetime')
def format_datetime(timestamp):
    """Convert Unix timestamp to formatted datetime string"""
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

@app.route('/')
def index():
    # Get the latest block hash
    latest_block_url = 'https://blockstream.info/api/blocks/tip/hash'
    response = requests.get(latest_block_url)
    if response.status_code != 200:
        return render_template('index.html', recent_blocks=[], network_stats=None)
    
    latest_hash = response.text.strip('"')
    
    # Get the latest block info for network stats
    latest_block = get_block_info(latest_hash)
    if not latest_block:
        return render_template('index.html', recent_blocks=[], network_stats=None)
    
    # Get the last 10 blocks
    recent_blocks = []
    current_hash = latest_hash
    
    for _ in range(10):
        block_info = get_block_info(current_hash)
        if block_info:
            recent_blocks.append(block_info)
            current_hash = block_info.get('previousblockhash')
            if not current_hash:
                break
    
    return render_template('index.html', 
                         recent_blocks=recent_blocks,
                         network_stats=latest_block)

@app.route('/search')
def search():
    query = request.args.get('query', '').strip()
    
    if not query:
        return render_template('error.html', message='Please enter a search query')
    
    # Check if it's a Bitcoin address (starts with 1, 3, or bc1)
    if query.startswith(('1', '3', 'bc1')):
        address_info = get_address_info(query)
        if address_info:
            return render_template('address.html', address=address_info)
    
    # Check if it's a block number
    if query.isdigit():
        block_info = get_block_by_height(int(query))
        if block_info:
            return render_template('block.html', block=block_info)
    
    # Check if it's a block hash or transaction ID (64 characters, hexadecimal)
    elif len(query) == 64 and all(c in '0123456789abcdefABCDEF' for c in query):
        # Try block first
        block_info = get_block_info(query)
        if block_info:
            return render_template('block.html', block=block_info)
        
        # If not a block, try transaction
        tx_info = get_transaction_info(query)
        if tx_info:
            return render_template('transaction.html', transaction=tx_info)
    
    return render_template('error.html', message='Invalid input format')

if __name__ == '__main__':
    app.run(debug=True)