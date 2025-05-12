# Bitcoin Block Explorer

A simple web application that allows users to explore the Bitcoin blockchain. Built with Flask and the Blockstream API.

## Features

- View recent blocks on the Bitcoin network
- Search for blocks by:
  - Block number (e.g., "1" for the Genesis Block)
  - Block hash
- Search for transactions by transaction ID
- Search for addresses to view their details
- Real-time network statistics
- Clean, modern interface

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd BC-block-explorer
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Usage

### Searching
- Enter a block number (e.g., "1" for the Genesis Block)
- Enter a block hash (64 character hexadecimal)
- Enter a transaction ID (64 character hexadecimal)
- Enter a Bitcoin address (starting with 1, 3, or bc1)

### Viewing Recent Blocks
The homepage displays the 10 most recent blocks on the Bitcoin network, including:
- Block height
- Block hash
- Timestamp
- Block size
- Number of transactions

### Network Statistics
The Network Overview section shows real-time statistics about the latest block.

## Technologies Used

- Flask - Web framework
- Blockstream API - Bitcoin blockchain data
- HTML/CSS - Frontend interface

## License

This project is licensed under the MIT License - see the LICENSE file for details. 