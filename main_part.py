from imports_all import *

# Connect to websocket(it will connect to tick-by-tick data server)

price_list , qoute_list = [],[]

try:
    start = time.time()
    while True :

        breeze.ws_connect()

        # Callback to receive ticks.
        def on_ticks(ticks):

            #print("Ticks: {}".format(ticks))

            if 'depth' not in ticks.keys() :
                print('PRICE TICK : {}{}'.format(ticks['ltt'],ticks['last']) )
                price_list.append(pd.DataFrame(ticks , index = [0]))
            
            else :
                print('QOUTE TICK : {}{}'.format(ticks['time'],ticks['depth']) )
                df = pd.concat( list( map( lambda x : pd.DataFrame(x , index= [0]) , ticks['depth'])) , 
                                        axis = 1 )
                
                df['time'] = ticks['time']
                qoute_list.append( df )

        # Assign the callbacks.
        breeze.on_ticks = on_ticks

        # subscribe stocks feeds
        breeze.subscribe_feeds(  exchange_code="NFO", stock_code="NIFTY",
                                product_type="futures", expiry_date="29-Aug-2024",
                                get_exchange_quotes= True, get_market_depth= True ) 
finally :

    stop = time.time()
    print('streaming error')

    price_quote_dct = { 'price': pd.concat(price_list , axis = 0)  ,
                        'qoute': pd.concat(qoute_list , axis = 0 )  
                            }
    
    with open('price_qoute.pickle1' , 'wb') as pickle_file :
        pickle.dump( price_quote_dct , pickle_file )
    
    duration = stop - start
    print( f'SAVED CATCHABLE PRICE / QOUTE TICKS TO PICKLE ! --  DURATION : {duration}' )


n = breeze.get_historical_data_v2(  interval="30minute",
                                    from_date= "2024-08-01T07:00:00.000Z",
                                    to_date= "2024-08-06T07:00:00.000Z",
                                    stock_code="NIFTY",
                                    exchange_code="NFO",
                                    product_type="futures",
                                    expiry_date="2024-08-29T07:00:00.000Z",
                                    right="others",
                                    strike_price="0")


data_df = pd.DataFrame(n['Success'])
