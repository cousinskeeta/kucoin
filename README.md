# KuCoin - Coin Data Scraper
The coinscraper client was desinged to compare the top 200 supported assets on Kucoin's decentralized exchange. Each asset's historical and fundamental data is sourced from coinmarketcap.com.  

The client has a few requirements/dependecies, please see requirements.txt file.  To install the client, download the .py file and the demo notebook for Google Colab.

## Connecting to Client 
    from coinscraper import coinscrapper
    today = 'YYYYMMDD'
    client = coinscrapper(today)

The client will require google authentication, and will also require selenium webdriver. I would suggest running this client in google colab to test it out. Feel free to comment out or change any functionality.

## Pulling Summary
The .summary() method will be a generate.csv file with all the assets summaries.

    client.summary()

## Access Saved Variables
Using the client we can access the variables saved during the summary process. The variables will each contain a list relevant to each asset identified on CoinMarketCap.com under the KuCoin Exchange.

1. client.todays_date
2. client.names
3. client.todays_price
4. client.todays_RSI
5. client.marketcaps
6. client.volumes
7. client.kucoin_list

Below is an example of how to access these variables using the client.

    [42]
    variables = [client.todays_date, client.names, client.todays_price, client.todays_RSI, client.marketcaps, client.volumes, client.kucoin_list]
    for each in variables:
    print(len(each))
    [43]
    # Today's Date
    print('Run date: ', client.todays_date)
    # Tickers for Each Asset
    print('Assets pulled: ', client.names)
    # Closing Price for Each Asset
    print('Latest Price: ', client.todays_price)
    # 14 Day RSI as of Today

## Access Saved Datasets
Using the client we can also access the datasets saved during the summary process. The datasets are saved in a python list, and will contain historic data for each asset. The fundamental data and the RSI dataset are separte pythonic lists of datasets.

1. client.technical_data
2. client.fundamental_data
3. client.rsi_data

Below is an example of how to access the saved datasets using the client.
    [47]
    # Historic Price Data
    list_of_historic_data = client.technical_data 
    print('Historic Price Data: ')
    display(list_of_historic_data[0].head())
    # Fundamental Data
    list_of_fundamental_data = client.fundamental_data 
    print('\nFundamental Data: \n')
    display(list_of_fundamental_data[0].set_index(0).stack())

## Access RSI Charts
Using the client we can access the RSI Charts saved during the summary process. The charts are saved in a python list, and also saved to your authenticated google drive. The plots are the matplotlib objects that just require the .show() method.

1. client.plots
2. client.candle_sticks (coming soon)
Below is an example of how to access the saved datasets using the client.

    [50]
    list_of_charts = client.plots
    for i in list_of_charts:
    i.show()
    
## Access the Log File
Using the client we can also access the log file saved during the summary process. The log file is a text file that shows which processes are running, or errors that occur.

1. client.log (coming soon)
Below is an example of how to access the log.
<code Python>
[48]
client.log
</code>


