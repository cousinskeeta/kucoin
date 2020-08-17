# kucoin
The coinscraper client was desinged to compare the top 400 supported assets on Kucoin's decentralized exchange. Each asset's historical and fundamental data is sourced from coinmarketcap.com.  

The client has a few requirements:  

To install the client, download the .py file:

    from coinscraper import coinscrapper

    client = coinscrapper()

The client will require google authentication, to disable, just comment out the line in the .py file.

Built in methods will preprocess the data and calculate the Relative Stregnth Index. 

    client.convert_links()
    client.get_data()
    client.pull_fundamentals()
    client.get_rsi_data()

Methods will also build graphs for each asset. 

    client.plot_rsi_data()
    client.save_candlesticks()

The .summarize() method will be a generate.csv file with all the assets summaries.

    client.summarize()

