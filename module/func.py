from django.conf import settings


from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction
from linebot.models import TemplateSendMessage,ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn
from linebot.models import ImagemapSendMessage, BaseSize, MessageImagemapAction, URIImagemapAction, ImagemapArea, TemplateSendMessage, ButtonsTemplate, DatetimePickerTemplateAction
from linebot.models import TextSendMessage, AudioSendMessage, VideoSendMessage
from linebot.models import BubbleContainer, ImageComponent, BoxComponent, TextComponent, IconComponent, ButtonComponent, SeparatorComponent, FlexSendMessage, URIAction
from linebot.models import TextSendMessage, ImageSendMessage, LocationSendMessage, TemplateSendMessage,ButtonsTemplate, URITemplateAction, ConfirmTemplate, PostbackTemplateAction
from linebot import LineBotApi, WebhookParser
#from hotelapi.models import booking
#from hotelapi.models import users

import datetime
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
def sendText(event):  #傳送文字
    try:
        message = TextSendMessage(  
            text = "我是 Linebot，\n您好！"
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendImage(event):  #傳送圖片
    try:
        message = ImageSendMessage(
            original_content_url = "https://i.imgur.com/4QfKuz1.png",
            preview_image_url = "https://i.imgur.com/4QfKuz1.png"
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendStick(event):  #傳送貼圖
    try:
        message = StickerSendMessage(  #貼圖兩個id需查表
            package_id='1',  
            sticker_id='2'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendMulti6(event):  #多項傳送
    try:
        message = [  #串列
            StickerSendMessage(  #傳送貼圖
                package_id='1',  
                sticker_id='2'
            ),
            TextSendMessage(  #傳送y文字
                text = "這是 Pizza 圖片！"
            ),
            ImageSendMessage(  #傳送圖片
                original_content_url = "https://i.imgur.com/4QfKuz1.png",
                preview_image_url = "https://i.imgur.com/4QfKuz1.png"
            )
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendPosition(event):  #傳送位置
    try:
        message = LocationSendMessage(
            title='101大樓',
            address='台北市信義路五段7號',
            latitude=25.034207,  #緯度
            longitude=121.564590  #經度
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendQuickreplya(event):  #快速選單
    try:
        message = TextSendMessage(
            text='請選擇最喜歡的程式語言',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="Python", text="Python")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="Java", text="Java")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="C#", text="C#")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="Basic", text="Basic")
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendButton4(event):  #按鈕樣版
    try:
        message = TemplateSendMessage(
            alt_text='按鈕樣板',
            template=ButtonsTemplate(
                    thumbnail_image_url  ='https://i.imgur.com/ZGaXkKd.jpg' ,
                    title  =  'demo' ,
                    text  =  'pizza demo' ,
            actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='文字訊息',
                        text='@購買披薩'
                    ),
                    URITemplateAction(  #開啟網頁
                        label  =  'website mcu' ,
                        uri  =  'https://web.mcu.edu.tw/'
                    ),
                    PostbackTemplateAction(  #執行Postback功能,觸發Postback事件
                        label='回傳訊息',  #按鈕文字
                        #text='@購買披薩',  #顯示文字計息
                        data='action=buy'  #Postback資料
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendConfirm(event):  #確認樣板
    try:
        message = TemplateSendMessage(
            alt_text='確認樣板',
            template=ConfirmTemplate(
                text='你確定要購買這項商品嗎？',
                actions=[
                    MessageTemplateAction(  #按鈕選項
                        label='是',
                        text='@yes'
                    ),
                    MessageTemplateAction(
                        label='否',
                        text='@no'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendCarousel3(event):  #轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='轉盤樣板',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
                        title='這是樣板一',
                        text='第一個轉盤樣板',
                        actions=[
                            MessageTemplateAction(
                                label='文字訊息一',
                                text='賣披薩'
                            ),
                            URITemplateAction(
                                label='連結文淵閣網頁',
                                uri='http://www.e-happy.com.tw'
                            ),
                            PostbackTemplateAction(
                                label='回傳訊息一',
                                data='action=sell&item=披薩'
                            ),
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/qaAdBkR.png',
                        title='這是樣板二',
                        text='第二個轉盤樣板',
                        actions=[
                            MessageTemplateAction(
                                label='文字訊息二',
                                text='賣飲料'
                            ),
                            URITemplateAction(
                                label='連結台大網頁',
                                uri='http://www.ntu.edu.tw'
                            ),
                            PostbackTemplateAction(
                                label='回傳訊息二',
                                data='action=sell&item=飲料'
                            ),
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendImgCarousel2(event):  #圖片轉盤
    try:
        message = TemplateSendMessage(
            alt_text='圖片轉盤樣板',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/4QfKuz1.png',
                        action=MessageTemplateAction(
                            label='文字訊息',
                            text='賣披薩'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/qaAdBkR.png',
                        action=PostbackTemplateAction(
                            label='回傳訊息',
                            data='action=sell&item=飲料'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendPizza(event):
    try:
        message = TextSendMessage(
            text = '感謝您購買披薩，我們將盡快為您製作。'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendYes(event):
    try:
        message = TextSendMessage(
            text='感謝您的購買，\n我們將盡快寄出商品。',
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBack_buy(event, backdata):  #處理Postback
    try:
        text1 = '感謝您購買披薩，我們將盡快為您製作。\n(action 的值為 ' + backdata.get('action') + ')'
        text1 += '\n(可將處理程式寫在此處。)'
        message = TextSendMessage(  #傳送文字
            text = text1
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBack_sell(event, backdata):  #處理Postback
    try:
        message = TextSendMessage(  #傳送文字
            text = '點選的是賣 ' + backdata.get('item')
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


def sendImgmap(event):  #圖片地圖
    try:
        image_url = 'https://i.imgur.com/Yz2yzve.jpg'  #圖片位址
        imgwidth = 1040  #原始圖片寛度一定要1040
        imgheight = 300
        message = ImagemapSendMessage(
            base_url=image_url,
            alt_text="圖片地圖範例",
            base_size=BaseSize(height=imgheight, width=imgwidth),  #圖片寬及高
            actions=[
                MessageImagemapAction(  #顯示文字訊息
                    text='你點選了紅色區塊！',
                    area=ImagemapArea(  #設定圖片範圍:左方1/4區域
                        x=0, 
                        y=0, 
                        width=imgwidth*0.25, 
                        height=imgheight  
                    )
                ),
                URIImagemapAction(  #開啟網頁
                    link_uri='http://www.e-happy.com.tw',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=imgwidth*0.75, 
                        y=0, 
                        width=imgwidth*0.25, 
                        height=imgheight  
                    )
                ),
            ]
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendDatetime(event):  #日期時間
    try:
        message = TemplateSendMessage(
            alt_text='日期時間範例',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/VxVB46z.jpg',
                title='日期時間示範',
                text='請選擇：',
                actions=[
                    DatetimePickerTemplateAction(
                        label="選取日期",
                        data="action=sell&mode=date",  #觸發postback事件
                        mode="date",  #選取日期
                        initial="2019-06-01",  #顯示初始日期
                        min="2019-01-01",  #最小日期
                        max="2020-12-31"  #最大日期
                    ),
                    DatetimePickerTemplateAction(
                        label="選取時間",
                        data="action=sell&mode=time",
                        mode="time",  #選取時間
                        initial="10:00",
                        min="00:00",
                        max="23:59"
                    ),
                    DatetimePickerTemplateAction(
                        label="選取日期時間",
                        data="action=sell&mode=datetime",
                        mode="datetime",  #選取日期時間
                        initial="2019-06-01T10:00",
                        min="2019-01-01T00:00",
                        max="2020-12-31T23:59"
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendData_sell(event, backdata):  #Postback,顯示日期時間
    try:
        if backdata.get('mode') == 'date':
            dt = '日期為：' + event.postback.params.get('date')  #讀取日期
        elif backdata.get('mode') == 'time':
            dt = '時間為：' + event.postback.params.get('time')  #讀取時間
        elif backdata.get('mode') == 'datetime':
            dt = datetime.datetime.strptime(event.postback.params.get('datetime'), '%Y-%m-%dT%H:%M')  #讀取日期時間
            dt = dt.strftime('{d}%Y-%m-%d, {t}%H:%M').format(d='日期為：', t='時間為：')  #轉為字串
        message = TextSendMessage(
            text=dt
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
     
def sendVoice(event):  #傳送聲音
    try:
        message = AudioSendMessage(
            original_content_url=baseurl + 'mario.m4a',  #聲音檔置於static資料夾
            duration=20000  #聲音長度20秒
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendVedio(event):  #傳送影像
    try:
        message = VideoSendMessage(
            original_content_url=baseurl + 'robot.mp4',  #影片檔置於static資料夾
            preview_image_url=baseurl + 'robot.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


def sendFlex(event):  #彈性配置
    try:
        bubble = BubbleContainer(
            direction='ltr',  #項目由左向右排列
            header=BoxComponent(  #標題
                layout='vertical',
                contents=[
                    TextComponent(text='冰火飲料', weight='bold', size='xxl'),
                ]
            ),
            hero=ImageComponent(  #主圖片
                url='https://i.imgur.com/3sBRh08.jpg',
                size='full',
                aspect_ratio='792:555',  #長寬比例
                aspect_mode='cover',
            ),
            body=BoxComponent(  #主要內容
                layout='vertical',
                contents=[
                    TextComponent(text='評價', size='md'),
                    BoxComponent(
                        layout='baseline',  #水平排列
                        margin='md',
                        contents=[
                            IconComponent(size='lg', url='https://i.imgur.com/GsWCrIx.png'),
                            TextComponent(text='25   ', size='sm', color='#999999', flex=0),
                            IconComponent(size='lg', url='https://i.imgur.com/sJPhtB3.png'),
                            TextComponent(text='14', size='sm', color='#999999', flex=0),
                        ]
                    ),
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='營業地址:', color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(text='台北市信義路14號', color='#666666', size='sm', flex=5)
                                ],
                            ),
                            SeparatorComponent(color='#0000FF'),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='營業時間:', color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(text="10:00 - 23:00", color='#666666', size='sm', flex=5),
                                ],
                            ),
                        ],
                    ),
                    BoxComponent(  
                        layout='horizontal',
                        margin='xxl',
                        contents=[
                            ButtonComponent(
                                style='primary',
                                height='sm',
                                action=URIAction(label='電話聯絡', uri='tel:0987654321'),
                            ),
                            ButtonComponent(
                                style='secondary',
                                height='sm',
                                action=URIAction(label='查看網頁', uri="http://www.e-happy.com.tw")
                            )
                        ]
                    )
                ],
            ),
            footer=BoxComponent(  #底部版權宣告
                layout='vertical',
                contents=[
                    TextComponent(text='Copyright@ehappy studio 2019', color='#888888', size='sm', align='center'),
                ]
            ),
        )
        message = FlexSendMessage(alt_text="彈性配置範例", contents=bubble)
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def manageForm2(event, mtext):
    try:
        flist = mtext[3:].split('/')
        text1 = '姓名：' + flist[0] + '\n'
        text1 += '日期：' + flist[1] + '\n'
        text1 += '包廂：' + flist[2]
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        


def sendUse(event):  #使用說明
    try:
        text1 ='''
1. 「房間預約」及「取消訂房」可預訂及取消訂房。每個 LINE 帳號只能進行一個預約記錄。
2. 「關於我們」對旅館做簡單介紹及旅館圖片。
3. 「位置資料」列出旅館地址，並會顯示地圖。
4. 「聯絡我們」可直接撥打電話與我們聯繫。
               '''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBooking(event, user_id):  #房間預約
    try:
       # if not (booking.objects.filter(bid=user_id).exists()):  #沒有訂房記錄
            message = TemplateSendMessage(
                alt_text = "房間預約",
                template = ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/1NSDAvo.jpg',
                    title='房間預約',
                    text='您目前沒有訂房記錄，可以開始預訂房間。',
                    actions=[
                        URITemplateAction(label='房間預約', uri='https://liff.line.me/1654180187-Y6rO6gmz')  #開啟LIFF讓使用者輸入訂房資料
                    ]
                )
            )
     #   else:  #已有訂房記錄
         #   message = TextSendMessage(
            #    text = '您目前已有訂房記錄，不能再訂房。'
          #  )
            line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendCancel(event, user_id):  #取消訂房
    try:
        if booking.objects.filter(bid=user_id).exists():  #已有訂房記錄
            bookingdata = booking.objects.get(bid=user_id)  #讀取訂房資料
            roomtype = bookingdata.roomtype
            amount = bookingdata.roomamount
            in_date = bookingdata.datein
            out_date = bookingdata.dateout
            text1 = "您預訂的房間資料如下："
            text1 += "\n房間型式：" + roomtype
            text1 += "\n房間數量：" + amount
            text1 += "\n入住日期：" + in_date
            text1 += "\n退房日期：" + out_date
            message = [
                TextSendMessage(  #顯示訂房資料
                    text = text1
                ),
                TemplateSendMessage(  #顯示確認視窗
                    alt_text='取消訂房確認',
                    template=ConfirmTemplate(
                        text='你確定要取消訂房嗎？',
                        actions=[
                            PostbackTemplateAction(  #按鈕選項
                                label='是',
                                data='action=yes'
                            ),
                            PostbackTemplateAction(
                                label='否',
                                data='action=no'
                           )
                        ]
                    )
                )
            ]
        else:  #沒有訂房記錄
            message = TextSendMessage(
                text = '您目前沒有訂房記錄！'
            )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendAbout(event):  #關於我們
    try:
        text1 = "我們提供良好的環境及優質的住宿服務，使您有賓至如歸的感受，歡迎來體驗美好的經歷。"
        message = [
            TextSendMessage(  #旅館簡介
                text = text1
            ),
            ImageSendMessage(  #旅館圖片
                original_content_url = "https://i.imgur.com/1NSDAvo.jpg",
                preview_image_url = "https://i.imgur.com/1NSDAvo.jpg"
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendPosition(event):  #位置資訊
    try:
        text1 = "地址：南投縣埔里鎮信義路85號"
        message = [
            TextSendMessage(  #顯示地址
                text = text1
            ),
            LocationSendMessage(  #顯示地圖
                title = "宜居旅舍",
                address = text1,
                latitude = 23.97381,
                longitude = 120.977198
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendContact(event):  #聯絡我們
    try:
        message = TemplateSendMessage(
            alt_text = "聯絡我們",
            template = ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/tVjKzPH.jpg',
                title='聯絡我們',
                text='打電話給我們',
                actions=[
                    URITemplateAction(label='撥打電話', uri='tel:0123456789')  #開啟打電話功能
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def manageForm(event, mtext, user_id):  #處理LIFF傳回的FORM資料
    try:
        flist = mtext[3:].split('/')  #去除前三個「#」字元再分解字串
        roomtype = flist[0]  #取得輸入資料
        amount = flist[1]
        in_date = flist[2]
        out_date = flist[3]
        
        unit = booking.objects.create(bid=user_id, roomtype=roomtype, roomamount=amount, datein=in_date, dateout=out_date)  #寫入資料庫
        unit.save()
        
        text1 = "您的房間已預訂成功，資料如下："
        text1 += "\n房間型式：" + roomtype
        text1 += "\n房間數量：" + amount
        text1 += "\n入住日期：" + in_date
        text1 += "\n退房日期：" + out_date
        message = TextSendMessage(  #顯示訂房資料
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendYes(event, user_id):  #處理取消訂房
    try:
        datadel = booking.objects.get(bid=user_id)  #從資料庫移除資料記錄
        datadel.delete()
        message = TextSendMessage(
            text = "您的房間預訂已成功刪除。\n期待您再次預訂房間，謝謝！"
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def pushMessage(event, mtext):  ##推播訊息給所有顧客
    try:
        msg = mtext[6:]  #取得訊息
        userall = users.objects.all()
        for user in userall:  #逐一推播
            message = TextSendMessage(
                text = msg
            )
            line_bot_api.push_message(to=user.uid, messages=[message])  #推播訊息
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        
def sendQuickreply(event):  #快速選單
    try:
        message = TextSendMessage(
            text='請選擇想要查詢的國內相關組織',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="行政院防制洗錢辦公室", text="https://www.amlo.moj.gov.tw/")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="法務部調查局洗錢防制處", text="https://www.mjib.gov.tw/mlpc")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="金管會", text="https://www.fsc.gov.tw/ch/index.jsp")
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        
def sendMulti2(event):  #多項傳送
    try:
        message = [  #串列

            TextSendMessage(  #傳送y文字
                text = "何謂洗錢??"
            ),
            ImageSendMessage(  #傳送圖片
                original_content_url ="https://img.itw01.com/images/2018/03/05/20/4828_rb0nUb_C75LEGQ.jpeg!r800x0.jpg",
                preview_image_url = "https://img.itw01.com/images/2018/03/05/20/4828_rb0nUb_C75LEGQ.jpeg!r800x0.jpg"
            ),

	   TextSendMessage(  #傳送y文字
                text = "洗錢:\n將其不法行為活動獲得的資金或財產，透過各種交易管道掩飾或隱匿， 轉換成為合法的資金或財產。"
            ),
	   TextSendMessage(  #傳送y文字
                text = "洗錢的架構:1.特定罪犯行為 2.取得不法利益 3.洗清黑錢"
            ),


            TextSendMessage(  #傳送y文字
                text ="https://www.youtube.com/watch?v=F-ESYoE0w0k"
	    ),

        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendButton3(event):  #按鈕樣版
    try:
        message = TemplateSendMessage(
            alt_text='重要資訊',
            template=ButtonsTemplate(
                thumbnail_image_url='https://evernote.com/blog/wp-content/uploads/2016/08/Facebook_LinkImage_1200x627-copy-1-300x300.png',  #顯示的圖片
                title=' ',  #主標題
                text='查詢特定人士：',  #副標題
                actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='查詢董監事',
                        text='https://reurl.cc/AqXVEe'
                    ),
                    MessageTemplateAction( 
                        label='查詢公司',
                        text='https://reurl.cc/AqXVEe'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendButton(event):  #按鈕樣版
    try:
        message = TemplateSendMessage(
            alt_text='洗錢小知識',
            template=ButtonsTemplate(
                thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTAbBLFzkUIGJndS970UI6i0B2jfTDs6Uy1AtyVMtMDuHwPWlWV&usqp=CAU',  #顯示的圖片
                title=' ',  #主標題
                text='查詢特定人士：',  #副標題
                actions=[
                URITemplateAction(
                        label='查詢公司名',
                        uri='https://reurl.cc/AqXVEe'
                    ),
                URITemplateAction(
                        label='查詢董監事',
                        uri='https://reurl.cc/AqXVEe'

                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))




def sendButtonb(event):  #按鈕樣版
    try:
        message = TemplateSendMessage(
            alt_text='防制洗錢小知識',
            template=ButtonsTemplate(
                thumbnail_image_url='https://cnews.com.tw/wp-content/uploads/%E5%8F%B0%E7%81%A3%E5%8F%8D%E6%B4%97%E9%8C%A2%E9%98%B2%E5%88%B6%E3%80%8C%E8%90%BD%E5%BE%8C%E3%80%8D-%E9%87%91%E7%AE%A1%E6%9C%83%E7%A0%94%E8%AD%B0%E7%9B%B8%E9%97%9C%E6%8E%AA%E6%96%BD.jpg',  #顯示的圖片
                title=' ',  #主標題
                text='國外相關組織：',  #副標題
                actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='FATF',
                        text='https://www.fatf-gafi.org/home/'
                    ),
                    MessageTemplateAction( 
                        label='APG',
                        text='http://www.apgml.org/'
                    ),
                     MessageTemplateAction( 
                        label='艾格蒙聯盟',
                        text='https://egmontgroup.org/en'
                  

                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
	

  
def sendCarousel(event):  #轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='其他',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT4NQBoplbhOoo3bc_Zgj37mraOw88ddrWP7LTZfpfnY7FcDr5m&usqp=CAU',
                        title=' ',
                        text='其他資訊',
                        actions=[
                            URITemplateAction(
                                label='洗錢防制之最終受益人查詢',
                                uri='https://reurl.cc/AqXVEe'
                            ),
                            MessageTemplateAction(
                                label='國際防制洗錢標準',
                                text='1.處罰洗錢及資恐行為2.沒收不法所得及進行目標制裁3.國際合作4.建立防治機制'
                            ),
		          
                             URITemplateAction(
                                label='最新資訊',
                                uri='https://www.amlo.moj.gov.tw/1461/1467/Lpsimplelist'
                            ),
                            
                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