Here is the table html generated for web:

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Name</th>
      <th>Price</th>
      <th>RSI</th>
      <th>MarketCap</th>
      <th>Volume</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20200819</td>
      <td>aurora</td>
      <td>0.010758</td>
      <td>42.187023</td>
      <td>$69,623,976 USD</td>
      <td>$11,064,328 USD</td>
      <td>https://coinmarketcap.com/currencies/aurora/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20200819</td>
      <td>eden</td>
      <td>0.003194</td>
      <td>61.808168</td>
      <td>$1,882,449 USD</td>
      <td>$98,028.04 USD</td>
      <td>https://coinmarketcap.com/currencies/eden/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20200819</td>
      <td>cargox</td>
      <td>0.018720</td>
      <td>56.580212</td>
      <td>$2,988,006 USD</td>
      <td>$25,556.41 USD</td>
      <td>https://coinmarketcap.com/currencies/cargox/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20200819</td>
      <td>plutusdefi</td>
      <td>0.279615</td>
      <td>51.926102</td>
      <td>$5,840,360 USD</td>
      <td>$4,307,851 USD</td>
      <td>https://coinmarketcap.com/currencies/plutusdefi/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20200819</td>
      <td>kyber-network</td>
      <td>1.680000</td>
      <td>51.799237</td>
      <td>$314,437,445 USD</td>
      <td>$69,980,556 USD</td>
      <td>https://coinmarketcap.com/currencies/kyber-network/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20200819</td>
      <td>waves-enterprise</td>
      <td>0.113152</td>
      <td>57.908557</td>
      <td>$4,126,606 USD</td>
      <td>$271,213 USD</td>
      <td>https://coinmarketcap.com/currencies/waves-enterprise/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20200819</td>
      <td>loom-network</td>
      <td>0.035414</td>
      <td>78.133532</td>
      <td>$30,683,517 USD</td>
      <td>$12,376,958 USD</td>
      <td>https://coinmarketcap.com/currencies/loom-network/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>7</th>
      <td>20200819</td>
      <td>aergo</td>
      <td>0.066013</td>
      <td>67.242300</td>
      <td>$16,668,105 USD</td>
      <td>$2,138,408 USD</td>
      <td>https://coinmarketcap.com/currencies/aergo/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>8</th>
      <td>20200819</td>
      <td>zcash</td>
      <td>83.250000</td>
      <td>53.969525</td>
      <td>$767,711,155 USD</td>
      <td>$474,251,401 USD</td>
      <td>https://coinmarketcap.com/currencies/zcash/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>9</th>
      <td>20200819</td>
      <td>function-x</td>
      <td>0.099583</td>
      <td>54.561607</td>
      <td>$22,469,847 USD</td>
      <td>$489,996 USD</td>
      <td>https://coinmarketcap.com/currencies/function-x/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>10</th>
      <td>20200819</td>
      <td>lockchain</td>
      <td>0.466456</td>
      <td>56.231728</td>
      <td>$6,673,619 USD</td>
      <td>$132,374 USD</td>
      <td>https://coinmarketcap.com/currencies/lockchain/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>11</th>
      <td>20200819</td>
      <td>paybx</td>
      <td>0.005499</td>
      <td>52.628953</td>
      <td>$1,548,476 USD</td>
      <td>$52,457.76 USD</td>
      <td>https://coinmarketcap.com/currencies/paybx/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>12</th>
      <td>20200819</td>
      <td>ethereum-classic</td>
      <td>6.810000</td>
      <td>46.728037</td>
      <td>$800,014,122 USD</td>
      <td>$770,540,495 USD</td>
      <td>https://coinmarketcap.com/currencies/ethereum-classic/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>13</th>
      <td>20200819</td>
      <td>crpt</td>
      <td>0.307643</td>
      <td>48.495801</td>
      <td>$31,223,141 USD</td>
      <td>$144,090 USD</td>
      <td>https://coinmarketcap.com/currencies/crpt/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20200819</td>
      <td>algorand</td>
      <td>0.597796</td>
      <td>66.299015</td>
      <td>$465,649,416 USD</td>
      <td>$283,429,562 USD</td>
      <td>https://coinmarketcap.com/currencies/algorand/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>15</th>
      <td>20200819</td>
      <td>blockport</td>
      <td>0.025856</td>
      <td>60.413404</td>
      <td>$1,440,720 USD</td>
      <td>$15,014.89 USD</td>
      <td>https://coinmarketcap.com/currencies/blockport/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>16</th>
      <td>20200819</td>
      <td>gramgold-coin</td>
      <td>18.220000</td>
      <td>NaN</td>
      <td>No Data</td>
      <td>$18,958.90 USD</td>
      <td>https://coinmarketcap.com/currencies/gramgold-coin/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>17</th>
      <td>20200819</td>
      <td>ocean-protocol</td>
      <td>0.546266</td>
      <td>70.783785</td>
      <td>$196,229,966 USD</td>
      <td>$20,099,232 USD</td>
      <td>https://coinmarketcap.com/currencies/ocean-protocol/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>18</th>
      <td>20200819</td>
      <td>decred</td>
      <td>16.650000</td>
      <td>52.548297</td>
      <td>$198,549,230 USD</td>
      <td>$5,747,849 USD</td>
      <td>https://coinmarketcap.com/currencies/decred/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20200819</td>
      <td>singularitynet</td>
      <td>0.048105</td>
      <td>69.420682</td>
      <td>$40,853,213 USD</td>
      <td>$2,231,308 USD</td>
      <td>https://coinmarketcap.com/currencies/singularitynet/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>20</th>
      <td>20200819</td>
      <td>fantom</td>
      <td>0.029771</td>
      <td>80.107353</td>
      <td>$62,865,921 USD</td>
      <td>$12,748,775 USD</td>
      <td>https://coinmarketcap.com/currencies/fantom/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>21</th>
      <td>20200819</td>
      <td>marcopolo-protocol</td>
      <td>0.061676</td>
      <td>78.222579</td>
      <td>No Data</td>
      <td>$315,053 USD</td>
      <td>https://coinmarketcap.com/currencies/marcopolo-protocol/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>22</th>
      <td>20200819</td>
      <td>wom-protocol</td>
      <td>0.178264</td>
      <td>49.254204</td>
      <td>$17,816,500 USD</td>
      <td>$2,116,774 USD</td>
      <td>https://coinmarketcap.com/currencies/wom-protocol/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>23</th>
      <td>20200819</td>
      <td>phantasma</td>
      <td>0.159935</td>
      <td>69.312095</td>
      <td>$8,973,372 USD</td>
      <td>$378,070 USD</td>
      <td>https://coinmarketcap.com/currencies/phantasma/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>24</th>
      <td>20200819</td>
      <td>dent</td>
      <td>0.000321</td>
      <td>59.732990</td>
      <td>$25,101,783 USD</td>
      <td>$572,015 USD</td>
      <td>https://coinmarketcap.com/currencies/dent/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>25</th>
      <td>20200819</td>
      <td>enecuum</td>
      <td>0.014925</td>
      <td>42.441919</td>
      <td>$1,824,208 USD</td>
      <td>$161,237 USD</td>
      <td>https://coinmarketcap.com/currencies/enecuum/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>26</th>
      <td>20200819</td>
      <td>zilliqa</td>
      <td>0.023264</td>
      <td>53.712596</td>
      <td>$229,828,699 USD</td>
      <td>$65,020,168 USD</td>
      <td>https://coinmarketcap.com/currencies/zilliqa/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>27</th>
      <td>20200819</td>
      <td>te-food</td>
      <td>0.024960</td>
      <td>59.237573</td>
      <td>$13,239,565 USD</td>
      <td>$96,368.76 USD</td>
      <td>https://coinmarketcap.com/currencies/te-food/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>28</th>
      <td>20200819</td>
      <td>datx</td>
      <td>0.000336</td>
      <td>53.429529</td>
      <td>$480,354 USD</td>
      <td>$1,380,568 USD</td>
      <td>https://coinmarketcap.com/currencies/datx/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>29</th>
      <td>20200819</td>
      <td>herocoin</td>
      <td>0.003579</td>
      <td>70.887568</td>
      <td>$675,870 USD</td>
      <td>$83,598.01 USD</td>
      <td>https://coinmarketcap.com/currencies/herocoin/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>30</th>
      <td>20200819</td>
      <td>bytom</td>
      <td>0.097534</td>
      <td>48.936949</td>
      <td>$131,149,089 USD</td>
      <td>$19,213,135 USD</td>
      <td>https://coinmarketcap.com/currencies/bytom/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>31</th>
      <td>20200819</td>
      <td>nimiq</td>
      <td>0.005105</td>
      <td>43.523934</td>
      <td>$33,311,559 USD</td>
      <td>$1,720,025 USD</td>
      <td>https://coinmarketcap.com/currencies/nimiq/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>32</th>
      <td>20200819</td>
      <td>neo</td>
      <td>15.880000</td>
      <td>70.415293</td>
      <td>$1,135,435,152 USD</td>
      <td>$358,005,447 USD</td>
      <td>https://coinmarketcap.com/currencies/neo/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>33</th>
      <td>20200819</td>
      <td>coinpoker</td>
      <td>0.003891</td>
      <td>43.889207</td>
      <td>$1,080,702 USD</td>
      <td>$8,019.00 USD</td>
      <td>https://coinmarketcap.com/currencies/coinpoker/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>34</th>
      <td>20200819</td>
      <td>akropolis</td>
      <td>0.024842</td>
      <td>53.426250</td>
      <td>$52,018,134 USD</td>
      <td>$7,146,539 USD</td>
      <td>https://coinmarketcap.com/currencies/akropolis/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>35</th>
      <td>20200819</td>
      <td>constellation</td>
      <td>0.019435</td>
      <td>57.973960</td>
      <td>$25,058,973 USD</td>
      <td>$734,789 USD</td>
      <td>https://coinmarketcap.com/currencies/constellation/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>36</th>
      <td>20200819</td>
      <td>amber</td>
      <td>0.033998</td>
      <td>58.402569</td>
      <td>$4,393,656 USD</td>
      <td>$3,416,543 USD</td>
      <td>https://coinmarketcap.com/currencies/amber/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>37</th>
      <td>20200819</td>
      <td>dock</td>
      <td>0.024320</td>
      <td>66.432841</td>
      <td>$15,118,562 USD</td>
      <td>$6,132,722 USD</td>
      <td>https://coinmarketcap.com/currencies/dock/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>38</th>
      <td>20200819</td>
      <td>synthetix-network-token</td>
      <td>6.100000</td>
      <td>66.351601</td>
      <td>$586,909,005 USD</td>
      <td>$78,777,843 USD</td>
      <td>https://coinmarketcap.com/currencies/synthetix-network-token/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>39</th>
      <td>20200819</td>
      <td>compound</td>
      <td>182.640000</td>
      <td>54.470261</td>
      <td>$463,269,378 USD</td>
      <td>$151,723,662 USD</td>
      <td>https://coinmarketcap.com/currencies/compound/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>40</th>
      <td>20200819</td>
      <td>origintrail</td>
      <td>0.249572</td>
      <td>74.481062</td>
      <td>$84,727,567 USD</td>
      <td>$990,778 USD</td>
      <td>https://coinmarketcap.com/currencies/origintrail/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>41</th>
      <td>20200819</td>
      <td>spendcoin</td>
      <td>0.004840</td>
      <td>54.573135</td>
      <td>$10,650,609 USD</td>
      <td>$442,021 USD</td>
      <td>https://coinmarketcap.com/currencies/spendcoin/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>42</th>
      <td>20200819</td>
      <td>waves</td>
      <td>4.230000</td>
      <td>86.307694</td>
      <td>$402,986,586 USD</td>
      <td>$177,176,546 USD</td>
      <td>https://coinmarketcap.com/currencies/waves/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>43</th>
      <td>20200819</td>
      <td>dxchain-token</td>
      <td>0.002140</td>
      <td>41.180402</td>
      <td>$110,704,595 USD</td>
      <td>$1,077,087 USD</td>
      <td>https://coinmarketcap.com/currencies/dxchain-token/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>44</th>
      <td>20200819</td>
      <td>babb</td>
      <td>0.000079</td>
      <td>43.910385</td>
      <td>$2,874,491 USD</td>
      <td>$182,330 USD</td>
      <td>https://coinmarketcap.com/currencies/babb/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>45</th>
      <td>20200819</td>
      <td>pundi-x</td>
      <td>0.000221</td>
      <td>57.123054</td>
      <td>$49,000,403 USD</td>
      <td>$2,932,756 USD</td>
      <td>https://coinmarketcap.com/currencies/pundi-x/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>46</th>
      <td>20200819</td>
      <td>cosmos</td>
      <td>5.670000</td>
      <td>62.405619</td>
      <td>$1,166,609,096 USD</td>
      <td>$181,972,098 USD</td>
      <td>https://coinmarketcap.com/currencies/cosmos/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>47</th>
      <td>20200819</td>
      <td>blockcloud</td>
      <td>0.000519</td>
      <td>44.795376</td>
      <td>No Data</td>
      <td>$90,868.43 USD</td>
      <td>https://coinmarketcap.com/currencies/blockcloud/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>48</th>
      <td>20200819</td>
      <td>achain</td>
      <td>0.009156</td>
      <td>60.209739</td>
      <td>$8,694,075 USD</td>
      <td>$9,717,035 USD</td>
      <td>https://coinmarketcap.com/currencies/achain/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>49</th>
      <td>20200819</td>
      <td>tether</td>
      <td>1.000000</td>
      <td>48.006160</td>
      <td>$10,012,606,114 USD</td>
      <td>$41,245,056,607 USD</td>
      <td>https://coinmarketcap.com/currencies/tether/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>50</th>
      <td>20200819</td>
      <td>wax</td>
      <td>0.055430</td>
      <td>62.230315</td>
      <td>$67,291,608 USD</td>
      <td>$3,378,665 USD</td>
      <td>https://coinmarketcap.com/currencies/wax/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>51</th>
      <td>20200819</td>
      <td>0x</td>
      <td>0.568065</td>
      <td>66.318581</td>
      <td>$375,892,799 USD</td>
      <td>$102,913,223 USD</td>
      <td>https://coinmarketcap.com/currencies/0x/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>52</th>
      <td>20200819</td>
      <td>open-platform</td>
      <td>0.001318</td>
      <td>48.255354</td>
      <td>$1,398,531 USD</td>
      <td>$304,059 USD</td>
      <td>https://coinmarketcap.com/currencies/open-platform/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>53</th>
      <td>20200819</td>
      <td>eos-force</td>
      <td>0.003993</td>
      <td>75.969180</td>
      <td>$3,678,774 USD</td>
      <td>$356,140 USD</td>
      <td>https://coinmarketcap.com/currencies/eos-force/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>54</th>
      <td>20200819</td>
      <td>experty</td>
      <td>0.043237</td>
      <td>78.990603</td>
      <td>$1,173,561 USD</td>
      <td>$59,510.71 USD</td>
      <td>https://coinmarketcap.com/currencies/experty/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>55</th>
      <td>20200819</td>
      <td>suku</td>
      <td>0.269401</td>
      <td>30.666296</td>
      <td>$19,238,710 USD</td>
      <td>$124,646 USD</td>
      <td>https://coinmarketcap.com/currencies/suku/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>56</th>
      <td>20200819</td>
      <td>trias</td>
      <td>0.001216</td>
      <td>62.298070</td>
      <td>$2,616,892 USD</td>
      <td>$1,480,214 USD</td>
      <td>https://coinmarketcap.com/currencies/trias/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>57</th>
      <td>20200819</td>
      <td>monero</td>
      <td>91.280000</td>
      <td>57.856280</td>
      <td>$1,626,258,970 USD</td>
      <td>$109,668,994 USD</td>
      <td>https://coinmarketcap.com/currencies/monero/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>58</th>
      <td>20200819</td>
      <td>nuls</td>
      <td>0.480896</td>
      <td>46.940011</td>
      <td>$40,111,347 USD</td>
      <td>$19,553,962 USD</td>
      <td>https://coinmarketcap.com/currencies/nuls/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>59</th>
      <td>20200819</td>
      <td>travala</td>
      <td>1.580000</td>
      <td>51.254027</td>
      <td>$58,120,158 USD</td>
      <td>$1,916,349 USD</td>
      <td>https://coinmarketcap.com/currencies/travala/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>60</th>
      <td>20200819</td>
      <td>betprotocol</td>
      <td>0.001852</td>
      <td>64.575857</td>
      <td>$3,467,550 USD</td>
      <td>$439,020 USD</td>
      <td>https://coinmarketcap.com/currencies/betprotocol/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>61</th>
      <td>20200819</td>
      <td>fetch</td>
      <td>0.128346</td>
      <td>63.903470</td>
      <td>$98,664,480 USD</td>
      <td>$21,531,860 USD</td>
      <td>https://coinmarketcap.com/currencies/fetch/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>62</th>
      <td>20200819</td>
      <td>just</td>
      <td>0.067530</td>
      <td>71.153636</td>
      <td>$138,636,469 USD</td>
      <td>$238,695,567 USD</td>
      <td>https://coinmarketcap.com/currencies/just/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>63</th>
      <td>20200819</td>
      <td>ethereum</td>
      <td>423.670000</td>
      <td>69.573726</td>
      <td>$46,231,829,387 USD</td>
      <td>$13,492,075,854 USD</td>
      <td>https://coinmarketcap.com/currencies/ethereum/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>64</th>
      <td>20200819</td>
      <td>v-systems</td>
      <td>0.029880</td>
      <td>55.017504</td>
      <td>$59,124,483 USD</td>
      <td>$3,230,662 USD</td>
      <td>https://coinmarketcap.com/currencies/v-systems/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>65</th>
      <td>20200819</td>
      <td>civic</td>
      <td>0.043921</td>
      <td>75.114678</td>
      <td>$27,727,749 USD</td>
      <td>$6,459,893 USD</td>
      <td>https://coinmarketcap.com/currencies/civic/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>66</th>
      <td>20200819</td>
      <td>insolar</td>
      <td>0.611427</td>
      <td>40.137144</td>
      <td>$61,139,939 USD</td>
      <td>$1,717,330 USD</td>
      <td>https://coinmarketcap.com/currencies/insolar/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>67</th>
      <td>20200819</td>
      <td>bitcoin-cash</td>
      <td>292.700000</td>
      <td>52.054866</td>
      <td>$5,452,851,760 USD</td>
      <td>$1,909,041,966 USD</td>
      <td>https://coinmarketcap.com/currencies/bitcoin-cash/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>68</th>
      <td>20200819</td>
      <td>roobee</td>
      <td>0.004670</td>
      <td>54.539693</td>
      <td>$8,729,286 USD</td>
      <td>$1,095,364 USD</td>
      <td>https://coinmarketcap.com/currencies/roobee/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>69</th>
      <td>20200819</td>
      <td>eos</td>
      <td>3.590000</td>
      <td>63.637000</td>
      <td>$3,181,727,775 USD</td>
      <td>$3,456,932,187 USD</td>
      <td>https://coinmarketcap.com/currencies/eos/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>70</th>
      <td>20200819</td>
      <td>nix</td>
      <td>0.103812</td>
      <td>46.467937</td>
      <td>$4,508,029 USD</td>
      <td>$170,510 USD</td>
      <td>https://coinmarketcap.com/currencies/nix/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>71</th>
      <td>20200819</td>
      <td>chrono-tech</td>
      <td>2.710000</td>
      <td>58.277410</td>
      <td>$1,984,590 USD</td>
      <td>$134,156 USD</td>
      <td>https://coinmarketcap.com/currencies/chrono-tech/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>72</th>
      <td>20200819</td>
      <td>coti</td>
      <td>0.080615</td>
      <td>69.639348</td>
      <td>$46,518,792 USD</td>
      <td>$14,644,086 USD</td>
      <td>https://coinmarketcap.com/currencies/coti/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>73</th>
      <td>20200819</td>
      <td>trueflip</td>
      <td>0.317285</td>
      <td>36.108653</td>
      <td>$1,995,401 USD</td>
      <td>$55,002.29 USD</td>
      <td>https://coinmarketcap.com/currencies/trueflip/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>74</th>
      <td>20200819</td>
      <td>matrix-ai-network</td>
      <td>0.017324</td>
      <td>56.857498</td>
      <td>$3,530,570 USD</td>
      <td>$102,731 USD</td>
      <td>https://coinmarketcap.com/currencies/matrix-ai-network/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>75</th>
      <td>20200819</td>
      <td>deepbrain-chain</td>
      <td>0.000936</td>
      <td>53.680313</td>
      <td>$2,821,679 USD</td>
      <td>$319,511 USD</td>
      <td>https://coinmarketcap.com/currencies/deepbrain-chain/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>76</th>
      <td>20200819</td>
      <td>nem</td>
      <td>0.074143</td>
      <td>72.089243</td>
      <td>$646,712,499 USD</td>
      <td>$23,232,379 USD</td>
      <td>https://coinmarketcap.com/currencies/nem/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>77</th>
      <td>20200819</td>
      <td>solve</td>
      <td>0.134688</td>
      <td>58.826809</td>
      <td>$43,256,908 USD</td>
      <td>$2,424,303 USD</td>
      <td>https://coinmarketcap.com/currencies/solve/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>78</th>
      <td>20200819</td>
      <td>aion</td>
      <td>0.136855</td>
      <td>67.514808</td>
      <td>$57,951,924 USD</td>
      <td>$4,658,043 USD</td>
      <td>https://coinmarketcap.com/currencies/aion/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>79</th>
      <td>20200819</td>
      <td>cardano</td>
      <td>0.129275</td>
      <td>43.395740</td>
      <td>$3,380,344,633 USD</td>
      <td>$385,602,673 USD</td>
      <td>https://coinmarketcap.com/currencies/cardano/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>80</th>
      <td>20200819</td>
      <td>binance-coin</td>
      <td>22.310000</td>
      <td>55.731620</td>
      <td>$3,257,053,406 USD</td>
      <td>$223,329,262 USD</td>
      <td>https://coinmarketcap.com/currencies/binance-coin/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>81</th>
      <td>20200819</td>
      <td>kardiachain</td>
      <td>0.038742</td>
      <td>74.803210</td>
      <td>$60,637,550 USD</td>
      <td>$7,362,741 USD</td>
      <td>https://coinmarketcap.com/currencies/kardiachain/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>82</th>
      <td>20200819</td>
      <td>orion-protocol</td>
      <td>3.720000</td>
      <td>50.218619</td>
      <td>$14,869,987 USD</td>
      <td>$4,695,003 USD</td>
      <td>https://coinmarketcap.com/currencies/orion-protocol/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>83</th>
      <td>20200819</td>
      <td>arpa-chain</td>
      <td>0.042364</td>
      <td>61.260285</td>
      <td>$33,569,752 USD</td>
      <td>$20,235,725 USD</td>
      <td>https://coinmarketcap.com/currencies/arpa-chain/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>84</th>
      <td>20200819</td>
      <td>milk-alliance</td>
      <td>0.218783</td>
      <td>NaN</td>
      <td>No Data</td>
      <td>$2,715,631 USD</td>
      <td>https://coinmarketcap.com/currencies/milk-alliance/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>85</th>
      <td>20200819</td>
      <td>videocoin</td>
      <td>0.099310</td>
      <td>41.022965</td>
      <td>$11,358,542 USD</td>
      <td>$433,623 USD</td>
      <td>https://coinmarketcap.com/currencies/videocoin/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>86</th>
      <td>20200819</td>
      <td>gas</td>
      <td>1.920000</td>
      <td>61.563659</td>
      <td>$18,058,025 USD</td>
      <td>$3,144,126 USD</td>
      <td>https://coinmarketcap.com/currencies/gas/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>87</th>
      <td>20200819</td>
      <td>wink-tronbet</td>
      <td>0.000119</td>
      <td>58.942960</td>
      <td>$34,582,488 USD</td>
      <td>$3,050,618 USD</td>
      <td>https://coinmarketcap.com/currencies/wink-tronbet/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>88</th>
      <td>20200819</td>
      <td>covesting</td>
      <td>0.443161</td>
      <td>56.735049</td>
      <td>$7,227,049 USD</td>
      <td>$37,323.82 USD</td>
      <td>https://coinmarketcap.com/currencies/covesting/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>89</th>
      <td>20200819</td>
      <td>chiliz</td>
      <td>0.016224</td>
      <td>54.184384</td>
      <td>$80,425,370 USD</td>
      <td>$19,237,348 USD</td>
      <td>https://coinmarketcap.com/currencies/chiliz/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>90</th>
      <td>20200819</td>
      <td>telcoin</td>
      <td>0.000281</td>
      <td>50.097905</td>
      <td>$13,301,493 USD</td>
      <td>$197,084 USD</td>
      <td>https://coinmarketcap.com/currencies/telcoin/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>91</th>
      <td>20200819</td>
      <td>paparazzi</td>
      <td>0.079124</td>
      <td>47.769460</td>
      <td>No Data</td>
      <td>$645,278 USD</td>
      <td>https://coinmarketcap.com/currencies/paparazzi/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>92</th>
      <td>20200819</td>
      <td>bitcoin</td>
      <td>11991.230000</td>
      <td>64.103790</td>
      <td>$217,704,473,884 USD</td>
      <td>$24,660,789,051 USD</td>
      <td>https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>93</th>
      <td>20200819</td>
      <td>susd</td>
      <td>1.040000</td>
      <td>57.792976</td>
      <td>$23,322,670 USD</td>
      <td>$2,146,847 USD</td>
      <td>https://coinmarketcap.com/currencies/susd/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>94</th>
      <td>20200819</td>
      <td>metahash</td>
      <td>0.004851</td>
      <td>51.975663</td>
      <td>$9,881,737 USD</td>
      <td>$4,505,357 USD</td>
      <td>https://coinmarketcap.com/currencies/metahash/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>95</th>
      <td>20200819</td>
      <td>zel</td>
      <td>0.045294</td>
      <td>56.902038</td>
      <td>$5,031,042 USD</td>
      <td>$2,674,817 USD</td>
      <td>https://coinmarketcap.com/currencies/zel/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>96</th>
      <td>20200819</td>
      <td>bitcoin-sv</td>
      <td>217.300000</td>
      <td>52.081909</td>
      <td>$3,859,407,825 USD</td>
      <td>$945,951,075 USD</td>
      <td>https://coinmarketcap.com/currencies/bitcoin-sv/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>97</th>
      <td>20200819</td>
      <td>dacc</td>
      <td>0.000066</td>
      <td>74.520933</td>
      <td>No Data</td>
      <td>$87,700.87 USD</td>
      <td>https://coinmarketcap.com/currencies/dacc/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>98</th>
      <td>20200819</td>
      <td>swipe</td>
      <td>3.600000</td>
      <td>65.544277</td>
      <td>$214,697,172 USD</td>
      <td>$308,010,891 USD</td>
      <td>https://coinmarketcap.com/currencies/swipe/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>99</th>
      <td>20200819</td>
      <td>digibyte</td>
      <td>0.031571</td>
      <td>56.615198</td>
      <td>$427,597,409 USD</td>
      <td>$15,086,748 USD</td>
      <td>https://coinmarketcap.com/currencies/digibyte/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>100</th>
      <td>20200819</td>
      <td>road</td>
      <td>0.148245</td>
      <td>82.996848</td>
      <td>$10,588,242 USD</td>
      <td>$1,302,841 USD</td>
      <td>https://coinmarketcap.com/currencies/road/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>101</th>
      <td>20200819</td>
      <td>populous</td>
      <td>0.376133</td>
      <td>54.331287</td>
      <td>$20,220,629 USD</td>
      <td>$1,917,446 USD</td>
      <td>https://coinmarketcap.com/currencies/populous/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>102</th>
      <td>20200819</td>
      <td>energy-web-token</td>
      <td>12.650000</td>
      <td>69.573331</td>
      <td>$372,054,941 USD</td>
      <td>$2,597,693 USD</td>
      <td>https://coinmarketcap.com/currencies/energy-web-token/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>103</th>
      <td>20200819</td>
      <td>verasity</td>
      <td>0.000926</td>
      <td>47.880857</td>
      <td>$3,630,591 USD</td>
      <td>$758,521 USD</td>
      <td>https://coinmarketcap.com/currencies/verasity/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>104</th>
      <td>20200819</td>
      <td>selfkey</td>
      <td>0.002052</td>
      <td>63.448247</td>
      <td>$5,864,234 USD</td>
      <td>$491,969 USD</td>
      <td>https://coinmarketcap.com/currencies/selfkey/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>105</th>
      <td>20200819</td>
      <td>enjin-coin</td>
      <td>0.208457</td>
      <td>56.008595</td>
      <td>$163,239,963 USD</td>
      <td>$10,651,899 USD</td>
      <td>https://coinmarketcap.com/currencies/enjin-coin/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>106</th>
      <td>20200819</td>
      <td>tokoin</td>
      <td>0.029876</td>
      <td>64.888120</td>
      <td>$5,319,740 USD</td>
      <td>$727,993 USD</td>
      <td>https://coinmarketcap.com/currencies/tokoin/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>107</th>
      <td>20200819</td>
      <td>senso</td>
      <td>0.234230</td>
      <td>75.437321</td>
      <td>No Data</td>
      <td>$1,166,825 USD</td>
      <td>https://coinmarketcap.com/currencies/senso/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>108</th>
      <td>20200819</td>
      <td>blockstack</td>
      <td>0.244119</td>
      <td>55.203230</td>
      <td>$143,547,860 USD</td>
      <td>$2,394,258 USD</td>
      <td>https://coinmarketcap.com/currencies/blockstack/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>109</th>
      <td>20200819</td>
      <td>maker</td>
      <td>652.400000</td>
      <td>55.082967</td>
      <td>$664,523,341 USD</td>
      <td>$32,958,773 USD</td>
      <td>https://coinmarketcap.com/currencies/maker/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>110</th>
      <td>20200819</td>
      <td>caspian</td>
      <td>0.007929</td>
      <td>73.471649</td>
      <td>$3,349,506 USD</td>
      <td>$69,329.56 USD</td>
      <td>https://coinmarketcap.com/currencies/caspian/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>111</th>
      <td>20200819</td>
      <td>waltonchain</td>
      <td>0.599800</td>
      <td>63.236152</td>
      <td>$42,996,238 USD</td>
      <td>$13,238,414 USD</td>
      <td>https://coinmarketcap.com/currencies/waltonchain/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>112</th>
      <td>20200819</td>
      <td>gochain</td>
      <td>0.013506</td>
      <td>55.017675</td>
      <td>$13,713,995 USD</td>
      <td>$1,118,029 USD</td>
      <td>https://coinmarketcap.com/currencies/gochain/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>113</th>
      <td>20200819</td>
      <td>rsk-infrastructure-framework</td>
      <td>0.093400</td>
      <td>49.670678</td>
      <td>$59,950,071 USD</td>
      <td>$449,415 USD</td>
      <td>https://coinmarketcap.com/currencies/rsk-infrastructure-framework/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>114</th>
      <td>20200819</td>
      <td>arcs</td>
      <td>0.309132</td>
      <td>54.433845</td>
      <td>No Data</td>
      <td>$246,999 USD</td>
      <td>https://coinmarketcap.com/currencies/arcs/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>115</th>
      <td>20200819</td>
      <td>ontology</td>
      <td>0.847864</td>
      <td>60.292969</td>
      <td>$551,148,398 USD</td>
      <td>$161,951,360 USD</td>
      <td>https://coinmarketcap.com/currencies/ontology/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>116</th>
      <td>20200819</td>
      <td>bitcoin-diamond</td>
      <td>0.781193</td>
      <td>38.494466</td>
      <td>$146,083,061 USD</td>
      <td>$5,471,707 USD</td>
      <td>https://coinmarketcap.com/currencies/bitcoin-diamond/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>117</th>
      <td>20200819</td>
      <td>xyo</td>
      <td>0.000588</td>
      <td>47.848966</td>
      <td>$7,648,505 USD</td>
      <td>$78,582.71 USD</td>
      <td>https://coinmarketcap.com/currencies/xyo/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>118</th>
      <td>20200819</td>
      <td>status</td>
      <td>0.033052</td>
      <td>57.702233</td>
      <td>$114,675,774 USD</td>
      <td>$16,049,560 USD</td>
      <td>https://coinmarketcap.com/currencies/status/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>119</th>
      <td>20200819</td>
      <td>qtum</td>
      <td>3.300000</td>
      <td>68.623432</td>
      <td>$326,284,054 USD</td>
      <td>$510,757,120 USD</td>
      <td>https://coinmarketcap.com/currencies/qtum/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>120</th>
      <td>20200819</td>
      <td>power-ledger</td>
      <td>0.105540</td>
      <td>58.166806</td>
      <td>$41,873,455 USD</td>
      <td>$4,086,907 USD</td>
      <td>https://coinmarketcap.com/currencies/power-ledger/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>121</th>
      <td>20200819</td>
      <td>proof-of-liquidity</td>
      <td>0.026190</td>
      <td>NaN</td>
      <td>No Data</td>
      <td>$141,787 USD</td>
      <td>https://coinmarketcap.com/currencies/proof-of-liquidity/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>122</th>
      <td>20200819</td>
      <td>dia-data</td>
      <td>3.330000</td>
      <td>65.709989</td>
      <td>$34,936,983 USD</td>
      <td>$38,299,166 USD</td>
      <td>https://coinmarketcap.com/currencies/dia-data/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>123</th>
      <td>20200819</td>
      <td>xensor</td>
      <td>0.012079</td>
      <td>26.901465</td>
      <td>$23,709,311 USD</td>
      <td>$4,350,334 USD</td>
      <td>https://coinmarketcap.com/currencies/xensor/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>124</th>
      <td>20200819</td>
      <td>swissborg</td>
      <td>0.108919</td>
      <td>45.831826</td>
      <td>$78,286,450 USD</td>
      <td>$801,808 USD</td>
      <td>https://coinmarketcap.com/currencies/swissborg/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>125</th>
      <td>20200819</td>
      <td>harmony</td>
      <td>0.011592</td>
      <td>60.967367</td>
      <td>$69,774,129 USD</td>
      <td>$15,548,452 USD</td>
      <td>https://coinmarketcap.com/currencies/harmony/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>126</th>
      <td>20200819</td>
      <td>chromia</td>
      <td>0.069011</td>
      <td>56.281851</td>
      <td>$26,106,789 USD</td>
      <td>$5,742,027 USD</td>
      <td>https://coinmarketcap.com/currencies/chromia/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>127</th>
      <td>20200819</td>
      <td>turtlecoin</td>
      <td>0.000019</td>
      <td>49.960462</td>
      <td>$1,567,939 USD</td>
      <td>$799,631 USD</td>
      <td>https://coinmarketcap.com/currencies/turtlecoin/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>128</th>
      <td>20200819</td>
      <td>thekey</td>
      <td>0.000520</td>
      <td>55.082818</td>
      <td>$3,145,495 USD</td>
      <td>$28,149.12 USD</td>
      <td>https://coinmarketcap.com/currencies/thekey/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>129</th>
      <td>20200819</td>
      <td>dero</td>
      <td>0.960014</td>
      <td>39.917180</td>
      <td>$9,565,319 USD</td>
      <td>$690,346 USD</td>
      <td>https://coinmarketcap.com/currencies/dero/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>130</th>
      <td>20200819</td>
      <td>kucoin-shares</td>
      <td>1.230000</td>
      <td>70.777558</td>
      <td>$99,922,704 USD</td>
      <td>$7,986,902 USD</td>
      <td>https://coinmarketcap.com/currencies/kucoin-shares/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>131</th>
      <td>20200819</td>
      <td>alchemy</td>
      <td>1.300000</td>
      <td>62.037949</td>
      <td>No Data</td>
      <td>$3,995.16 USD</td>
      <td>https://coinmarketcap.com/currencies/alchemy/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>132</th>
      <td>20200819</td>
      <td>dash</td>
      <td>88.130000</td>
      <td>49.233298</td>
      <td>$858,621,846 USD</td>
      <td>$290,894,329 USD</td>
      <td>https://coinmarketcap.com/currencies/dash/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>133</th>
      <td>20200819</td>
      <td>silent-notary</td>
      <td>0.000003</td>
      <td>57.174455</td>
      <td>$223,266 USD</td>
      <td>$18,969.96 USD</td>
      <td>https://coinmarketcap.com/currencies/silent-notary/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>134</th>
      <td>20200819</td>
      <td>dragonchain</td>
      <td>0.091351</td>
      <td>60.114811</td>
      <td>$28,350,773 USD</td>
      <td>$302,433 USD</td>
      <td>https://coinmarketcap.com/currencies/dragonchain/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>135</th>
      <td>20200819</td>
      <td>cryptoindex-com-100</td>
      <td>0.181718</td>
      <td>55.434549</td>
      <td>$29,155,320 USD</td>
      <td>$114,925 USD</td>
      <td>https://coinmarketcap.com/currencies/cryptoindex-com-100/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>136</th>
      <td>20200819</td>
      <td>xrp</td>
      <td>0.303307</td>
      <td>65.850872</td>
      <td>$13,117,444,477 USD</td>
      <td>$2,175,812,285 USD</td>
      <td>https://coinmarketcap.com/currencies/xrp/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>137</th>
      <td>20200819</td>
      <td>adbank</td>
      <td>0.002023</td>
      <td>43.496757</td>
      <td>$1,490,619 USD</td>
      <td>$32,978.28 USD</td>
      <td>https://coinmarketcap.com/currencies/adbank/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>138</th>
      <td>20200819</td>
      <td>pivx</td>
      <td>0.520000</td>
      <td>61.370261</td>
      <td>$27,245,636 USD</td>
      <td>$585,937 USD</td>
      <td>https://coinmarketcap.com/currencies/pivx/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>139</th>
      <td>20200819</td>
      <td>grin</td>
      <td>0.551634</td>
      <td>49.160245</td>
      <td>$27,674,999 USD</td>
      <td>$8,862,655 USD</td>
      <td>https://coinmarketcap.com/currencies/grin/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>140</th>
      <td>20200819</td>
      <td>cpchain</td>
      <td>0.002536</td>
      <td>49.635909</td>
      <td>$885,171 USD</td>
      <td>$76,524.58 USD</td>
      <td>https://coinmarketcap.com/currencies/cpchain/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>141</th>
      <td>20200819</td>
      <td>suterusu</td>
      <td>0.010305</td>
      <td>53.526615</td>
      <td>$12,615,384 USD</td>
      <td>$2,391,079 USD</td>
      <td>https://coinmarketcap.com/currencies/suterusu/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>142</th>
      <td>20200819</td>
      <td>stellar</td>
      <td>0.102548</td>
      <td>49.704844</td>
      <td>$2,123,652,190 USD</td>
      <td>$253,496,286 USD</td>
      <td>https://coinmarketcap.com/currencies/stellar/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>143</th>
      <td>20200819</td>
      <td>iostoken</td>
      <td>0.007254</td>
      <td>66.402563</td>
      <td>$104,609,209 USD</td>
      <td>$75,252,092 USD</td>
      <td>https://coinmarketcap.com/currencies/iostoken/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>144</th>
      <td>20200819</td>
      <td>doc-com</td>
      <td>0.003284</td>
      <td>38.149920</td>
      <td>$2,509,925 USD</td>
      <td>$20,095.20 USD</td>
      <td>https://coinmarketcap.com/currencies/doc-com/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>145</th>
      <td>20200819</td>
      <td>tomochain</td>
      <td>1.140000</td>
      <td>52.018933</td>
      <td>$81,804,878 USD</td>
      <td>$11,200,140 USD</td>
      <td>https://coinmarketcap.com/currencies/tomochain/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>146</th>
      <td>20200819</td>
      <td>merculet</td>
      <td>0.000650</td>
      <td>53.674087</td>
      <td>$2,773,114 USD</td>
      <td>$128,778 USD</td>
      <td>https://coinmarketcap.com/currencies/merculet/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>147</th>
      <td>20200819</td>
      <td>ampleforth</td>
      <td>0.604262</td>
      <td>39.054462</td>
      <td>$132,461,703 USD</td>
      <td>$15,015,613 USD</td>
      <td>https://coinmarketcap.com/currencies/ampleforth/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>148</th>
      <td>20200819</td>
      <td>decentraland</td>
      <td>0.083199</td>
      <td>56.475205</td>
      <td>$118,808,802 USD</td>
      <td>$21,561,149 USD</td>
      <td>https://coinmarketcap.com/currencies/decentraland/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>149</th>
      <td>20200819</td>
      <td>bns-token</td>
      <td>0.086560</td>
      <td>74.002146</td>
      <td>No Data</td>
      <td>$750,346 USD</td>
      <td>https://coinmarketcap.com/currencies/bns-token/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>150</th>
      <td>20200819</td>
      <td>amino-network</td>
      <td>0.003098</td>
      <td>49.019397</td>
      <td>$147,233 USD</td>
      <td>$36,091.64 USD</td>
      <td>https://coinmarketcap.com/currencies/amino-network/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>151</th>
      <td>20200819</td>
      <td>vid</td>
      <td>0.344210</td>
      <td>38.538634</td>
      <td>$9,566,933 USD</td>
      <td>$875,742 USD</td>
      <td>https://coinmarketcap.com/currencies/vid/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>152</th>
      <td>20200819</td>
      <td>revain</td>
      <td>0.010725</td>
      <td>56.183432</td>
      <td>$32,034,160 USD</td>
      <td>$1,281,464 USD</td>
      <td>https://coinmarketcap.com/currencies/revain/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>153</th>
      <td>20200819</td>
      <td>dapp-token</td>
      <td>0.001427</td>
      <td>53.436097</td>
      <td>No Data</td>
      <td>$246,175 USD</td>
      <td>https://coinmarketcap.com/currencies/dapp-token/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>154</th>
      <td>20200819</td>
      <td>iotex</td>
      <td>0.008735</td>
      <td>58.626283</td>
      <td>$42,051,924 USD</td>
      <td>$4,599,873 USD</td>
      <td>https://coinmarketcap.com/currencies/iotex/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>155</th>
      <td>20200819</td>
      <td>omg</td>
      <td>2.710000</td>
      <td>77.477847</td>
      <td>$464,504,890 USD</td>
      <td>$594,019,127 USD</td>
      <td>https://coinmarketcap.com/currencies/omg/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>156</th>
      <td>20200819</td>
      <td>high-performance-blockchain</td>
      <td>0.345251</td>
      <td>75.600443</td>
      <td>$19,990,836 USD</td>
      <td>$1,056,425 USD</td>
      <td>https://coinmarketcap.com/currencies/high-performance-blockchain/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>157</th>
      <td>20200819</td>
      <td>presearch</td>
      <td>0.014436</td>
      <td>45.013286</td>
      <td>$2,482,167 USD</td>
      <td>$70,768.23 USD</td>
      <td>https://coinmarketcap.com/currencies/presearch/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>158</th>
      <td>20200819</td>
      <td>terra-luna</td>
      <td>0.563460</td>
      <td>65.888389</td>
      <td>$206,736,062 USD</td>
      <td>$68,317,073 USD</td>
      <td>https://coinmarketcap.com/currencies/terra-luna/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>159</th>
      <td>20200819</td>
      <td>request</td>
      <td>0.039763</td>
      <td>48.005441</td>
      <td>$33,421,160 USD</td>
      <td>$677,134 USD</td>
      <td>https://coinmarketcap.com/currencies/request/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>160</th>
      <td>20200819</td>
      <td>tezos</td>
      <td>3.630000</td>
      <td>51.485968</td>
      <td>$2,739,805,042 USD</td>
      <td>$387,019,304 USD</td>
      <td>https://coinmarketcap.com/currencies/tezos/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>161</th>
      <td>20200819</td>
      <td>restart-energy-mwat</td>
      <td>0.002508</td>
      <td>49.546717</td>
      <td>$1,060,401 USD</td>
      <td>$4,856.32 USD</td>
      <td>https://coinmarketcap.com/currencies/restart-energy-mwat/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>162</th>
      <td>20200819</td>
      <td>electroneum</td>
      <td>0.005792</td>
      <td>53.466737</td>
      <td>$55,663,746 USD</td>
      <td>$390,349 USD</td>
      <td>https://coinmarketcap.com/currencies/electroneum/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>163</th>
      <td>20200819</td>
      <td>credits</td>
      <td>0.039871</td>
      <td>62.756997</td>
      <td>$8,054,577 USD</td>
      <td>$253,446 USD</td>
      <td>https://coinmarketcap.com/currencies/credits/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>164</th>
      <td>20200819</td>
      <td>lisk</td>
      <td>1.700000</td>
      <td>65.589107</td>
      <td>$197,483,307 USD</td>
      <td>$6,569,894 USD</td>
      <td>https://coinmarketcap.com/currencies/lisk/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>165</th>
      <td>20200819</td>
      <td>vidt-datalink</td>
      <td>0.956447</td>
      <td>74.117616</td>
      <td>$42,187,525 USD</td>
      <td>$7,108,463 USD</td>
      <td>https://coinmarketcap.com/currencies/vidt-datalink/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>166</th>
      <td>20200819</td>
      <td>bittorrent</td>
      <td>0.000469</td>
      <td>56.645822</td>
      <td>$472,463,702 USD</td>
      <td>$33,020,825 USD</td>
      <td>https://coinmarketcap.com/currencies/bittorrent/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>167</th>
      <td>20200819</td>
      <td>wanchain</td>
      <td>0.404629</td>
      <td>64.889985</td>
      <td>$48,012,581 USD</td>
      <td>$3,697,539 USD</td>
      <td>https://coinmarketcap.com/currencies/wanchain/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>168</th>
      <td>20200819</td>
      <td>cappasity</td>
      <td>0.002709</td>
      <td>77.271447</td>
      <td>$1,422,697 USD</td>
      <td>$105,593 USD</td>
      <td>https://coinmarketcap.com/currencies/cappasity/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>169</th>
      <td>20200819</td>
      <td>vechain</td>
      <td>0.019134</td>
      <td>51.975110</td>
      <td>$1,003,573,081 USD</td>
      <td>$217,493,702 USD</td>
      <td>https://coinmarketcap.com/currencies/vechain/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>170</th>
      <td>20200819</td>
      <td>kick-token</td>
      <td>0.000029</td>
      <td>72.466654</td>
      <td>$1,942,196 USD</td>
      <td>$568,523 USD</td>
      <td>https://coinmarketcap.com/currencies/kick-token/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>171</th>
      <td>20200819</td>
      <td>multivac</td>
      <td>0.000864</td>
      <td>46.764375</td>
      <td>$3,042,899 USD</td>
      <td>$414,771 USD</td>
      <td>https://coinmarketcap.com/currencies/multivac/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>172</th>
      <td>20200819</td>
      <td>aelf</td>
      <td>0.110200</td>
      <td>49.682471</td>
      <td>$60,773,567 USD</td>
      <td>$9,304,470 USD</td>
      <td>https://coinmarketcap.com/currencies/aelf/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>173</th>
      <td>20200819</td>
      <td>utrust</td>
      <td>0.212491</td>
      <td>80.742579</td>
      <td>$96,347,468 USD</td>
      <td>$4,161,866 USD</td>
      <td>https://coinmarketcap.com/currencies/utrust/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>174</th>
      <td>20200819</td>
      <td>lympo</td>
      <td>0.002968</td>
      <td>60.990576</td>
      <td>$2,353,792 USD</td>
      <td>$202,791 USD</td>
      <td>https://coinmarketcap.com/currencies/lympo/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>175</th>
      <td>20200819</td>
      <td>litecoin</td>
      <td>62.000000</td>
      <td>59.508214</td>
      <td>$4,126,383,386 USD</td>
      <td>$3,442,466,661 USD</td>
      <td>https://coinmarketcap.com/currencies/litecoin/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>176</th>
      <td>20200819</td>
      <td>noia-network</td>
      <td>0.110802</td>
      <td>58.723934</td>
      <td>$32,974,940 USD</td>
      <td>$632,021 USD</td>
      <td>https://coinmarketcap.com/currencies/noia-network/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>177</th>
      <td>20200819</td>
      <td>bolt</td>
      <td>0.003496</td>
      <td>56.840931</td>
      <td>$3,405,640 USD</td>
      <td>$238,551 USD</td>
      <td>https://coinmarketcap.com/currencies/bolt/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>178</th>
      <td>20200819</td>
      <td>tron</td>
      <td>0.026537</td>
      <td>64.605604</td>
      <td>$1,955,026,321 USD</td>
      <td>$1,564,532,215 USD</td>
      <td>https://coinmarketcap.com/currencies/tron/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>179</th>
      <td>20200819</td>
      <td>lukso</td>
      <td>1.220000</td>
      <td>80.322322</td>
      <td>$4,427,685 USD</td>
      <td>$4,093,928 USD</td>
      <td>https://coinmarketcap.com/currencies/lukso/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>180</th>
      <td>20200819</td>
      <td>rsk-smart-bitcoin</td>
      <td>11897.790000</td>
      <td>62.454738</td>
      <td>$3,180,797 USD</td>
      <td>$65,081.39 USD</td>
      <td>https://coinmarketcap.com/currencies/rsk-smart-bitcoin/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>181</th>
      <td>20200819</td>
      <td>energi</td>
      <td>1.750000</td>
      <td>38.357128</td>
      <td>$55,247,444 USD</td>
      <td>$1,128,628 USD</td>
      <td>https://coinmarketcap.com/currencies/energi/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>182</th>
      <td>20200819</td>
      <td>oneledger</td>
      <td>0.016000</td>
      <td>75.625915</td>
      <td>$6,014,294 USD</td>
      <td>$373,663 USD</td>
      <td>https://coinmarketcap.com/currencies/oneledger/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>183</th>
      <td>20200819</td>
      <td>crypto-com-coin</td>
      <td>0.166581</td>
      <td>58.244993</td>
      <td>$3,113,005,706 USD</td>
      <td>$70,229,885 USD</td>
      <td>https://coinmarketcap.com/currencies/crypto-com-coin/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>184</th>
      <td>20200819</td>
      <td>casino-betting-coin</td>
      <td>0.014522</td>
      <td>39.111303</td>
      <td>$2,169,612 USD</td>
      <td>$19,666.69 USD</td>
      <td>https://coinmarketcap.com/currencies/casino-betting-coin/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>185</th>
      <td>20200819</td>
      <td>nano</td>
      <td>1.180000</td>
      <td>56.865137</td>
      <td>$158,508,259 USD</td>
      <td>$15,730,510 USD</td>
      <td>https://coinmarketcap.com/currencies/nano/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>186</th>
      <td>20200819</td>
      <td>kusama</td>
      <td>12.220000</td>
      <td>51.688401</td>
      <td>$103,655,084 USD</td>
      <td>$8,219,456 USD</td>
      <td>https://coinmarketcap.com/currencies/kusama/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>187</th>
      <td>20200819</td>
      <td>ankr</td>
      <td>0.012184</td>
      <td>57.078667</td>
      <td>$72,020,033 USD</td>
      <td>$30,509,956 USD</td>
      <td>https://coinmarketcap.com/currencies/ankr/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>188</th>
      <td>20200819</td>
      <td>digitalbits</td>
      <td>0.020758</td>
      <td>52.466526</td>
      <td>$7,183,600 USD</td>
      <td>$829,999 USD</td>
      <td>https://coinmarketcap.com/currencies/digitalbits/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>189</th>
      <td>20200819</td>
      <td>quarkchain</td>
      <td>0.008852</td>
      <td>56.365987</td>
      <td>$19,011,711 USD</td>
      <td>$5,449,861 USD</td>
      <td>https://coinmarketcap.com/currencies/quarkchain/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>190</th>
      <td>20200819</td>
      <td>gamb</td>
      <td>0.000206</td>
      <td>50.712359</td>
      <td>$739,144 USD</td>
      <td>$9,616.82 USD</td>
      <td>https://coinmarketcap.com/currencies/gamb/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>191</th>
      <td>20200819</td>
      <td>opacity</td>
      <td>0.009649</td>
      <td>47.027870</td>
      <td>$1,206,005 USD</td>
      <td>$8,272.85 USD</td>
      <td>https://coinmarketcap.com/currencies/opacity/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>192</th>
      <td>20200819</td>
      <td>neblio</td>
      <td>0.668764</td>
      <td>58.842011</td>
      <td>$10,394,366 USD</td>
      <td>$209,347 USD</td>
      <td>https://coinmarketcap.com/currencies/neblio/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>193</th>
      <td>20200819</td>
      <td>carvertical</td>
      <td>0.000333</td>
      <td>64.084608</td>
      <td>$2,574,821 USD</td>
      <td>$34,733.13 USD</td>
      <td>https://coinmarketcap.com/currencies/carvertical/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>194</th>
      <td>20200819</td>
      <td>digitex-futures</td>
      <td>0.048877</td>
      <td>35.801663</td>
      <td>$43,148,116 USD</td>
      <td>$2,968,058 USD</td>
      <td>https://coinmarketcap.com/currencies/digitex-futures/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>195</th>
      <td>20200819</td>
      <td>wirex-token</td>
      <td>0.010474</td>
      <td>46.454484</td>
      <td>$28,175,276 USD</td>
      <td>$748,639 USD</td>
      <td>https://coinmarketcap.com/currencies/wirex-token/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>196</th>
      <td>20200819</td>
      <td>fortknoxster</td>
      <td>0.003092</td>
      <td>49.984046</td>
      <td>$464,341 USD</td>
      <td>$61,643.97 USD</td>
      <td>https://coinmarketcap.com/currencies/fortknoxster/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>197</th>
      <td>20200819</td>
      <td>newscrypto</td>
      <td>0.211433</td>
      <td>89.993602</td>
      <td>$18,836,307 USD</td>
      <td>$1,943,552 USD</td>
      <td>https://coinmarketcap.com/currencies/newscrypto/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>198</th>
      <td>20200819</td>
      <td>jarvis</td>
      <td>0.003118</td>
      <td>45.176360</td>
      <td>$323,411 USD</td>
      <td>$40,822.97 USD</td>
      <td>https://coinmarketcap.com/currencies/jarvis/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>199</th>
      <td>20200819</td>
      <td>elastos</td>
      <td>2.720000</td>
      <td>57.680855</td>
      <td>$44,763,965 USD</td>
      <td>$6,228,738 USD</td>
      <td>https://coinmarketcap.com/currencies/elastos/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>200</th>
      <td>20200819</td>
      <td>terra-sdt</td>
      <td>1.390000</td>
      <td>NaN</td>
      <td>No Data</td>
      <td>$266,684 USD</td>
      <td>https://coinmarketcap.com/currencies/terra-sdt/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>201</th>
      <td>20200819</td>
      <td>sylo</td>
      <td>0.003220</td>
      <td>46.916507</td>
      <td>No Data</td>
      <td>$268,814 USD</td>
      <td>https://coinmarketcap.com/currencies/sylo/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>202</th>
      <td>20200819</td>
      <td>neutrino-dollar</td>
      <td>1.010000</td>
      <td>59.810873</td>
      <td>$21,781,941 USD</td>
      <td>$1,683,622 USD</td>
      <td>https://coinmarketcap.com/currencies/neutrino-dollar/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
    <tr>
      <th>203</th>
      <td>20200819</td>
      <td>loki</td>
      <td>0.559147</td>
      <td>49.139945</td>
      <td>$27,800,224 USD</td>
      <td>$67,122.84 USD</td>
      <td>https://coinmarketcap.com/currencies/loki/historical-data/?start=20200501&amp;end=20200819</td>
    </tr>
  </tbody>
</table>
