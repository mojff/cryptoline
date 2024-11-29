from binance.client import Client    #To comunicate with Binance API (to install this package run this command on the cmd :pip install python-binance)
import pandas as pd 
import API
import requests	                                      #To comunicate with CoinMarketCap API
import dash
from dash import dcc                                  # To access to  interactive components, including dropdowns, checklists, and sliders.
from dash import html                                 # To design the layout
import plotly.graph_objects as go                     # To visualize the charts 
from plotly.subplots import make_subplots             # To make subplots 
from dash.dependencies import Input, Output           # To Update the chart

# defining variables
Pkey =API.Pkey
Skey =API.Skey
client = Client(api_key=Pkey, api_secret=Skey)
interval=Client.KLINE_INTERVAL_1HOUR

# colors dictionary :
project_colors={
'snow':'rgb(255, 250, 240)',#This  color kind dark blue of   that we have determined  it based on the compound values red,green and blue and basiclly we used it to the font color 
'turquoise':'rgb(72,209,204)',#The name of the color is ((MediumTurquoise))
'pink':'rgb(255, 72, 112)',#This 	color  kind of bink that we have determined  it based on the compound values red,green and blue 
'purple':'rgb(142, 60, 168)', #purple color for 
'Blue':'rgb(32, 128, 225)', #This 	color  kind blue of   that we have determined  it based on the compound values red,green and blue 
'darkBlue':'rgb(13, 5, 15)',#This 	color  its kind dark blue of   that we have determined  it based on the compound values red,green and blue and basiclly we used it to the our backgroud dashbourd color 
'darkestBlue':'rgb(18, 5, 17)'#This  color kind dark blue of   that we have determined  it based on the compound values red,green and blue and basiclly we used it to the our backgroud dashbourd color 
}

# creat the dashboard components and their styles :
tab_style_selected={'background-color':project_colors['darkBlue'],'border-color':project_colors['darkBlue'],'color':'rgb(72,209,204)',
					'border':'0','border-width':'0','border-hight':'0','padding':'0px 0px 0px 0px'}
Liundecorated_style={'list-style-type':' '}
P_tag_style_interval_text={'color':project_colors['turquoise'],}
Ulinline_style={'list-style-type':'none','display':'flex','flex-direction':'row','justify-content':'flex-start', 'white-space': 'nowrap'}
inputtext_style={'background-color':project_colors['darkBlue'],'border-color':project_colors['turquoise'],'color':project_colors['snow'],
				'padding':'0px 0px 0px 0px','margin':'60px 0px 0px 0px ','width':'170px','display': 'inline-block',
				'border-top-style':'none','border-right-style':'none','border-bottom-styl':'solid','border-left-style':'none','border-radius':'2px'}
inputnumeric_style={'background-color':project_colors['darkBlue'],'border-color':project_colors['turquoise'],'color':project_colors['snow'],
					'padding':'0px 0px 0px 0px','margin':'30px 0px 0px 0px ','width':'40px','display': 'inline-block', 'border-radius':'10px',}
inputtextcoin=dcc.Input(id='input_currency',type='text',placeholder='Enter The Symbol Like: BTC',style=inputtext_style,debounce=True,value='')


# labels and values for the dropdown tabs:
interval_frame_options = [

    {'label': '1m', 'value': '1m'},
    {'label': '3m', 'value': '3m'},
    {'label': '5m', 'value': '5m'},
    {'label': '15m', 'value': '15m'},
    {'label': '30m', 'value': '30m'},
	{'label': '1h', 'value': '1h'},
	{'label': '2h', 'value': '2h'},
	{'label': '4h', 'value': '4h'},
	{'label': '6h', 'value': '6h'},
	{'label': '8h', 'value': '8h'},
	{'label': '12h', 'value': '12h'},
	{'label': '1D', 'value': '1d'},
	{'label': '3D', 'value': '3d'},
	{'label': '1W', 'value': '1w'},
	{'label': '1Mon', 'value': '1M'},

]

