import time
import numpy as np
import pandas as pd
import datetime
from sklearn.preprocessing import StandardScaler
import requests
import pickle 
import math
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

class predict_(object):
    asset = ""
    name = ""
    date = ""
    
    def __init__(self, asset, name, date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.asset = asset
        self.name = name
        self.date = date

    def promotion(self):
        return ('Your Ad Goes Here')
    def quote(self):
        return ("YOLO!!!")
    def forecast(self, per=7, i=0, yahoo=False, verbose=False):
        from tqdm import tqdm
        coin=self.asset
        verbose = verbose
        name=self.name
        print(f"Connecting to Coinmarketcap:\n{coin}")
        today = self.date
        per = per
        i = i
        if yahoo:
            from pandas_datareader.data import get_data_yahoo
            test = get_data_yahoo(coin).reset_index()
            dff = pd.DataFrame(test.copy())
            dff.columns = ['Date', 'High', 'Low', 'Open*', 'Close**', 'Volume', 'Adj Close']
            targets = ['High', 'Low', 'Open*', 'Close**', 'Volume', 'Adj Close']
        else:
            crypto_url = requests.get(coin)
            test = pd.read_html(crypto_url.text)
            targets = ["Open*", "High","Low","Close**","Volume", "Market Cap"]
            dff = test[2].copy()
            print("Dimensionality: ", dff.shape)
        date_range= pd.Series([i + pd.offsets.Day() for i in pd.date_range(today, freq='D', periods=per)])
        pbar = tqdm(total=len(date_range)+1)

        forecasts = []
        while i < len(date_range):
            pbar.update(1)
            self.promotion()
            self.quote()
            dff.sort_values(by='Date', inplace=True)
            new = self.predict(dff, verbose = verbose, targets=targets, asset=name, j=i) 
            new['Date'] = pd.to_datetime(date_range[i])
            print("results", new.shape, new)
            forecasts.append(new['Close**'])
            da = pd.concat([dff, new])
            da.reset_index(inplace=True)
            da.drop("index", axis=1, inplace=True)
            da.sort_values(by='Date', inplace=True)
            i+=1
            if i != len(date_range):
                dff = da.copy()
            else:
                a = forecasts[0].values
                b = forecasts[-1].values

                if b > a:
                    pch = 100 * ((b - a) / a )
                    resp=[f"{name.split('/')[4].upper()}'s price is predicted to increase over the next {len(date_range)} days !!!\n",
                    f"We forecast a {round(pch[0],7)}% increase in {name.split('/')[4].upper()} in a range of {round(a[0],7)} to {round(b[0],7)}, or ${round(b[0]-a[0],7)}",
                    f"{name}"]
                    print("""
                    Price is predicted to increase over the next {} days !!! \n
                    We forecast a {}% increase in {} from {} to {}, or ${}. URL: <a href="{}>link</a>\n
                    """.format(len(date_range), round(pch[0],2), name.split('/')[4], 
                            round(a[0],7), round(b[0],7), round(b[0]-a[0],7), name))
                else:
                    pch = 100 * ((b - a) / a )
                    resp=[f"{name.split('/')[4].upper()}'s price is predicted to decrease over the next {len(date_range)} days !!!\n",
                    f"We forecast a {round(pch[0],7)}% decrease in {name.split('/')[4].upper()} in a range of {round(a[0],7)} to {round(b[0],7)}, or $({round(b[0]-a[0],7)})",
                    f"{name}"]
                    print("""
                    Price is predicted to decrease over the next {} days !!! \n
                    We forecast a {}% decrease in {} from {} to {}, or $({}). URL: <a href="{}>link</a>\n
                    """.format(len(date_range), round(pch[0],2), name.split('/')[4], 
                            round(a[0],7), round(b[0],7), round(b[0]-a[0],7), name))


                # import matplotlib.pyplot as plt
                # import seaborn as sns
                # sns.set_style("whitegrid")
                # print(coin)
                # plt.figure(figsize=(16,9))
                # plt.plot(date_range, da['Close**'][-per:], label='Projection', color = "k")
                # plt.plot(date_range, da['High'][-per:], label='Projected High', color='r')
                # plt.plot(date_range, da['Low'][-per:], label='Projected Low', color='g')
                # kwargs = {"color":'b', 'alpha':.1, 'label':['Range: High/Low']}
                # plt.fill_between(date_range, da['High'][-per:], da['Low'][-per:], **kwargs)
                # plt.title(f"Close Price - {per} Day Projection")
                # plt.xticks(date_range, date_range)
                # plt.ylabel('Price')
                # plt.xlabel('Date')
                # plt.legend()
                # # plt.show();
                # dest = '{name}.jpeg'
                # plt.savefig(dest, dpi=72)
                # display(da.tail(per))
                pbar.close()
                return [da, pch, resp] #dest

    def predict(self, data=pd.DataFrame(), targets=[], verbose = False, predictions = {}, asset= name, j = 0):
        predictions = {}
        data = data
        targets=targets
        verbose = verbose
        asset = self.name
        j = j
        for i in targets:
            # Copy orignial dataset for each iteration
            df = pd.DataFrame(data)

            if i == "Open*":
                # Preprocessing data to add features and polynomial
                new_df, new_columns, new_index = self.preprocess(df, verbose, drop = i)    
                if verbose:
                    print([i for i in new_columns], print(type(new_index)))

                # Creating training and validation sets from new dataset and orignial
                train_X = pd.DataFrame(new_df).ffill() if pd.isnull(new_df).any() else new_df
                train_y = data[i]
                    
                # Adding Prediction to list
                metrics, res = self.ensemble(train_X,train_y, verbose, data, drop = i, asset=asset)
                predictions[i] = []
                predictions[i].append(res)
                
                if verbose:
                    # display(metrics)
                    print(f"Average {i}:", predictions[i])
                    print(predictions, type(metrics))

            elif i == "High":
                # Preprocessing data to add features and polynomials
                new_df, new_columns, new_index = self.preprocess(df, verbose, drop = i)    
                if verbose:
                    print([i for i in new_columns])

                # Creating training and validation sets from new dataset and orignial
                train_X = pd.DataFrame(new_df).ffill() if pd.isnull(new_df).any() else new_df
                train_y = data[i]
                    
                # Adding Prediction to list
                metrics, res = self.ensemble(train_X,train_y, verbose, data, drop = i, asset=asset, j=j)
                predictions[i] = []
                predictions[i].append(res)
                
                if verbose:
                    # display(metrics)
                    print(f"Average {i}:", predictions[i])
                    print(predictions)
        

            elif i == "Low":
                # Preprocessing data to add features and polynomials
                new_df, new_columns, new_index = self.preprocess(df, verbose, drop = i)    
                if verbose:
                    print([i for i in new_columns])

                # Creating training and validation sets from new dataset and orignial
                train_X = pd.DataFrame(new_df).ffill() if pd.isnull(new_df).any() else new_df
                train_y = data[i]
                    
                # Adding Prediction to list
                metrics, res = self.ensemble(train_X,train_y, verbose, data, drop = i, asset=asset)
                predictions[i] = []
                predictions[i].append(res)      
                
                if verbose:
                    # display(metrics)     
                    print(f"Average {i}:", predictions[i])
                    print(predictions)

            elif i == "Close**":
                # Preprocessing data to add features and polynomials
                new_df, new_columns, new_index = self.preprocess(df, verbose, drop = i)    
                if verbose:
                    print([i for i in new_columns])

                # Creating training and validation sets from new dataset and orignial
                train_X = pd.DataFrame(new_df).ffill() if pd.isnull(new_df).any() else new_df
                train_y = data[i]
                    
                # Adding Prediction to list
                metrics, res = self.ensemble(train_X,train_y, verbose, data, drop = i, asset=asset)
                predictions[i] = []
                predictions[i].append(res)
                
                if verbose:
                    # display(metrics)
                    print(f"Average {i}:", predictions[i])
                    print(predictions)

            elif i == "Volume":
                # Preprocessing data to add features and polynomials
                new_df, new_columns, new_index = self.preprocess(df, verbose, drop = i)    
                if verbose:
                    print([i for i in new_columns])

                # Creating training and validation sets from new dataset and orignial
                train_X = pd.DataFrame(new_df).ffill() if pd.isnull(new_df).any()  else new_df
                train_y = data[i]
                    
                # Adding Prediction to list
                metrics, res = self.ensemble(train_X,train_y, verbose, data, drop = i, asset=asset)
                predictions[i] = []
                predictions[i].append(res)
                
                if verbose:
                    # display(metrics)
                    print(f"Average {i}:", predictions[i])
                    print(predictions)
                

            elif i == "Market Cap" or i == 'Adj Close':
                # Preprocessing data to add features and polynomials
                new_df, new_columns, new_index = self.preprocess(df, verbose, drop = i)    
                if verbose:
                    print([i for i in new_columns])

                # Creating training and validation sets from new dataset and orignial
                train_X = pd.DataFrame(new_df).ffill() if pd.isnull(new_df).any() else new_df
                train_y = data[i]
                    
                # Adding Prediction to list
                metrics, res = self.ensemble(train_X,train_y, verbose, data, drop = i, asset=asset)
                predictions[i] = []
                predictions[i].append(res)
                
                if verbose:
                    # display(metrics)
                    print(f"Average {i}:", predictions[i])
                    print(predictions)

        _____ = pd.DataFrame.from_dict(predictions) 
        return _____

    def preprocess(self, df=pd.DataFrame(), verbose=True, drop=""):
        verbose= verbose
        df= df
        data= df.copy()
        drop = drop
        """                                                              _           
            ___   ____ ___  ___   ____ ___  ____ ___  ___  ___  (_)___  ___ _
            / _ \ / __// -_)/ _ \ / __// _ \/ __// -_)(_-< (_-< / // _ \/ _ `/
        / .__//_/   \__// .__//_/   \___/\__/ \__//___//___//_//_//_/\_, / 
        /_/             /_/                                          /___/  
        """
        # creating datatime index
        df['Date'] = pd.to_datetime(df['Date'])  # change to sort by date, convert date to datetime format
        df.index = pd.DatetimeIndex(df['Date'])
        df.sort_index(ascending=True, inplace=True)  
        final = df.copy()
        print("new index:",final.head(), final.tail())
        ## indicator features

        # EMA - ema(data, period=0, column='Close**')
        bitcoin_ema = data.copy()
        for n in [9,21,50,200]:
            data_ = self.ema(bitcoin_ema, period=n, column=drop)
            for i in data_.columns[6:]:
                final[f'{i}']= data_[i].bfill().values

        # MACD -  macd(data, period_long=26, period_short=12, period_signal=9, column='Close**')
        bitcoin_macd = bitcoin_ema
        data_ = self.macd(bitcoin_macd, period_long=26, period_short=12, period_signal=9, column=drop)
        for i in data_.columns[6:]:
            final[f'{i}']= data_[i].bfill().values
        
        ## ACC Dist
        bitcoin_acd = bitcoin_macd
        data_ = self.acc_dist(bitcoin_acd)
        for i in data_.columns[11:]:
            final[f'{i}']= data_[i].bfill().values

        # ## Bollinger Bands
        # bitcoin_bb = bitcoin_acd
        # data_ = self.bollinger_bands(bitcoin_bb)
        # for i in data_.columns[13:]:
        #     final[f'{i}']= data_[i].bfill().values

        # ### On-balance volume
        # bitcoin_obv = bitcoin_ema
        # data_ = self.on_balance_volume(bitcoin_obv)
        # for i in data_.columns[16:]:
        #     final[f'{i}']= data_[i].bfill().values

        # ## Price Volume Trend
        # bitcoin_pvt = bitcoin_obv
        # data_ = self.price_volume_trend(bitcoin_pvt)
        # for i in data_.columns[18:]:
        #     final[f'{i}']= data_[i].bfill().values

        e = final.copy()

        ## checking and removing Null values
        e.fillna(0,axis=1, inplace=True)

        ## month and day features
        e['Month'] = e.index.month
        e['Day'] = e.index.dayofyear
        e['Year'] = e.index.year - e.index.year.min()
        date_features = ['Day','Month','Year']

        ## month and day polynomials
        polynomial_terms = [.5, 1.5, 2]
        for feature in date_features:
            for i in polynomial_terms:
                e[feature+'**'+str(i)] = e[feature]**i

        ## previous values and polynomials
        previous_values_range = 36
        for i in range(1,previous_values_range):
            e['Previous'+str(i)] = e[drop].shift(i).bfill()
            for j in polynomial_terms:
                e['Previous'+str(i)+'**'+str(j)] = (e[drop].shift(i).bfill())**j
        
        e.drop([drop, 'Date'], axis=1, inplace=True)
        
        ## Scaling features before modeling
        from sklearn.preprocessing import StandardScaler
        scalar = StandardScaler()
        scalar.fit(e.to_numpy(copy=True, na_value=0))
        X = scalar.transform(e)
        return X, e.columns, e.index

    def ensemble(self, X,y, verbose=True, data=pd.DataFrame(), drop="", asset="", j =0):

        # drive.mount('/content/drive', force_remount=True)
        j=j
        train_X = X
        print("Train_X dtype: ", type(train_X))
        print(train_X)

        train_y = y
        print("Train_X dtype: ", type(train_y))
        print(train_y)

        verbose = verbose
        data = data
        drop= drop
        asset= asset

        model_name = []
        model_mse = []
        model_rmse = []
        model_preds = []
        model_times = []
        metrics = pd.DataFrame()
        
        # Lasso Regression
        starting = time.time()
        model_name.append("Lasso")
        save_name = f"{drop[:2]}-Lasso-Model"
        print(save_name+".p")
        from pathlib import Path
        p = Path(f"{save_name}.p")
        
        if p.exists() and j == 0:
            print(f'Loading{save_name}...')
            lasso = pickle.load( open(f"{save_name}.p", "rb" ) )
            
            print(type(train_X),train_X)
            train_X = pd.DataFrame(train_X)
            print("\n--------->",type(train_X),train_X.head())

            if train_X.isnull().sum().sum() > 0:
                train_X.fillna(0, axis=1, inplace=True)
            lasso.fit(train_X, train_y)

            print('prediction:',train_X[-1:0])

            y_pred = lasso.predict(train_X[-1:]) #.reshape(1,-1))  # Making prediction based on last day info
            model_preds.append(y_pred[-1])
            
            filename = f'{save_name}.p'
            pickle.dump(lasso, open(filename, 'wb'))
            
            from sklearn.metrics import mean_squared_error # Metrics for the model
            y_true = data[drop].values[-1:]

            mse = mean_squared_error(np.array(y_true), np.array(y_pred))
            model_mse.append(mse)
            
            rmse = mean_squared_error(np.array(y_true), np.array(y_pred), squared=False)
            model_rmse.append(rmse)

            elapsed = round(time.time() - starting,2)     # Time to run model
            model_times.append(elapsed)
        elif p.exists() and j>0:
            print(f'Loading{save_name}...')
            ridge = pickle.load( open(f"{save_name}.p", "rb" ) )
            
            print(type(train_X),train_X)
            train_X = pd.DataFrame(train_X)
            print("\n--------->",type(train_X),train_X.head())
            
            if train_X.isnull().sum().sum() > 0:
                train_X.fillna(0, axis=1, inplace=True)
            ridge.fit(train_X, train_y)

            y_pred = ridge.predict(train_X[-1:])  # Making prediction based on last day info
            model_preds.append(y_pred[-1])

            from sklearn.metrics import mean_squared_error # Metrics for the model
            y_true = data[drop].values[-1:]

            mse = mean_squared_error(np.array(y_true), np.array(y_pred))
            model_mse.append(mse)
            
            rmse = mean_squared_error(np.array(y_true), np.array(y_pred), squared=False)
            model_rmse.append(rmse)

            elapsed = round(time.time() - starting,2)     # Time to run model
            model_times.append(elapsed) 
        else:
            print(f'Could not find {save_name}...\nCreating new model for future usage...')
            print("Loaded: Scikit-Learn")
            model_names = []
            scores = []
            r2s = []
            mses = []
            rmses = []
            times = []

            n_train = 500
            n_records = len(train_X)
            print(len(train_X))
            from sklearn.linear_model import LassoLars
            lasso = LassoLars()  

            for i in range(n_train, n_records):
                start = time.time()
                name = '{}: #{}'.format(save_name,i-499)
                print(name, f"out of {len(range(n_train, n_records))}")

                X_train, X_test = train_X[0:i], train_X[i:i+1]
                y_train, y_test = train_y[0:i], train_y[i:i+1]

                print('Xtrain=%d, Xtest=%d' % (len(X_train), len(X_test)))
                print('ytrain=%d, ytest=%d' % (len(y_train), len(y_test)))
                
                if X_train.isnull().sum().sum() > 0:
                    X_train.fillna(0, axis=1, inplace=True)
                lasso.fit(X_train, y_train)

                y_pred = lasso.predict(X_test)
                
                score = lasso.score(X_test, y_test)
                r2 = r2_score(y_test, y_pred)

                mse = mean_squared_error(y_test, y_pred)
                mses.append(mse)
                
                rmse = math.sqrt(mse)
                rmses.append(rmse)

                elapsed = time.time() - start
                
                print('Time: ', elapsed, 'seconds.')
                print('#'*20)

                r2s.append(r2)
                model_names.append(name)
                scores.append(score)
                times.append(elapsed)

            metrics_ = pd.DataFrame()
            metrics_['Name'] = model_names
            metrics_["Score"] = scores
            metrics_['R^2'] = r2s
            metrics_['MSE'] = mses
            metrics_['RMSE'] = rmses
            metrics_['Time'] = model_times
            print(metrics.head(3), metrics.tail(3))

            # display(metrics_.head())
            print(type(train_X),train_X)
            train_X = pd.DataFrame(train_X)
            print("\n--------->",type(train_X),train_X.head())
            if train_X.isnull().sum().sum() > 0:
                train_X.fillna(0, axis=1, inplace=True)
            lasso.fit(train_X,train_y)
            y_pred = lasso.predict(train_X[-1:])  # Making prediction based on last day info
            model_preds.append(y_pred[-1])
            
            # saving data
            filename = f'{save_name}.p'
            pickle.dump(lasso, open(filename, 'wb'))
            metrics_.to_pickle(f'{save_name}-metrics.p')
            
            from sklearn.metrics import mean_squared_error # Metrics for the model
            y_true = data[drop].values[-1:]

            mse = mean_squared_error(np.array(y_true), np.array(y_pred))
            model_mse.append(mse)
            
            rmse = mean_squared_error(np.array(y_true), np.array(y_pred), squared=False)
            model_rmse.append(rmse)

            elapsed = round(time.time() - starting,2)     # Time to run model
            model_times.append(elapsed)

        # Linear Regression
        from sklearn.linear_model import LinearRegression 
        starting = time.time()
        model_name.append("Linear")
        save_name = f"{drop[:2]}-Linear-Model"
        print(save_name)
        from pathlib import Path
        p = Path(f"{save_name}.p")
        
        if p.exists() and j == 0:
            print(f'Loading{save_name}...')
            linear = pickle.load( open(f"{save_name}.p", "rb" ) )

            print(type(train_X),train_X)
            train_X = pd.DataFrame(train_X)
            print("\n--------->",type(train_X),train_X.head())

            if train_X.isnull().sum().sum() > 0:
                train_X.fillna(0, axis=1, inplace=True)
            linear.fit(train_X, train_y)

            y_pred = linear.predict(train_X[-1:])  # Making prediction based on last day info
            model_preds.append(y_pred[-1])
            
            filename = f'{save_name}.p'
            pickle.dump(linear, open(filename, 'wb'))
            
            from sklearn.metrics import mean_squared_error # Metrics for the model
            y_true = data[drop].values[-1:]

            mse = mean_squared_error(np.array(y_true), np.array(y_pred))
            model_mse.append(mse)
            
            rmse = mean_squared_error(np.array(y_true), np.array(y_pred), squared=False)
            model_rmse.append(rmse)

            elapsed = round(time.time() - starting,2)     # Time to run model
            model_times.append(elapsed)  
        elif p.exists() and j > 0:
            print(f'Loading{save_name}...')
            ridge = pickle.load( open(f"{save_name}.p", "rb" ) )

            print(type(train_X),train_X)
            train_X = pd.DataFrame(train_X)
            print("\n--------->",type(train_X),train_X.head())

            if train_X.isnull().sum().sum() > 0:
                train_X.fillna(0, axis=1, inplace=True)
            ridge.fit(train_X, train_y)

            y_pred = ridge.predict(train_X[-1:])  # Making prediction based on last day info
            model_preds.append(y_pred[-1])

            from sklearn.metrics import mean_squared_error # Metrics for the model
            y_true = data[drop].values[-1:]

            mse = mean_squared_error(np.array(y_true), np.array(y_pred))
            model_mse.append(mse)
            
            rmse = mean_squared_error(np.array(y_true), np.array(y_pred), squared=False)
            model_rmse.append(rmse)

            elapsed = round(time.time() - starting,2)     # Time to run model
            model_times.append(elapsed) 
        else:
            print(f'Could not find {save_name}...\nCreating new model for future usage...')
            model_names = []
            scores = []
            r2s = []
            mses = []
            rmses = []
            times = []

            n_train = 500
            n_records = len(X)
            linear = LinearRegression()  

            for i in range(n_train, n_records):
                start = time.time()
                name = '{}: #{}'.format(save_name,i-499)
                print(name, f"out of {len(range(n_train, n_records))}")

                X_train, X_test = train_X[0:i], train_X[i:i+1]
                y_train, y_test = train_y[0:i], train_y[i:i+1]

                print('Xtrain=%d, Xtest=%d' % (len(X_train), len(X_test)))
                print('ytrain=%d, ytest=%d' % (len(y_train), len(y_test)))
                
                if X_train.isnull().sum().sum() > 0:
                    X_train.fillna(0, axis=1, inplace=True)
                linear.fit(X_train, y_train)

                y_pred = linear.predict(X_test)
                
                score = linear.score(X_test, y_test)
                r2 = r2_score(y_test, y_pred)

                mse = mean_squared_error(y_test, y_pred)
                mses.append(mse)
                
                rmse = math.sqrt(mse)
                rmses.append(rmse)

                print('Score: ', score)
                print("R2: ", r2)  
                print('MSE: ', mse)
                print('RMSE: ', rmse)

                elapsed = time.time() - start
                
                print('Time: ', elapsed, 'seconds.')
                print('#'*20)

                r2s.append(r2)
                model_names.append(name)
                scores.append(score)
                times.append(elapsed)

            metrics_ = pd.DataFrame()
            metrics_['Name'] = model_names
            metrics_["Score"] = scores
            metrics_['R^2'] = r2s
            metrics_['MSE'] = mses
            metrics_['RMSE'] = rmses
            metrics_['Time'] = model_times

            # display(metrics_.head())
            print(type(train_X),train_X)
            train_X = pd.DataFrame(train_X)
            print("\n--------->",type(train_X),train_X.head())
            if train_X.isnull().sum().sum() > 0:
                train_X.fillna(0, axis=1, inplace=True)
            linear.fit(train_X,train_y)
            y_pred = linear.predict(train_X[-1:])
            model_preds.append(y_pred[-1])


            # saving data
            filename = f'{save_name}.p'
            pickle.dump(linear, open(filename, 'wb'))
            metrics_.to_pickle(f'{save_name}-metrics.p')

            from sklearn.metrics import mean_squared_error # Metrics for the model
            y_true = data[drop].values[-1:]

            mse = mean_squared_error(np.array(y_true), np.array(y_pred))
            model_mse.append(mse)
            
            rmse = mean_squared_error(np.array(y_true), np.array(y_pred), squared=False)
            model_rmse.append(rmse)

            elapsed = round(time.time() - starting,2)     # Time to run model
            model_times.append(elapsed)

        # Ridge Regression
        from sklearn.linear_model import Ridge
        starting = time.time()
        model_name.append("Ridge")
        save_name = f"{drop[:2]}-Ridge-Model"
        print(save_name)
        from pathlib import Path
        p = Path(f"{save_name}.p")
        
        if p.exists() and j==0: 
            print(f'Loading{save_name}...')
            ridge = pickle.load( open(f"{save_name}.p", "rb" ) )
            print(type(train_X),train_X)
            train_X = pd.DataFrame(train_X)
            print("\n--------->",type(train_X),train_X.head())

            if train_X.isnull().sum().sum() > 0:
                train_X.fillna(0, axis=1, inplace=True)
            ridge.fit(train_X, train_y)

            y_pred = ridge.predict(train_X[-1:])  # Making prediction based on last day info
            model_preds.append(y_pred[-1])
            
            filename = f'{save_name}.p'
            pickle.dump(ridge, open(filename, 'wb'))
            
            from sklearn.metrics import mean_squared_error # Metrics for the model
            y_true = data[drop].values[-1:]

            mse = mean_squared_error(np.array(y_true), np.array(y_pred))
            model_mse.append(mse)
            
            rmse = mean_squared_error(np.array(y_true), np.array(y_pred), squared=False)
            model_rmse.append(rmse)

            elapsed = round(time.time() - starting,2)     # Time to run model
            model_times.append(elapsed)  
        elif p.exists() and j>0:
            print(f'Loading{save_name}...')
            ridge = pickle.load( open(f"{save_name}.p", "rb" ) )

            print(type(train_X),train_X)
            train_X = pd.DataFrame(train_X)
            print("\n--------->",type(train_X),train_X.head())

            if train_X.isnull().sum().sum() > 0:
                train_X.fillna(0, axis=1, inplace=True)
            ridge.fit(train_X, train_y)

            y_pred = ridge.predict(train_X[-1:])  # Making prediction based on last day info
            model_preds.append(y_pred[-1])
            
            from sklearn.metrics import mean_squared_error # Metrics for the model
            y_true = data[drop].values[-1:]

            mse = mean_squared_error(np.array(y_true), np.array(y_pred))
            model_mse.append(mse)
            
            rmse = mean_squared_error(np.array(y_true), np.array(y_pred), squared=False)
            model_rmse.append(rmse)

            elapsed = round(time.time() - starting,2)     # Time to run model
            model_times.append(elapsed)     
        else:
            print(f'Could not find {save_name}...\nCreating new model for future usage...')
            import math
            model_names = []
            scores = []
            r2s = []
            mses = []
            rmses = []
            times = []

            n_train = 500
            n_records = len(X)
            ridge = Ridge(alpha=.1) 

            for i in range(n_train, n_records):
                start = time.time()
                name = '{}: #{}'.format(save_name,i-499)
                print(name, f"out of {len(range(n_train, n_records))}")

                X_train, X_test = train_X[0:i], train_X[i:i+1]
                y_train, y_test = train_y[0:i], train_y[i:i+1]

                print('Xtrain=%d, Xtest=%d' % (len(X_train), len(X_test)))
                print('ytrain=%d, ytest=%d' % (len(y_train), len(y_test)))
                if X_train.isnull().sum().sum() > 0:
                    X_train.fillna(0, axis=1, inplace=True)
                ridge.fit(X_train, y_train)

                y_pred = ridge.predict(X_test)
                
                score = ridge.score(X_test, y_test)
                r2 = r2_score(y_test, y_pred)

                mse = mean_squared_error(y_test, y_pred)
                mses.append(mse)
                
                rmse = math.sqrt(mse)
                rmses.append(rmse)

                elapsed = time.time() - start
                
                print('Time: ', elapsed, 'seconds.')
                print('#'*20)

                r2s.append(r2)
                model_names.append(name)
                scores.append(score)
                times.append(elapsed)

            metrics_ = pd.DataFrame()
            metrics_['Name'] = model_names
            metrics_["Score"] = scores
            metrics_['R^2'] = r2s
            metrics_['MSE'] = mses
            metrics_['RMSE'] = rmses
            metrics_['Time'] = model_times

            # display(metrics_.head())
            print(type(train_X),train_X)
            train_X = pd.DataFrame(train_X)
            print("\n--------->",type(train_X),train_X.head())            
            if train_X.isnull().sum().sum() > 0:
                train_X.fillna(0, axis=1, inplace=True)
            ridge.fit(train_X,train_y)
            y_pred = ridge.predict(train_X[-1:])
            model_preds.append(y_pred[-1])

            # saving data
            filename = f'{save_name}.p'
            pickle.dump(ridge, open(filename, 'wb'))
            metrics_.to_pickle(f'{save_name}-metrics.p')
            from sklearn.metrics import mean_squared_error # Metrics for the model
            y_true = data[drop].values[-1:]

            mse = mean_squared_error(np.array(y_true), np.array(y_pred))
            model_mse.append(mse)
            
            rmse = mean_squared_error(np.array(y_true), np.array(y_pred), squared=False)
            model_rmse.append(rmse)

            elapsed = round(time.time() - starting,2)     # Time to run model
            model_times.append(elapsed)

        metrics['Model'] = model_name
        metrics['Prediction'] = model_preds
        metrics['MSE'] = model_mse
        metrics['RMSE'] = model_rmse
        metrics['Time'] = model_times
        return metrics, metrics.Prediction.mean()

    def ema(self, data, period=0, column='Close**'):
        """
        Exponential moving average
        Params: 
            data: pandas DataFrame
            period: smoothing period
            column: the name of the column with values for calculating EMA in the 'data' DataFrame
            
        Returns:
            copy of 'data' DataFrame with 'ema[period]' column added
        """
        data['ema' + str(period)] = data[column].ewm(ignore_na=False, min_periods=period, com=period, adjust=True).mean()

        return data

    def macd(self, data, period_long=26, period_short=12, period_signal=9, column='Close**'):
        """
        Moving Average Convergence/Divergence Oscillator (MACD)
        Source: http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_convergence_divergence_macd
        Params: 
            data: pandas DataFrame
            period_long: the longer period EMA (26 days recommended)
            period_short: the shorter period EMA (12 days recommended)
            period_signal: signal line EMA (9 days recommended)
            column: the name of the column with values for calculating MACD in the 'data' DataFrame
            
        Returns:
            copy of 'data' DataFrame with 'macd_val' and 'macd_signal_line' columns added
        """
        remove_cols = []
        if not 'ema' + str(period_long) in data.columns:
            data = self.ema(data, period_long)
            remove_cols.append('ema' + str(period_long))

        if not 'ema' + str(period_short) in data.columns:
            data = self.ema(data, period_short)
            remove_cols.append('ema' + str(period_short))

        data['macd_val'] = data['ema' + str(period_short)] - data['ema' + str(period_long)]
        data['macd_signal_line'] = data['macd_val'].ewm(ignore_na=False, min_periods=0, com=period_signal, adjust=True).mean()

        data = data.drop(remove_cols, axis=1)
            
        return data

    def acc_dist(self, data, trend_periods=21, open_col='Open*', high_col='High', low_col='Low', close_col='Close**', vol_col='Volume'):
        """
        Accumulation Distribution 
        Source: http://stockcharts.com/school/doku.php?st=accumulation+distribution&id=chart_school:technical_indicators:accumulation_distribution_line
        Params: 
            data: pandas DataFrame
            trend_periods: the over which to calculate AD
            open_col: the name of the OPEN values column
            high_col: the name of the HIGH values column
            low_col: the name of the LOW values column
            close_col: the name of the CLOSE values column
            vol_col: the name of the VOL values column
            
        Returns:
            copy of 'data' DataFrame with 'acc_dist' and 'acc_dist_ema[trend_periods]' columns added
        """
        _ = []
        for index, row in data.iterrows():
            if row[high_col] != row[low_col]:
                ac = ((row[close_col] - row[low_col]) - (row[high_col] - row[close_col])) / (row[high_col] - row[low_col]) * row[vol_col]
            else:
                ac = 0
                print(index)
            _.append(ac)
        data['acc_dist'] = _
        data['acc_dist_ema' + str(trend_periods)] = data['acc_dist'].ewm(ignore_na=False, min_periods=0, com=trend_periods, adjust=True).mean()
        
        return data

    def bollinger_bands(self, data, trend_periods=20, close_col='Close**'):
        """
        Bollinger Bands
        Source: https://en.wikipedia.org/wiki/Bollinger_Bands
        Params: 
            data: pandas DataFrame
            trend_periods: the over which to calculate BB
            close_col: the name of the CLOSE values column
            
        Returns:
            copy of 'data' DataFrame with 'bol_bands_middle', 'bol_bands_upper' and 'bol_bands_lower' columns added
        """
        data['bol_bands_middle'] = data[close_col].ewm(ignore_na=False, min_periods=0, com=trend_periods, adjust=True).mean()
        up = []
        low = []
        for index, row in data.iterrows():

            s = data[close_col].iloc[index - trend_periods: index]
            sums = 0
            middle_band = data.at[index, 'bol_bands_middle']
            for e in s:
                sums += np.square(e - middle_band)

            std = np.sqrt(sums / trend_periods)
            d = 2
            upper_band = middle_band + (d * std)
            lower_band = middle_band - (d * std)

            up.append(upper_band)
            low.append(lower_band)

        data['bol_bands_upper'] = up
        data['bol_bands_lower'] = low

        return data

    

    def on_balance_volume(self, data, trend_periods=21, close_col='Close**', vol_col='Volume'):
        """
        On Balance Volume (OBV)
        Source: http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:on_balance_volume_obv
        Params: 
            data: pandas DataFrame
            trend_periods: the over which to calculate OBV
            close_col: the name of the CLOSE values column
            vol_col: the name of the VOL values column
            
        Returns:
            copy of 'data' DataFrame with 'obv' and 'obv_ema[trend_periods]' columns added
        """
        data['obv'] = [0.]*len(data)
        for index, row in data.iterrows():
            if index > 0:
                last_obv = data.at[index - 1, 'obv']
                if row[close_col] > data.at[index - 1, close_col]:
                    current_obv = last_obv + row[vol_col]
                elif row[close_col] < data.at[index - 1, close_col]:
                    current_obv = last_obv - row[vol_col]
                else:
                    current_obv = last_obv
            else:
                last_obv = 0
                current_obv = row[vol_col]

            data.iat[index, 17] = current_obv

        data['obv_ema' + str(trend_periods)] = data['obv'].ewm(ignore_na=False, min_periods=0, com=trend_periods, adjust=True).mean()
        
        return data

    def price_volume_trend(self, data, trend_periods=21, close_col='Close**', vol_col='Volume'):
        """
        Price-volume trend (PVT) (sometimes volume-price trend)
        Source: https://en.wikipedia.org/wiki/Volume%E2%80%93price_trend
        Params: 
            data: pandas DataFrame
            trend_periods: the over which to calculate PVT
            close_col: the name of the CLOSE values column
            vol_col: the name of the VOL values column
            
        Returns:
            copy of 'data' DataFrame with 'pvt' and 'pvt_ema[trend_periods]' columns added
        """
        data['pvt'] = [0.]*len(data)
        for index, row in data.iterrows():
            if index > 0:
                last_val = data.at[index - 1, 'pvt']
                last_close = data.at[index - 1, close_col]
                today_close = row[close_col]
                today_vol = row[vol_col]
                current_val = last_val + (today_vol * (today_close - last_close) / last_close)
            else:
                current_val = row[vol_col]

            data.iat[index, 21] = current_val

        data['pvt_ema' + str(trend_periods)] = data['pvt'].ewm(ignore_na=False, min_periods=0, com=trend_periods, adjust=True).mean()
            
        return data

