from flask import Flask,request,jsonify,render_template
#request present in flask we write code as from flask import Flask,request

#Need to give apps name so that it can understand which app it is talking about
#__name__ is private variable which is already stored
app=Flask(__name__)

#Now we will start handling the request. For request we need to use route(for which url you are considering)
@app.route("/")#When do /, it becomes home page
#Inside bracket we provide for which page or which url, how my application should behave
#Need to provide function which can handle this route
# Two types: Get request and Post request
#Get request:www.google.com
#Post request: searching something in search engine
#If don't provide any methods, then it become get request
#def hello_world():
#    return "Hello World"
#Slash means i will be redirected to this func hello_world
def welcome():
    return render_template("index.html")
#We want to make index.html as home page, so we will take help of render_template and give 
#input of homepage.html. It basically checks whether that file is present or not

@app.route("/aboutus")
def aboutus():
    return "<h1>We are ineuron</h1>"

#How to handle post request?
@app.route('/demo',methods=['POST'])#Handle post only but if given both input, then will handle both
def math_operation():
    #Whatever we input get stored in server and we can retrieve it with the help of request
    if(request.method=='POST'):
        #Whatever we are giving as input will be retrieved with the help of this.
        #whatever we enter will be stored in object request
        #Whenever we use request we need data in json form and can we retrieve it? Yes
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        result=0

        if operation=="add":
            result=num1+num2
        elif operation=="multiply":
            result= num1*num2
        elif operation=="division":
            result= num1/num2
        else:
            result=num1-num2
        return jsonify("The operation is {} and the result is {}".format(operation,result))
        #Will get result in form of Json

#        return "The operation is {} and the result is {}".format(operation,result) - will get result in html form
@app.route('/operation',methods=['POST'])
def operation():
    #Whatever we input get stored in server and we can retrieve it with the help of request
    if(request.method=='POST'):
        #Whatever we are giving as input will be retrieved with the help of this.
        #whatever we enter will be stored in object request
        #Whenever we use request we need data in json form and can we retrieve it? Yes
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=0

        if operation=="add":
            result=num1+num2
        elif operation=="multiply":
            result= num1*num2
        elif operation=="division":
            result= num1/num2
        else:
            result=num1-num2
#        return "The operation is {} and the result is {}".format(operation,result)
        return render_template("result.html",result=result)
#Once done open postman to test the API, change to post, https://green-accountant-xbrcy.ineuron.app:5000/demo
#Select Body,raw, JSON and paste the content from json file

#@app.route('/multiply',methods=['POST'])
#def multiply_operation():
#    if(request.method=='POST'):
#        operation=request.json['operation']
#        num1=request.json['num1']
#        num2=request.json['num2']
#        result=num1*num2

#        return "The operation is {} and the result is {}".format(operation,result) 

# Telling that this is the entry point of Flask
if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000 )# It is telling about the local address
    #This will automatically map to local address/the cloud ip address /where this program is running
    #If you want to run in local, then IP address that we use is 127.0.0.1
    #Port tells that wherever it is running, through which specific port this app can be accessed.
    # SUppose we are not able to access through 1 port, means that is closed 

#When we run command python app.py in terminal, we get three server name,
#1. where program running 2. local ip address and 3. is server ip address
# Can we access this IP? No as this IP is mapped to url: https://lemon-artist-kfwzx.ineuron.app/
#Open new tab with above url:5000 and will get page NOT Found, URL not found in server
#Showing error port 5000 is not using then change the port no to 5001
#We got 404 as we didn't handled any specific request