depth_frame_options = [
    {'label': '1H', 'value': '1 hour ago'},
    {'label': '1D', 'value': '1 day ago'},
    {'label': '1W', 'value': '1 week ago'},
    {'label': '1Mon', 'value': '1 month ago'},
    
]

# craeting the Dropdown tabs with their styles :
Dropdown_style={'background-color':project_colors['darkBlue'],'border-color':project_colors['darkBlue'],'color':project_colors['darkBlue'],
				'border':'0px','border-width':'0','border-hight':'0','padding':'0px 0px 0px 0px','margin':'27px 0px 0px -27px ','width':'65px',}
Dropdown_intrval=dcc.Dropdown( options=interval_frame_options,id='interval_drpdown',placeholder='all',style=Dropdown_style,)
Dropdown_depth=dcc.Dropdown(  options=depth_frame_options,id='depth_dropdown',placeholder='all',style=Dropdown_style,)

#creat a dectionary styles key:name of the class   value:the value of the 'style' attribut of the html tag 
style={
	'appDiv':{'position':'fixed','top':'0px','bottom':'0px','right':'0px','left':'0px','background-color':project_colors['darkBlue'],'height':'100%','width':'100%','border-color':project_colors['darkBlue'],'color':'rgb(72,209,204)','border':'0','border-width':'0','border-hight':'0','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px'},
	'header':{'width':'100%','height':'11%','margin':'0px 0px 0px 0px','padding':'0px','border':'0px','background-color':project_colors['darkBlue'],'background-color':project_colors['darkBlue'],'display': 'flex','flexWrap':'wrap','border-color':project_colors['darkBlue'],'color':'rgb(72,209,204)','border':'0','border-width':'0','border-hight':'0','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px'},
	'headerMainDiv':{'width':'100%','height':'100%','margin':'0px 0px 0px 0px','padding':'0px','border':'0px','background-color':project_colors['darkBlue'],'border-top-style':'none','border-right-style':'none','border-bottom-styl':'solid','border-left-style':'none','border-radius':'2px','border-color':project_colors['darkBlue'],'color':'rgb(72,209,204)','border':'0','border-width':'0','border-hight':'0','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px'},
	'headerMainUl':{'width':'100%','height':'100%','margin':'0px 0px 0px 0px','padding':'0px','border':'0px','background-color':project_colors['darkBlue'],'list-style-type':'none','display':'flex','flex-direction':'row','justify-content':'flex-start', 'white-space': 'nowrap'},
	'headerMainUlchild':{'list-style-type':' ','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px',},
	'left header Ul':{'list-style-type':'none','margin':'0px 750px 0px 0px','padding':'20px','display':'flex','flex-direction':'row','justify-content':'flex-start', 'white-space': 'nowrap'},
	'left left header Li':{'list-style-type':' ','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px',},#logo of the header 'crypto market 
	'P Logo header':{'color':project_colors['snow'],'font-size': '36px'},
	'left right header Li':{'list-style-type':'','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px',},
	'right header Ul':{'list-style-type':'none','margin':'0px 0px 0px 0px','padding':'20px','display':'flex','flex-direction':'row','justify-content':'flex-start', 'white-space': 'nowrap'},
	'right left header Li':{'list-style-type':' '},
	'Img coin header':{'width':50,'height':50,'display':'inline'},
	'right right header Li':{'list-style-type':' '},
	'P namecoin header':{'color':project_colors['turquoise'],},
	'bodyMainDiv':{'width':'100%','height':'90%','margin':'0px 0px 0px 0px','padding':'0px','border':'0px','background-color':project_colors['darkBlue']},
	'bodyMainUl':{'width':'100%','height':'100%','margin':'0px 0px 0px 0px','padding':'0px','border':'0px','background-color':project_colors['darkBlue'],'list-style-type':'none','display':'flex','flex-direction':'row','justify-content':'flex-start', 'white-space': 'nowrap'},#The main Ul that is used to contain all the component in the body
	'bodyMainUlchild':{'width':'100%','height':'100%','margin':'0px 0px 0px 0px','padding':'0px','border':'0px','background-color':project_colors['darkBlue'],'list-style-type':' '},
	'left body Ul':{'width':'100%','height':'100%','margin':'0px 0px 0px 0px','padding':'0px','border':'0px','background-color':project_colors['darkBlue'],'list-style-type':'none','display':'flex','flex-direction':'column','justify-content':'flex-start', 'white-space': 'nowrap'},
	'left top body Li':{'list-style-type':' '},
	'interval+values, depth+values, RSI+scroll, candelsnum+scroll Ul':{'width':'100%','height':'100%','margin':'0px 0px 0px 0px','padding':'0px','border':'0px','background-color':project_colors['darkBlue'],'list-style-type':'none','display':'flex','flex-direction':'row','justify-content':'flex-start', 'white-space': 'nowrap'},
	'interval+values Li':{'list-style-type':' ','margin':'0px 0px 0px 0px','padding':'0px','border':'0px','background-color':project_colors['purple']},
	'interval+values Li Div':{'margin':'0px 0px 0px 0px','padding':'0px','border':'0px','background-color':project_colors['darkBlue']},
	'interval + values-tabs Ul':{'margin':'0px 0px 0px 0px','padding':'0px','border':'0px','background-color':project_colors['darkBlue'],'list-style-type':'none','display':'flex','flex-direction':'row','justify-content':'flex-start', 'white-space': 'nowrap'},
	'Interval Li':{'list-style-type':' ','margin':'0px 0px 0px 0px','padding':'0px','border':'0px'},
	'Li P':{'color':project_colors['turquoise'],},
	'values tabs Li':{'list-style-type':' ','margin':'0px 0px 0px 0px','padding':'0px','border':'0px'},
	'Tabs':{},
	'Tab':{},
	'depth+values Li':{'list-style-type':' '},
	'depth+values Li Div':{},
	'depth + values-tabs Ul':{'list-style-type':'none','display':'flex','flex-direction':'row','justify-content':'flex-start', 'white-space': 'nowrap'},
	'depth Li':{'list-style-type':' ','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px',},
	'RSI+input, MA+input Li':{'list-style-type':' ','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px',},
	'RSI+input, MA+input Ul':{'list-style-type':'none','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px','display':'flex','flex-direction':'row','justify-content':'flex-start', 'white-space': 'nowrap'},
	'RSI+input, MA+input Ul child':{'list-style-type':' ','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px',},
	'RSI+input Ul':{'list-style-type':'none','display':'flex','flex-direction':'row','justify-content':'flex-start', 'white-space': 'nowrap'},
	'RSI Li':{'list-style-type':' ','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px',},
	'RSILinput Li':{'list-style-type':' ','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px',},
	'inputnumeric':{},
	'MA+input Ul':{'list-style-type':'none','display':'flex','flex-direction':'row','justify-content':'flex-start', 'white-space': 'nowrap'},
	'MA Li':{'list-style-type':' ','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px',},
	'MALinput Li':{'list-style-type':' ','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px',},
	'left bottom body Li':{'width':'100%','height':'100%','list-style-type':' ','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px',},#candelstick charts 
	'left bottom body Li Div':{'width':'100%','height':'100%','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px',},#candelstick charts 
	'candlestick dcc graph':{'width':'100%','height':'100%','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px',},
	'right body Ul':{'list-style-type':'none','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px','display':'flex','flex-direction':'column','justify-content':'flex-start', 'white-space': 'nowrap'},
	'right top body Li':{'list-style-type':' ','padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px'},#pi chart
	'right top body Li Div':{'padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px',},#pi chart
	'pi dcc graph':{'padding':'0px 0px 0px 0px','margin':'0px 0px 0px 0px','padding':'0px','border':'0px',},
}

