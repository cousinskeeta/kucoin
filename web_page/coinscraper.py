# -*- coding: utf-8 -*-
"""coinscraper_V3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JoE4d6o6h_al59wK9I0IJaLhVhK64mTL
"""

# Commented out IPython magic to ensure Python compatibility.
import requests
import pandas as pd
import time
import random
import math
import sqlite3
import numpy as np
from math import pi
import matplotlib.pyplot as plt
# %matplotlib inline
from bokeh.plotting import figure, output_file, show    
from os import mkdir, makedirs
from os.path import exists
from datetime import date
from predict_ import *
import sys
from subprocess import STDOUT, check_call, call, Popen
import pathlib

class coinscrapper(object):
  today = None
  kucoin_list = []
  technical_data = []
  fundamental_data = []
  rsi_data = []
  names = []
  todays_RSI = []
  todays_price = []
  todays_date = []
  marketcaps = []
  volumes = []
  plots = []
  log = []
  test= None
  now = date.today().strftime("%Y%m%d")
  lookup = {}

  def __init__(self, today=now, *args, **kwargs):
    super().__init__(*args, **kwargs)
    if today == self.now:
      self.today = today
    else:
      self.today = today
    self.log.append("Loading client\n")
    # self.connect_googleDrive()
    # Popen(['mkdir', "/data/images/test_dir/"])
  
  def update_list(self):
    today_ = self.today
    self.kucoin_list = ['https://coinmarketcap.com/currencies/monero/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/jarvis/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/nuls/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/function-x/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/thekey/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/deepbrain-chain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/cpchain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/swissborg/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/maker/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/fetch/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/ocean-protocol/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/oneledger/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/herocoin/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/phantasma/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/eos-force/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/akropolis/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/hypercash/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/nimiq/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/newscrypto/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/terra-sdt/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/request/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/gas/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/vid/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/blockstack/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/xensor/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/digitalbits/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/bitcoin-cash/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/neo/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/suku/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/presearch/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/orion-protocol/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/merculet/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/compound/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/neutrino-dollar/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/ampleforth/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/cargox/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/grin/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/high-performance-blockchain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/road/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/metahash/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/binance-coin/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/aurora/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/alchemy/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/paparazzi/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/dxchain-token/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/multivac/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/loom-network/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/senso/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/dock/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/digitex-futures/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/paybx/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/dragonchain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/fantom/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/dacc/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/decentraland/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/waltonchain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/dero/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/singularitynet/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/blockcloud/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/carvertical/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/noia-network/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/achain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/wirex-token/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/experty/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/revain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/travala/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/rsk-smart-bitcoin/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/dmm-governance/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/amber/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/elastos/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/synthetix-network-token/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/lukso/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/gramgold-coin/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/swipe/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/kusama/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/susd/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/ankr/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/aion/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/ethereum/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/dapp-token/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/iot-chain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/coti/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/bittorrent/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/blockport/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/spendcoin/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/fortknoxster/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/sylo/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/lockchain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/tron/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/kardiachain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/datx/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/marcopolo-protocol/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/trias/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/covesting/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/proof-of-liquidity/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/omg/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/zel/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/opacity/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/vidt-datalink/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/status/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/wax/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/kyber-network/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/dash/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/bytom/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/insolar/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/videocoin/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/arcs/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/gamb/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/cardano/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/nix/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/enecuum/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/betprotocol/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/cappasity/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/0x/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/wanchain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/nem/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/v-systems/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/cryptoindex-com-100/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/tether/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/ethereum-classic/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/crpt/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/civic/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/aelf/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/change/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/te-food/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/loki/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/decred/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/casino-betting-coin/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/tomochain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/energy-web-token/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/bitcoin-diamond/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/enjin-coin/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/constellation/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/qtum/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/bitcoin-sv/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/digibyte/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/verasity/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/telcoin/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/wink-tronbet/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/adbank/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/suterusu/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/credits/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/pundi-x/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/lympo/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/dent/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/power-ledger/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/utrust/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/tokoin/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/aergo/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/gochain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/electroneum/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/plutusdefi/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/stellar/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/xyo/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/babb/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/nano/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/chromia/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/iotex/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/dia-data/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/energi/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/waves/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/bns-token/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/zcash/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/chainlink/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/roobee/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/lisk/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/eos/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/algorand/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/just/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/xrp/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/trueflip/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/eden/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/iostoken/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/wom-protocol/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/crypto-com-coin/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/solve/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/selfkey/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/chiliz/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/harmony/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/silent-notary/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/milk-alliance/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/arpa-chain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/populous/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/bolt/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/cosmos/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/turtlecoin/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/vechain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/waves-enterprise/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/chrono-tech/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/matrix-ai-network/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/tezos/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/zilliqa/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/litecoin/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/caspian/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/doc-com/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/ontology/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/quarkchain/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/rsk-infrastructure-framework/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/kick-token/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/kucoin-shares/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/terra-luna/historical-data/?start=20200501&end=20200820',
                        'https://coinmarketcap.com/currencies/origintrail/historical-data/?start=20200501&end=20200820']
    days = [today_]*len(self.kucoin_list)
    tickers = [z.split("/")[4] for z in self.kucoin_list]
    updated = [link.replace("20200820", self.today) for link in self.kucoin_list]
    print(tickers)
    self.kucoin_list = updated
    self.names = tickers
    self.todays_date = days
    for k,v in zip(self.names, self.kucoin_list):
      self.lookup[k] = v


  def get_data(self):
    if len(self.kucoin_list) < 1:
      self.update_list()
    series = self.kucoin_list
    time.sleep(random.uniform(5, 10))
    start = time.time()
    for idx, coins in enumerate(series):
      loop = time.time()
      print(idx+1,"out of ", len(series))
      try:
        crypto_url = requests.get(coins)
        data = pd.read_html(crypto_url.text)
        self.technical_data.append(data[2])
        print("td:",data[2].head())
        self.fundamental_data.append(data[3])
        print("fd:",data[3].head())
        time.sleep(random.uniform(7, 10))
        elapsed = loop - start
        print('Success!', elapsed, 'seconds...')
        self.log.append(f'{round(elapsed/60,2)} minutes elapsed...\n')
      except:
        self.technical_data.append("Error")
        self.fundamental_data.append("Error")
        time.sleep(random.uniform(7, 10))
        elapsed = loop - start
        print("Failed.", elapsed, 'seconds...')
        self.log.append(f'Ooopps.... Somebody hating. \nWe missing the one for {coins}, \n or CMC just did not have the data')
        self.log.append(f'{round(elapsed/60,2)} minutes elapsed...\n')

  def computeRSI (self, data, time_window):
    diff = data.diff(1).dropna()  
    up_chg = 0 * diff
    down_chg = 0 * diff
    up_chg[diff > 0] = diff[ diff>0 ]
    down_chg[diff < 0] = diff[ diff < 0 ]
    up_chg_avg   = up_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    down_chg_avg = down_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    rs = abs(up_chg_avg/down_chg_avg)
    rsi = 100 - 100/(1+rs)
    self.log.append("Computing RSI\n")
    return rsi

  def preprocess(self, df):
    data = df.copy()
    data['date_'] = pd.to_datetime(data['Date'])
    data.index = pd.DatetimeIndex(data['date_'])
    data.sort_index(ascending=True, inplace=True)
    self.log.append("Prepocessing data\n")
    return data

  def get_rsi_data(self, data):
    try:
      m = data.copy()
      x = self.preprocess(m)
      x['RSI'] = self.computeRSI(x['Close**'], 14)
      r = list(x['RSI'])[-1]
      p = list(x['Close**'])[-1]
      self.rsi_data.append(x)
      self.todays_RSI.append(r)
      self.todays_price.append(p)
      self.log.append("Collecing RSI data\n")
      return x
    except:
      return None

  def plot_rsi_data(self, data, title):
    title = title
    test = data 
    r = list(test['RSI'])[-1]
    print(f'Plotting RSI ({r}) for: ', f'{title}')
    fig = plt.figure(figsize=(40,9))
    plt.plot(test.index[-14:],test.RSI[-14:])
    plt.title(f'{title}'+"-Current-RSI-"+str(r))
    plt.hlines(80,xmin=test.index[-14:].min(),  xmax=test.index[-14:].max(),colors='k', label='80')
    plt.hlines(70,xmin=test.index[-14:].min(),  xmax=test.index[-14:].max(),colors='r', label='70', linestyles='dashdot')
    plt.hlines(30,xmin=test.index[-14:].min(),  xmax=test.index[-14:].max(),colors='g', label='30', linestyles='dashdot')
    plt.hlines(20,xmin=test.index[-14:].min(),  xmax=test.index[-14:].max(),colors='b', label='20')
    plt.xlabel('Date')
    plt.ylabel('RSI_14')
    plt.legend()
    # plt.show()
    return fig


  def summary(self):
    if len(self.technical_data) < 1:
      self.get_data()
      self.pull_fundamentals()
    if len(self.todays_RSI) < 1:
      backup = [self.get_rsi_data(i) for i in self.technical_data]
      # charts = [self.plot_rsi_data(j,k) for j,k in zip(backup,self.names)]
      # print(len(charts))
      # # candles = [self.save_candlesticks(j,k) for j,k in zip(backup,self.names)]
      # for i in charts:
      #   i.show();
      #   self.plots.append(i)
      #   try:
      #     for name in self.names:
      #       if not exists(f'/data/images/{name}/'):
      #         mkdir(f'/data/images/{name}/')
      #     save_plots = [i.savefig(f'/data/images/{k}/RSI-{self.today}.png', dpi=72) for k in self.names]
      #     self.plots.append(i)
      #     self.log.append(f"Saved plot data. \n")
      #   except: 
      #     raise Exception("""Make sure you have a folder named, 'CoinScraper', and also a sub-folder named "charts\n~/content/drive/My Drive/CoinScraper/charts/""")
      #     print('Please connect to google drive to save files.')
      #     # self.connect_googleDrive()
      #     for name in self.names:
      #       if not exists(f'/images/{name}/'):
      #         mkdir(f'/data/images/{name}/')
      #     save_plots = [i.savefig(f'/data/images/{k}/RSI-{self.today}.png', dpi=72) for k in self.names]
      #     self.plots.append(i)
      #     self.log.append(f"Could not save plot data. \n")

    sum_table = pd.DataFrame()
    try:
      sum_table['Date'] = self.todays_date
      sum_table['Name'] = self.names
      sum_table['Price'] = self.todays_price
      sum_table['RSI'] = self.todays_RSI
      sum_table['MarketCap'] = self.marketcaps
      sum_table['Volume'] = self.volumes
      sum_table['URL'] = self.kucoin_list
      try:
        sum_table.fillna(0, axis=1, inplace=True)
        # sum_table.sort_values('RSI').to_csv(f'/data/summary-{self.today}.csv')
        self.log.append('Saving Data\n')
      except:
        # self.connect_googleDrive()
        sum_table.fillna(0, axis=1, inplace=True)
        # sum_table.sort_values('RSI').to_csv(f'/data/summary-{self.today}.csv')

      return sum_table.sort_values('RSI')
    except: 
      raise Exception('Error generating summary table')

  def pull_fundamentals(self):
    fund = self.fundamental_data
    for i in fund:
      try:
        marketcap = i.set_index(0).stack()[3]
        volume = i.set_index(0).stack()[4]
        self.marketcaps.append(marketcap)
        self.volumes.append(volume)
        self.log.append('Pulling fundamentals\n')
      except:
        self.marketcaps.append('Error')
        self.volumes.append('Error')
        self.log.append('Error pulling fundamentals\n')
      
  # def load_html_page():
  #   pass


  # def save_candlesticks(self, data, name):
  #   df = data
  #   name = name
  #   try:
  #     inc = df['Close**'] > df['Open*']
  #     dec = df['Open*'] > df['Close**']
  #     w = 12*60*60*1000 # half day in ms
  #     TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
  #     p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = f"{name} Price Chart")
  #     p.xaxis.major_label_orientation = pi/4
  #     p.grid.grid_line_alpha=0.3
  #     p.segment(df.index, df['High'], df.index, df['Low'], color="black")
  #     p.vbar(df.index[inc], w, df['Open*'][inc], df['Close**'][inc], fill_color="#D5E1DD", line_color="black")
  #     p.vbar(df.index[dec], w, df['Open*'][dec], df['Close**'][dec], fill_color="#F2583E", line_color="black")
  #     output_file(f"/content/drive/My Drive/CoinScraper/charts/{name}/candle-stick-{self.today}.html", title=f"{name}-{self.today}")
  #     self.log.append(f'Plotting {name} candlesticks\n')
  #     show(p)  # open a browser
  #     self.candle_sticks.append(p)
  #   except:
  #     self.log.append(f'Error plotting candlesticks for {name}\n')

  def prediction(self, name=""):
    try:
      url_link = self.lookup[name]
      print("Loaded: ", url_link)
    except:
      try:
        url_link = name
        print("Loaded: ", url_link)
      except:
        print("Error loading URL address")
      
    try:
      asset_name = name
      print("Loaded: ", asset_name)
    except:
      asset_name = name.split("/")[4]
      print("Loaded: ", asset_name)
    f = predict_(asset=url_link,name=asset_name,date=self.today)
    results = f.forecast()
    print(results)
    return results