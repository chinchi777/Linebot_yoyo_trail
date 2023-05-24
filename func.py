from django.conf import settings

from linebot import LineBotApi
from linebot.models import *
import sqlite3
import pymysql

baseurl = 'https://dd6b-36-228-148-117.ngrok.io/static/'
line_bot_api = LineBotApi('pY/ldcKO8eoXh8Xp+HqIaZyacLT5nKw1r2tgDKF7G3wUlLLY6vg1wNYZ7FeaOgGk2+9G9g5MuXodDZLVL9KBs1HNlmCWG2fodoTrCbFiNoLAfJP6XcsjjFItqR8LPxkNv58p8/vFwmsUT/d3pZoLLgdB04t89/1O/w1cDnyilFU=')

def cityData():
    return {
      "@北北基人氣步道": '''SELECT * FROM `tabletrail` WHERE 所在地 LIKE '新北市%' OR 所在地 LIKE '台北市%' OR 所在地 LIKE '基隆市%' HAVING 步道難度 ='低' ''',
      "@桃園新竹人氣步道": '''SELECT * FROM `tabletrail` WHERE 所在地 LIKE '桃園市%' OR 所在地 LIKE '新竹市%' OR 所在地 LIKE '新竹縣%' HAVING 步道難度 ='低'  ''',
      "@宜蘭人氣步道":'''SELECT * FROM `tabletrail` WHERE 所在地 LIKE '宜蘭縣%' HAVING 步道難度 ='低'   ''',
      "@苗栗人氣步道":'''SELECT * FROM `tabletrail` WHERE 所在地 LIKE '苗栗縣%' HAVING 步道難度 ='低' ''',
      "@台中南投人氣步道":'''SELECT * FROM `tabletrail` WHERE 所在地 LIKE '台中市%' OR 所在地 LIKE '南投縣%' HAVING 步道難度 ='低'   ''',
      "@彰化雲林步道":'''SELECT * FROM `tabletrail` WHERE 所在地 LIKE '彰化縣%' OR 所在地 LIKE '雲林縣%' HAVING 步道難度 ='低'   ''',
      "@嘉義人氣步道":'''SELECT * FROM `tabletrail` WHERE 所在地 LIKE '嘉義縣%' OR 所在地 LIKE '嘉義市%' HAVING 步道難度 ='低'  ''',
      "@台南人氣步道":'''SELECT * FROM `tabletrail` WHERE 所在地 LIKE '台南市%' HAVING 步道難度 ='低'   ''',
      "@高雄屏東人氣步道":'''SELECT * FROM `tabletrail` WHERE 所在地 LIKE '高雄市%' OR 所在地 LIKE '屏東縣%' HAVING 步道難度 ='低' ''',
      "@花蓮人氣步道":'''SELECT * FROM `tabletrail` WHERE 所在地 LIKE '花蓮縣%' HAVING 步道難度 ='低'  ''',
      "@台東人氣步道":'''SELECT * FROM `tabletrail` WHERE 所在地 LIKE '台東縣%' HAVING 步道難度 ='低'  ''',
      "@外島人氣步道":'''SELECT * FROM `tabletrail` WHERE 所在地 LIKE '連江縣%' OR 所在地 LIKE '金門縣%' OR 所在地 LIKE '澎湖縣%' HAVING 步道難度 ='低'  ''',
      "@新手入門步道":'''SELECT * FROM `tabletrail` WHERE 步道難度 LIKE '低'   ''',
      "@需要體力步道":'''SELECT * FROM `tabletrail` WHERE 步道難度 LIKE '低-中'   ''',
      "@體力訓練步道":'''SELECT * FROM `tabletrail` WHERE 步道難度 LIKE '中' OR 步道難度 LIKE '中-高'  ''',
      "@專業級步道":'''SELECT * FROM `tabletrail` WHERE 步道難度 LIKE '高'   '''
          
              
    }
    
 
      