# Gathering Binance data process (clean it), add simple calculations
def PullFromBinance(ticker,interval,depth,window):
	CoinData_RAW = client.get_historical_klines(ticker, interval, depth)

	CoinDataFrame_RAW = pd.DataFrame(CoinData_RAW)
	if not CoinDataFrame_RAW.empty:
		#cleanData
        # convert timestamp to readable datetime
		CoinDataFrame_RAW[0] =  pd.to_datetime(CoinDataFrame_RAW[0],unit='ms')

		# change colmuns names from numbers
		CoinDataFrame_RAW.columns = ['Date','Open','High','Low','Close','Volume','IGNORE','Quote_Volume','Trades_Count','BUY_VOL','BUY_VOL_VAL','x']
		# Set the Date column as the index of the table 
		CoinDataFrame_RAW= CoinDataFrame_RAW.set_index('Date')

		# DELETE unecessary colmuns
		del CoinDataFrame_RAW['IGNORE']
		del CoinDataFrame_RAW['BUY_VOL']
		del CoinDataFrame_RAW['BUY_VOL_VAL']
		del CoinDataFrame_RAW['x']

		# convert to numbers (the data provided by Binance API is in JSON format)
		CoinDataFrame_RAW["Open"] = pd.to_numeric(CoinDataFrame_RAW["Open"])
		CoinDataFrame_RAW ["High"] = pd.to_numeric(CoinDataFrame_RAW["High"])
		CoinDataFrame_RAW ["Low"] = pd.to_numeric(CoinDataFrame_RAW["Low"])
		CoinDataFrame_RAW ["Close"] = pd.to_numeric(CoinDataFrame_RAW["Close"])
		CoinDataFrame_RAW ["Volume"] = round(pd.to_numeric(CoinDataFrame_RAW["Volume"]))
		CoinDataFrame_RAW ["Quote_Volume"] = round(pd.to_numeric(CoinDataFrame_RAW["Quote_Volume"]))
		CoinDataFrame_RAW ["Trades_Count"] = pd.to_numeric(CoinDataFrame_RAW["Trades_Count"])
		

		# Add New columns(Calculate the RSI values and add it to the data frame):

		delta = CoinDataFrame_RAW['Close'].diff()
		gain = delta.where(delta > 0, 0)
		loss = -delta.where(delta < 0, 0)
		avg_gain = gain.rolling(window=window).mean()
		avg_loss = loss.rolling(window=window).mean()
		rs = avg_gain / avg_loss
		CoinDataFrame_RAW['RSI'] =100 - (100 / (1 + rs))

		# save data as CSV file
		CoinDataFrame_RAW.to_csv(f'files/{ticker}.csv')
				
