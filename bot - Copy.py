import requests
import json
from web3 import Web3
import asyncio
import time
web3 = Web3(Web3.WebsocketProvider('ws://127.0.0.1:8548'))
print(web3.isConnected())
panRouterContractAddress = web3.toChecksumAddress('0x10ED43C718714eb63d5aA57B78B54704E256024E')
panabi = '[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'
spend = web3.toChecksumAddress("0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c")  #WBNB Address
busd= web3.toChecksumAddress("0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56")  #WBNB Address
usdt= web3.toChecksumAddress("0x55d398326f99059fF775485246999027B3197955")  #WBNB Address
contract = web3.eth.contract(address=panRouterContractAddress, abi=panabi)

busdadd ='e9e7cea3dedca5984780bafc599bd69add087d56'
usdtadd ='55d398326f99059ff775485246999027b3197955'
bnbadd ='bb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c'

#----------------------------------------------------------------------------------

spyContract ='0xED9C644fCe0E376F200C16ED3AA3A0973b2DAB88' 

spyContract1='0xed9c644fce0e376f200c16ed3aa3a0973b2dab88'

def BUYbnb():
    for i in range(1):
        txt = open("vi.txt").read().splitlines()[i]
        sender_address10 = txt.split("|")[0]
        private10 = txt.split("|")[1]
        nonce1 = web3.eth.get_transaction_count(sender_address10)
        amount_out_min = 0
        pancakeswap2_txn1 = contract.functions.swapExactETHForTokens(
            amount_out_min,
            [spend,tokenToBuy],
            sender_address10,
            (int(time.time()) + 10000)
            ).buildTransaction({
            'from': sender_address10,
            'value': web3.toWei(0.02,'ether'),
            'gas': 1400000,
            'gasPrice':web3.toWei('5','gwei'),
            'nonce': nonce1,
            })
        signed_txn1 = web3.eth.account.sign_transaction(pancakeswap2_txn1, private10)
        tx_token1 = web3.eth.send_raw_transaction(signed_txn1.rawTransaction)
        print(web3.toHex(tx_token1))

def BUYusdt():
    for i in range(1):
        txt = open("vi.txt").read().splitlines()[i]
        sender_address10 = txt.split("|")[0]
        private10 = txt.split("|")[1]
        nonce1 = web3.eth.get_transaction_count(sender_address10)
        amount_out_min = 0
        amount_in = 10*10**18
        pancakeswap2_txn1 = contract.functions.swapExactTokensForTokens(
            amount_in,amount_out_min,
            [usdt,tokenToBuy],
            sender_address10,
            (int(time.time()) + 10000)
            ).buildTransaction({
            'from': sender_address10,
            'gas': 1400000,
            'gasPrice':web3.toWei('5','gwei'),
            'nonce': nonce1,
            })
        signed_txn1 = web3.eth.account.sign_transaction(pancakeswap2_txn1, private10)
        tx_token1 = web3.eth.send_raw_transaction(signed_txn1.rawTransaction)
        print(web3.toHex(tx_token1))


def BUYbusd():
    for i in range(1):
        txt = open("vi.txt").read().splitlines()[i]
        sender_address10 = txt.split("|")[0]
        private10 = txt.split("|")[1]
        nonce1 = web3.eth.get_transaction_count(sender_address10)
        amount_out_min = 0
        amount_in = 10*10**18
        pancakeswap2_txn1 = contract.functions.swapExactTokensForTokens(
            amount_in,amount_out_min,
            [busd,tokenToBuy],
            sender_address10,
            (int(time.time()) + 10000)
            ).buildTransaction({
            'from': sender_address10,
            'gas': 1400000,
            'gasPrice':web3.toWei('5','gwei'),
            'nonce': nonce1,
            })
        signed_txn1 = web3.eth.account.sign_transaction(pancakeswap2_txn1, private10)
        tx_token1 = web3.eth.send_raw_transaction(signed_txn1.rawTransaction)
        print(web3.toHex(tx_token1))



def handle_event(event):
    #print(Web3.toJSON(event))
    try:
        getTrans = Web3.toJSON(event).strip('"')
        #print(web3.eth.get_transaction(getTrans))
        trans = web3.eth.get_transaction(getTrans)
        #print(trans)
        #print(trans['input'])
        data = trans['input'][0:10]
        sfrom = trans['from']
        to = trans['to']
        buyfrom = trans['input'][546:586]#64
        tokenBuy = trans['input'][610:650]#64
        print(getTrans,'***from:',sfrom,'***to:',to)
        if to == spyContract or to == spyContract1:
            tokenToBuy = web3.toChecksumAddress('0x'+tokenBuy)  
            if data =='0x91ef9ce9' or data =='0x4ddbbea0':
        #1
                if buyfrom == busdadd:
                    if tokenToBuy == bnbadd:
                        print('change coin')
                    elif tokenToBuy == usdtadd:
                        print('change coin')
                    else:
                        print('buy bang busd')
                        print('tokenToBuy',tokenToBuy)
                        BUYbusd()
                        url = 'https://api.telegram.org/bot5621470818:AAG95KWNN67jrjnrIAvhFKLVwZRzEW9LIK4/sendMessage?chat_id=-1001620047055&parse_mode=html&text=BOT VIP |' + tokenToBuy
                        r = requests.get(url)
        #2
                elif buyfrom == usdtadd:
                    if tokenToBuy == bnbadd:
                        print('change coin')
                    elif tokenToBuy == busdadd:
                        print('change coin')
                    else:
                        print('buy bang usdt')
                        print('tokenToBuy',tokenToBuy)
                        BUYusdt()
                        url = 'https://api.telegram.org/bot5621470818:AAG95KWNN67jrjnrIAvhFKLVwZRzEW9LIK4/sendMessage?chat_id=-1001620047055&parse_mode=html&text=BOT VIP |' + tokenToBuy
                        r = requests.get(url)
        #3
                elif buyfrom == bnbadd:
                    if tokenToBuy == usdtadd:
                        print('change coin')
                    elif tokenToBuy == busdadd:
                        print('change coin')
                    else:
                        print('buy bang bnb')
                        print('tokenToBuy',tokenToBuy)
                        BUYbnb()
                        url = 'https://api.telegram.org/bot5621470818:AAG95KWNN67jrjnrIAvhFKLVwZRzEW9LIK4/sendMessage?chat_id=-1001620047055&parse_mode=html&text=BOT VIP |' + tokenToBuy
                        r = requests.get(url)

    except Exception as e:
        print(f'error occurred: {e}')

        
async def log_loop(event_filter, poll_interval):
    while True:
        for PairCreated in event_filter.get_new_entries():
            handle_event(PairCreated)
        await asyncio.sleep(poll_interval)


def main():
    #block_filter = web3.eth.filter('latest')
    tx_filter = web3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
 
                # log_loop(block_filter, 2),
                log_loop(tx_filter, 2)))
    finally:
        # close loop to free up system resources
        loop.close()

main()