def sendCarousel_trail(event):  #轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='步道查詢方式',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
 					    #thumbnail_image_url=baseurl +'蘋果.jpg',
                        title='依照地區選擇',
                        text='從北到南步道走透透',
                        actions=[
                            MessageTemplateAction(
                                label='請點選這裡',
                                text='@步道分區'
                            ),                            
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=baseurl +'蘋果.jpg',
                        title='依照難度選擇',
                        text='五星難度最高 一星最適合入門',
                        actions=[
                            MessageTemplateAction(
                                label='請點選這裡',
                                text='@步道難度'
                            ),                           
                        ]
                    ),
 					CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
						#thumbnail_image_url=baseurl +'蘋果.jpg',
                        title='依照所在位置附近找尋',
                        text='取得您的定位 找尋附近最熱門步道',
                        actions=[
                            MessageTemplateAction(
                                label='定位請點選這裡',
                                text='@抓取定位'
                            ),
                            
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendArea(event):  #分區轉盤
    try:
        message = TemplateSendMessage(
            alt_text='分區查詢',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.pinimg.com/474x/d1/68/6b/d1686b88be5002dd960afde8c8dd4404.jpg',
 					    # thumbnail_image_url=baseurl +'north.jpeg',
                        title='北部步道',
                        text='精選各區人氣步道 請選擇城市',
                        actions=[
                            MessageTemplateAction(
                                label='北北基步道',
                                text='@北北基人氣步道'
                            ),
                            MessageTemplateAction(
                                label='桃園新竹步道',
                                text='@桃園新竹人氣步道'
                            ),
                            MessageTemplateAction(
                                label='宜蘭步道',
                                text='@宜蘭人氣步道'
                            ),                                                                                  
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.pinimg.com/474x/27/17/47/271747fd82b8e70f23a1a23d329f7458.jpg',
                        title='中部步道',
                        text='精選各區人氣步道 請選擇城市',
                        actions=[
                            MessageTemplateAction(
                                label='苗栗步道',
                                text='@苗栗人氣步道'
                            ),
                            MessageTemplateAction(
                                label='台中南投步道',
                                text='@台中南投人氣步道'
                            ),
                            MessageTemplateAction(
                                label='彰化雲林步道',
                                text='@彰化雲林步道'
                            ),
                            
                        ]
                    ),
 					CarouselColumn(
                        thumbnail_image_url='https://i.pinimg.com/474x/86/f4/7c/86f47c4d97d5aa10ad870c03aad6dd37.jpg',
# 						thumbnail_image_url=baseurl +'south.jpg',
                        title='南部步道',
                        text='精選各區人氣步道 請選擇城市',
                        actions=[
                            MessageTemplateAction(
                                label='嘉義步道',
                                text='@嘉義人氣步道'
                            ),
                            MessageTemplateAction(
                                label='台南步道',
                                text='@台南人氣步道'
                            ),
                            MessageTemplateAction(
                                label='高雄屏東步道',
                                text='@高雄屏東人氣步道'
                            ),
                            
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.pinimg.com/474x/76/cc/55/76cc550a88d8b8af280f55582af44656.jpg',
# 						thumbnail_image_url=baseurl +'east.jpg',
                        title='東部及外島步道',
                        text='精選各區人氣步道 請選擇城市',
                        actions=[
                            MessageTemplateAction(
                                label='花蓮步道',
                                text='@花蓮人氣步道'
                            ),
                            MessageTemplateAction(
                                label='台東步道',
                                text='@台東人氣步道'
                            ),
                            MessageTemplateAction(
                                label='外島步道',
                                text='@外島人氣步道'
                            ),
                            
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendDiff(event):  #難度轉盤
    try:
        message = TemplateSendMessage(
            alt_text='難度查詢',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.pinimg.com/564x/94/83/a3/9483a30a072972fa347e98ef1373f052.jpg',
 					    #thumbnail_image_url=baseurl +'蘋果.jpg',
                        title='難度入門級',
                        text='最簡單就能登高看景',
                        actions=[
                            MessageTemplateAction(
                                label='新手也能輕鬆完成步道推薦',
                                text='@新手入門步道'
                            ),                            
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.pinimg.com/564x/33/c1/41/33c14196ea7c90630da55a3273b3079a.jpg',
                        title='難度中階級',
                        text='培養健行的興趣',
                        actions=[
                            MessageTemplateAction(
                                label='適合稍有體力的新手',
                                text='@需要體力步道'
                            ),                            
                        ]
                    ),
 					CarouselColumn(
                        thumbnail_image_url='https://i.pinimg.com/564x/03/18/ea/0318ea2c22a193fe877854559e16a552.jpg',
						#thumbnail_image_url=baseurl +'蘋果.jpg',
                        title='難度進階級',
                        text='美景與體力的挑戰',
                        actions=[
                            MessageTemplateAction(
                                label='朝百岳邁進的訓練步道',
                                text='@體力訓練步道'
                            ),                            
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.pinimg.com/564x/ae/94/d9/ae94d9f88e89db041b04c28cbb2cc3ed.jpg',
						#thumbnail_image_url=baseurl +'蘋果.jpg',
                        title='難度大魔王級',
                        text='登山能力者的清單',
                        actions=[
                            MessageTemplateAction(
                                label='百岳集點快來收集',
                                text='@專業級步道'
                            ),                            
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendAnaly(event):  #分析轉盤
    try:
        message = TemplateSendMessage(
            alt_text='資料分析',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.pinimg.com/564x/94/83/a3/9483a30a072972fa347e98ef1373f052.jpg',
 					    #thumbnail_image_url=baseurl +'蘋果.jpg',
                        title='步道難易數量',
                        text='低難度步道有近1200條可選擇，新手可以多多嘗試再慢慢進階',
                        actions=[
                            URIAction(label='看分析圖大圖',url='https://i.pinimg.com/564x/ae/94/d9/wiufn4972oih3974rheurnjf8746d84bd.jpg')
                        ]

                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.pinimg.com/564x/33/c1/41/33c14196ea7c90630da55a3273b3079a.jpg',
                        title='步道分區數量',
                        text='新北市瑞芳區步道數量就有40多條，住在北部的民眾可多去走走',
                        actions=[
                            URIAction(label='看分析圖大圖',url='https://i.pinimg.com/564x/ae/94/d9/ou3u4895ofhyh3u4mfklgo484hfkfd93k.jpg')
                        ]

                    ),
 					
                    CarouselColumn(
                        thumbnail_image_url='https://i.pinimg.com/564x/ae/94/d9/ae94d9f88e89db041b04c28cbb2cc3ed.jpg',
						#thumbnail_image_url=baseurl +'蘋果.jpg',
                        title='高難度步道分佈',
                        text='高難度步道在全台分佈的數量跟區域，北部佔比較高',
                        actions=[
                            URIAction(label='看分析圖大圖',url='https://i.pinimg.com/564x/ae/94/d9/siwu4847ehdfk947ehdkf4734jjk4hhfn.jpg')
                        ]

                    ),                            
                ]
            )
        )
    
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def buildBubble(key):#設定bubble的形式把資料丟進去
        queries = cityData()
        conn = pymysql.connect(host='localhost',port=3306,db='projectpython',user='root',passwd='cc19850119',charset='utf8')
        cur = conn.cursor()
        # sql ='''SELECT * FROM `tabletrail` WHERE 所在地 LIKE '新北市%' OR 所在地 LIKE '台北市%' OR 所在地 LIKE '基隆市%' HAVING 步道難度 ='低' ORDER BY 到過人數 DESC '''
        cur.execute(queries[key])
        result=cur.fetchmany(10)
        # print(result)
        bb_list=[]
        
        for item in result:
            bubble = BubbleContainer(  #建立起整個框架，也就是layout部份
                direction='ltr',  #項目由左向右排列
                header=BoxComponent(  #標題
                    layout='vertical',
                    background_color="#326229",
                    contents=[
                        TextComponent(text=item[0], weight='bold', size='xl',color="#eff7ed"),
                    ]
                ),
                hero=ImageComponent(  #主圖片
                    url=item[2],
                    size='full',
                    aspect_ratio='3:2',  #長寬比例
                    aspect_mode='cover',
                ),
                body=BoxComponent(  #主要內容
                    layout='vertical',
                    contents=[                   
                        BoxComponent(
                            layout='baseline',#水平排列
                            direction='ltr', 
                            margin='md',
                            contents=[
                                TextComponent(text='難度:'+item[4], size='md'),
                                IconComponent(size='md', url='https://cdn-icons-png.flaticon.com/512/762/762437.png'),                           
                            ]
                        ),
                        BoxComponent(
                            layout='vertical',  #垂直排列                    
                            contents=[
                                TextComponent(text='所在地:'+item[1], size='md'), 
                                TextComponent(text='步道長度:'+item[5], size='md'),
                                TextComponent(text='完成:'+item[6], size='md'),                         
                            ]
                        ),                                       
                        BoxComponent(  
                            layout='horizontal',
                            margin='xxl',
                            contents=[
                                ButtonComponent(
                                    style='primary',
                                    height='sm',
                                    color="#326229",
                                    action=URIAction(label='查看路線圖', uri=item[10]),
                                ),
                                ButtonComponent(
                                    style='secondary',
                                    height='sm',
                                    color="#8cca81",
                                    action=URIAction(label='查看地圖',uri="https://hiking.biji.co"+item[11])
                                
                                
                                )
                            ]
                        )
                    ],
                ),
                footer=BoxComponent(  #底部文字
                    layout='vertical',
                    contents=[
                        ButtonComponent(
                            style='link',
                            height='sm',              
                            action=URIAction(label='更多資訊', uri="https://hiking.biji.co"+item[3]),
                        ),
                    ]
                ),
                
            )
            bb_list.append(bubble)
        
        return  bb_list 

        
      
        

# func.buildBubble(event)
        
def sendFlex(event, key):  #彈性配置
    try:
        
        bb_list = buildBubble(key)
        
        ca=CarouselContainer(bb_list) #合併所有bubble
        # conn.close()
        message = FlexSendMessage(alt_text="北部人氣步道", contents=ca)
        # message = FlexSendMessage(alt_text="彈性配置範例", contents=bubble)
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