# Gather market data from coinmarketcap
def PullMarketDataFromCMC():
	url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest"
	
	parameters = {
	"CMC_PRO_API_KEY": API.CMCK
	}

	response = requests.get(url, params=parameters)

	data = response.json()

	total_market_cap = data["data"]["quote"]["USD"]["total_market_cap"]

	return(total_market_cap)

# Gather coin data from coinmarketcap
def PullCoinDataFromCMC(symbol):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    
    parameters = {
	"symbol": symbol,
	"CMC_PRO_API_KEY": API.CMCK
	}
    response = requests.get(url, params=parameters)
    coin_data = response.json()
    

    market_cap = coin_data["data"][symbol]["quote"]["USD"]["market_cap"]
    

    name = coin_data["data"][symbol]["name"]
   
    
    return(market_cap,name)

# Gather logos for each coin from coinmarketcap API
def logo(symbol):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/info"

    parameters = {
    "symbol":symbol
    }

    headers = {
    "X-CMC_PRO_API_KEY": API.CMCK
    }

    response = requests.get(url, params=parameters, headers=headers)

    data = response.json()

    logo_url = data['data'][symbol	]['logo']

    return(logo_url)

app = dash.Dash()

#Create  Pie chart which represents Percentage of Total Market Capitalization
def creatpiechart (coin):
	if coin !="":
	
		fig_Piechart =go.Figure(data=[go.Pie(labels=[f'Market Capitalization of {coin} ', 'The Rest of Total Market Capitalization '],
								values=[PullCoinDataFromCMC(coin)[0],PullMarketDataFromCMC()-PullCoinDataFromCMC(coin)[0],]),])
		
		#Update the traces for the Pie chart
		fig_Piechart.update_traces(
			hoverinfo='label+percent+value', 
			textinfo='percent', 
			textfont_size=20,
			textposition='inside',
			titlefont_size=19,
					
			
		)
		#Set the style for  layouts pie charst
		fig_Piechart.update_layout(
		title=dict(text='Market Capitalization Compared To Total Market Capitalization', y=0.9,x=0.5),
		autosize=False,
		width=800,
		height=600,
		margin=dict(l=50, r=50, t=100, b=100),
		legend=dict(x=0, y=-0.3, traceorder='normal', font=dict(family='sans-serif',size=14,color='#000'), bgcolor='#E5E5E5',bordercolor='#FFFFFF', borderwidth=2
        ),
        
		
		font_color=project_colors['snow'],
		font_size=13,
		legend_title_font_color=project_colors['snow'],
		uniformtext_minsize=12, 
		paper_bgcolor=project_colors['darkBlue'],
		
	)

	return fig_Piechart 

   
