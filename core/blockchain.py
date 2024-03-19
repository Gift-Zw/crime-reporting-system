# blockchain.py

from web3 import Web3

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
# Load smart contract ABI
contract_abi = CRIME_REPORT_ABI
# Load contract address
contract_address = 'CONTRACT_ADDRESS'
# Create contract instance
crime_report_contract = web3.eth.contract(address=contract_address, abi=contract_abi)
# Function to create a new crime report
def create_crime_report(crime_report_data):
    # Send transaction to smart contract
    tx_hash = crime_report_contract.functions.createCrimeReport(
        crime_report_data['crimeType'],
        crime_report_data['location'],
        crime_report_data['city'],
        crime_report_data['date'],
        crime_report_data['suspectInformation'],
        crime_report_data['witnessInformation'],
        crime_report_data['reporterCell'],
        crime_report_data['description'],
        crime_report_data['status'],
        crime_report_data['assignedOfficer']
    ).transact({'from': web3.eth.accounts[0]})
    # Wait for transaction receipt
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    # Return transaction receipt
    return receipt


