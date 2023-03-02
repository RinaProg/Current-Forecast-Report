from flask import Flask,render_template ,request        
import requests
import datetime as date ,datetime

app=Flask(__name__)

ownkey = ""  # use your own api key..

@app.route('/' , methods=['GET','POST'])
def weather():
    if request.method =='POST':
        location = request.form.get('city')
        
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={ownkey}"
        
        api_link = requests.get(api_url)
        api_data = api_link.json()
        day=date.date.today()
        now = datetime.datetime.today()
        time = now.strftime("%H:%M %p")

        if api_data['cod'] =='404':
           
            return render_template('errorpg.html',location=location)    
        
        else:
            
            wea_main= (api_data['weather'][0]['main'])
            wea_desc= (api_data['weather'][0]['description'])
            wea_icon= (api_data['weather'][0]['icon'])
            temp1    = ((api_data['main']['temp']) - 273.15)
            temp     = round(temp1,)
            mintemp  =((api_data['main']['temp_min']) - 273.15)
            mintemp1 =round(mintemp,)
            maxtemp  =((api_data['main']['temp_max']) - 273.15)
            maxtemp1 =round(maxtemp,)
            humid    = (api_data['main']['humidity'])
            speed    = (api_data['wind']['speed'])
            
                
            return render_template('test.html',temp=temp,humid=humid,speed=speed,
            location=location,wea_desc=wea_desc, wea_icon=wea_icon, mintemp1=mintemp1,maxtemp1=maxtemp1, wea_main=wea_main,day=day,time=time)
    return render_template('test.html')
    
if __name__=='__main__':
    app.run(debug=True)

    