#Create  candelstick figure with multi y-axis whish are represent the price,voluem,RSI 
def data_visualization(ticker,interval,depth,window):
	PullFromBinance(ticker,interval,depth,window)
	data = pd.read_csv(f'files/{ticker}.csv')
	fig_data_visualization=make_subplots(
		rows=3, cols=1,shared_xaxes=True,
		specs=[
			[{"secondary_y":False}],
			[{"secondary_y": False}],
			[{"secondary_y": False}]
			]
	)
	
	# Set the style for the x-axes of fig_data_visualization 
	fig_data_visualization.update_xaxes(
		
		title_font_family="Times New Roman",
		
		
	)


	# Set the style for the candelstick cgart for second y-axes
	fig_data_visualization.update_yaxes(
	
		secondary_y=False,
		ticks='inside',
		mirror=True,
			
		
	)

	#Set the style for  layouts candelstick chart
	fig_data_visualization.update_layout(
		autosize=False,
		minreducedwidth=100,
		minreducedheight=100,
		width=1000,
		height=530,
		bargap=0.05,
		margin=dict(l=40, r=30, t=30, b=70),
		margin_autoexpand=False,#Turns on/off margin expansion computations. Legends, colorbars, updatemenus, sliders, axis rangeselector and rangeslider are allowed to push the margins by defaults.
		yaxis=dict(title='USD'),
	    yaxis2=dict(title='USD'),
	  	font_family="Times New Roman",
		font_color=project_colors['snow'],
		font_size=10,
		legend_title_font_color=project_colors['snow'],
		yaxis_tickformat='M',
		xaxis_rangeslider_visible=False ,#delet the rangeslider for the candelstick chart wihc is come with the candelstick by defaoult 
		xaxis2_rangeslider_visible=False,
		xaxis3_rangeslider_visible=True, 

		xaxis3_rangeslider_thickness=0.04,

		
		template='plotly_dark',
		plot_bgcolor=project_colors['darkestBlue'],
		paper_bgcolor=project_colors['darkestBlue'],
		legend=dict(
			orientation="h", #to make the hint for the charts visible
			yanchor="bottom",
			y=1.02,
			xanchor="right",
			x=1,
		)
	)

	# add horizontal line on 70% for the RSI
	fig_data_visualization.add_shape(
		type='line',
		x0=data['Date'].min(),
		x1=data['Date'].max(),
		y0=70,
		y1=70,
		xref='x',
		yref='y',
		row=3,
		col=1,
		line=dict(color='green', width=1, dash='dot')
	)
	# add horizontal line on 30% for the RSI
	fig_data_visualization.add_shape(
		type='line',
		x0=data['Date'].min(),
		x1=data['Date'].max(),
		y0=30,
		y1=30,
		xref='x',
		yref='y',
		row=3,
		col=1,
		line=dict(color='orange', width=1, dash='dot')
	)


	# Price Visualization 
	fig_data_visualization.add_trace(go.Candlestick(x=data['Date'], open=data['Open'], close=data['Close'],
													 high=data['High'], low=data['Low'], name='Cnadlestick'),secondary_y=False,row=1, col=1)



	# Voluem RSI Visualization
	fig_data_visualization.add_trace(go.Bar(x=data['Date'], y=data['Quote_Volume'], name='Volume',
											marker={'color':project_colors['Blue']}), secondary_y=False,row=2, col=1)


	# RSI Visualization 
	fig_data_visualization.add_trace(go.Scatter(x=data['Date'], y=data['RSI'], name='RSI',
												line=dict(color=project_colors['turquoise'],width=2.5, )),secondary_y=False,row=3, col=1)

	
	#update the traces candelstick charts 
	fig_data_visualization.update_traces(
		increasing_line_color=project_colors['turquoise'],#  change color of line bounding the box(es).the Default for it in candel stick shart is : "#3D9970" for the increasing candel
		decreasing_line_color=project_colors['pink'],#  change the color of line bounding the box(es) but for the decrasing candel
		visible=True ,
		selector=dict(type='candlestick'),
		
	)

	return fig_data_visualization

# layout design 
app.layout = html.Div(className='appDiv',children=[
	
			html.Header(className='header',
			children=[ html.Div(className='headerMainDiv',
				
				children=[
			     html.Ul(className='headerMainUl',
					children=[
					   html.Li(className='headerMainUlchild',
						children=[
							html.Ul(className='left header Ul',
								children=[
							     
                                 html.Li( className='left left header Li', #The name of the project 'Cryptoline'
									children=[
										html.B( className='P Logo header',
											children=[
					                             html.B(html.I('Cryptoline')) ,
					                        ],
					                        style=style['P Logo header'],
										)],
									style=style['left left header Li'],
								 ),
								 html.Li( className='left right header Li',# Choosing coin's symbol 
									children=[
										inputtextcoin
									],
									
								 ),
								],
								style=style['left header Ul']
							)
						],
						style=style['headerMainUlchild'],
					   ),
					   html.Li(className='headerMainUlchild',
						children=[ 
							html.Ul(className='right header Ul',
								children=[
								 html.Li(className='right left header Li', #image of coin 
								  children=[
									html.Img( className='Img coin header',id='logo',
					                  src=logo("BTC"),
					                  style=style['Img coin header'],
					
		                            ),],
								  style=style['right left header Li'],
				  
				                 ),
				                 html.Li(className='right right header Li',#name of the coin 
									children=[
					                  html.P( className='P namecoin header',
					                       children=[
					                             html.B(html.I(id='coin_name',
													children=[f"{PullCoinDataFromCMC('BTC')[1]}"]
													)) ,
					                        ],
					                        style=style['P namecoin header'],
				                      ),
									],
				                    style=style['right right header Li'],
				
				                 ),

					           ],
					           style=style['right header Ul']

				            ),
				        ],
				        style=style['headerMainUlchild']
					   ),				        
				    ],
				style=style['headerMainUl']
				),
				  
				],
				style=style['headerMainDiv'],
			),
			
			],
		   style=style['header']
		),
		
	        
	
	
	html.Div(className='bodyMainDiv',children=[
		html.Ul(className='bodyMainUl',#The main Ul that is used to contain all the component in the body
			children=[
				html.Li( className='bodyMainUlchild',
				children=[
					html.Ul( className='left body Ul',
						children=[
							html.Li(className='left top body Li ',
								children=[
									      html.Ul(className='interval+values, depth+values, RSI+scroll, candelsnum+scroll Ul',
					                        	children=[
			                                        	html.Li(className='interval+values Li',
					                                        children=[
					                                         	html.Div(className='interval+values Li Div',
							                                        children=[
								                                       html.Ul(className='interval + values-tabs Ul',
									                                       children=[
									                                        	html.Li(className='Interval Li',
																					children=[
											                                            html.P(className='Li P',
												                                            children=[html.B(html.I('Interval'))],
												                                            style=P_tag_style_interval_text,
										                                            	),
																					],
											                                        style=style['Interval Li']
									                                        	),
									                                        	html.Li(className='values tabs Li',
										                                        	children=[
											                                        	dcc.Tabs( className='Tabs',
												                                        	id='interval',
													                                        value='tab-1',
                                                                                            children=[
													                                          	dcc.Tab(className='Tab',id='1m',label='1m',value='1m',selected_style=tab_style_selected,style={'background-color':project_colors['darkBlue'],'border-color':'rgb(18, 12, 46)','color':'rgb(255, 250, 240)','border':'0','border-width':'0','border-hight':'0','padding':'30px 0px 0px 0px','margin':'1px 1px 1px 1px ','width':'23%'}),
														                                        dcc.Tab(className='Tab',id='1h',label='1h',value='1h',selected_style=tab_style_selected,style={'background-color':project_colors['darkBlue'],'border-color':'rgb(18, 12, 46)','color':'rgb(255, 250, 240)','border':'0','border-width':'0','border-hight':'0','padding':'30px 0px 0px 0px','margin':'1px 1px 1px 1px ','width':'23%'}),
														                                        dcc.Tab(className='Tab',id='1d',label='1d',value='1d',selected_style=tab_style_selected,style={'background-color':project_colors['darkBlue'],'border-color':'rgb(18, 12, 46)','color':'rgb(255, 250, 240)','border':'0','border-width':'0','border-hight':'0','padding':'30px 0px 0px 0px','margin':'1px 1px 1px 1px ','width':'23%'}),
														                                       
													                                        ],
													                                        style={'height':'10px','width':'170px','display':'inline-block','background-color':project_colors['darkBlue'],'font-style':'italic','font-weight':'bold','font-size':'15px','padding':'0px 0px 0px 0px','margin':'1px 1px 1px 1px','border-width':'0','border-hight':'0'},
												                                        )
											                                        ],
											                                        style=Liundecorated_style
										                                        ),
																				html.Li(className='values tabs Li',
																				children= Dropdown_intrval,
																				style=Liundecorated_style
																				)
										
									                                        ],
								                                        	style=Ulinline_style
							                                        	)
						                                        	]
						                                        )
				                                        	]
				                                           ,style=Liundecorated_style
				                                        ),
			                                            html.Li(className='depth+values Li',
				                                          	children=[
					                                        	html.Div(className='depth+values Li Div',
						                                         	children=[
								                                        html.Ul(className='depth + values-tabs Ul',
																			children=[
							                                            		html.Li(className='depth Li',
																					    children=[
									                                                    	html.P(className='Li P',
										                                                    	children=[html.B(html.I('depth'))],
											                                                    style=P_tag_style_interval_text,
									                                                    	)
																						],
								                                                    	),
								                                            	html.Li(className='values tabs Li',
										                                            children=[
										                                             	dcc.Tabs(className='Tabs',
												                                            id='depth',
													                                        value='tab-2',
                                                                                            children=[
														                                        dcc.Tab(className='Tab',id='1h',label='1h',value=depth_frame_options[0]['value'],selected_style=tab_style_selected,style={'background-color':project_colors['darkBlue'],'border-color':project_colors['darkBlue'],'color':'rgb(255, 250, 240)','border':'0','border-width':'0','border-hight':'0','padding':'30px 0px 0px 0px','margin':'1px 1px 1px 1px ','width':'23%'}),
														                                        dcc.Tab(className='Tab',id='1d',label='1d',value=depth_frame_options[1]['value'],selected_style=tab_style_selected,style={'background-color':project_colors['darkBlue'],'border-color':project_colors['darkBlue'],'color':'rgb(255, 250, 240)','border':'0','border-width':'0','border-hight':'0','padding':'30px 0px 0px 0px','margin':'1x 1px 1px 1px ','width':'23%'}),
														                                        dcc.Tab(className='Tab',id='1w',label='1w',value=depth_frame_options[2]['value'],selected_style=tab_style_selected,style={'background-color':project_colors['darkBlue'],'border-color':project_colors['darkBlue'],'color':'rgb(255, 250, 240)','border':'0','border-width':'0','border-hight':'0','padding':'30px 0px 0px 0px','margin':'1px 1px 1px 1px ','width':'23%'}),
														                                        
													                                        ],
													                                        style={'height':'10px','width':'170px','display':'inline-block','background-color':project_colors['darkBlue'],'font-style':'italic','font-weight':'bold','font-size':'15px','padding':'0px 0px 0px 0px','margin':'1px 1px 1px 1px','border-width':'0','border-hight':'0'},
											                                            )
										                                            ],
									                                            ),
																				html.Li(className='values tabs Li',
																				children= Dropdown_depth,
																				style=Liundecorated_style
																				)
																			],
									                                        style=Ulinline_style,
								                                        )
						                                         	]
						                                        )
					                                        ]
				                                        ),
			                                            html.Li(className='RSI+input, MA+input Li',
														    children=[
																html.Ul(className='RSI+input, MA+input Ul',
																	children=[
                                                                        html.Li( className='RSI+input, MA+input Ul child',
																			children=[
																				html.Ul(className='RSI+input Ul',
																					children=[
																						html.Li(className='RSI Li',
																							children=[
																								html.P(className='Li P',
																									children=[html.B(html.I('RSI length'))],
											                                                         style=style['Li P'],
																								),
																							],
																							style=style['RSI Li']
																						),
																						html.Li(className='RSILinput Li',
                                                                                            children=[
																								dcc.Input(className='inputnumeric',id='rsi',type='number',min=0,max=20,value=5,style=inputnumeric_style)
																							],
																							style=style['RSILinput Li'],
																						)
																					],
																					style=style['RSI+input Ul'],
																				)
																			],
																			style=style['RSI+input, MA+input Ul child'],
																		),
																	
																	],
																	style=style['RSI+input, MA+input Ul']
																)
															],
															 style=style['RSI+input, MA+input Li'],
														),
											    ],
					   	                        style=style['interval+values, depth+values, RSI+scroll, candelsnum+scroll Ul']
						                    )                                                   

							    ],
								style=style['left top body Li']
							),
							html.Li(className='left bottom body Li',#candelstich chart part 
								children=[
                                    html.Div(className='left bottom body Li Div',
										children=[ dcc.Graph(id='full_chart',className='candlestick dcc graph',figure=data_visualization("BTCUSDT","1h","3 days ago",6)),],
										style=style['left bottom body Li Div']
									),
								],
								style=style['left bottom body Li'],
							)
						],
						style=style['left body Ul']
					),
					],
					style=style['bodyMainUlchild']
					),
				
				
			
					html.Li(className='right top body Li',#pi chart
										children=[
											html.Div(className='right top body Li Div',#pi chart
												children=[dcc.Graph(className='pi dcc graph',id='pie_chart',figure=creatpiechart('BTC'),style=style['pi dcc graph'] ),

												],
												style=style['right top body Li Div']
											),
										],
										style=style['right top body Li'],
									),	
							
						
					],
			style=style['bodyMainUl']
				)
			],
			style=style['bodyMainDiv'],
			
	),
         
	
     ],
	   style=style['appDiv']
	   )
   
@app.callback([
	 Output('full_chart', 'figure'),
	 Output('logo','src'),
	 Output('coin_name','children'),
	 Output('pie_chart','figure')],
    [Input('input_currency', 'value'),
	 Input('rsi','value'),
     Input('interval_drpdown', 'value'),
	 Input('depth_dropdown', 'value'),

    ])
def update_chart(input_currency,rsi,interval_drpdown,depth_dropdown):
	Coin =str(input_currency)
	ticker = f'{Coin}USDT'
	fig_candelstick=data_visualization(ticker,interval_drpdown,depth_dropdown,rsi)
	
	
	logo1=logo(input_currency)
	coin_name=PullCoinDataFromCMC(input_currency)[1]

	#Create  Pie chart which represents Percentage of Total Market Capitalization
	fig_Piemarketcap =creatpiechart(input_currency)


	return fig_candelstick,logo1,coin_name,fig_Piemarketcap

	
if __name__ == '__main__':
  app.run_server(debug=False)