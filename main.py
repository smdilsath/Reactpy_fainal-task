from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient


@component
def MyCrud():
    ## Creating state
    alltodo = use_state([])
    name, set_name = use_state("")
    password, set_password = use_state("")
    age, set_age = use_state("")  # New state for age
    address, set_address = use_state("")
    email,set_email=use_state("")


    def mysubmit(event):
        newtodo = {"name": name, "password": password, "age": age," address":  address,"email":email}  # Include age in newtodo

        # push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo])
        login(newtodo)  # function call to login function using the submitted data

    def handle_age_change(event):  # Event handler for age input change
        set_age(event["target"]["value"])

    def handle_address_change(event):  # Event handler for age input change
        set_address(event["target"]["value"])
    def handle_email_change(event):  # Event handler for email input change
        set_email(event["target"]["value"])    

    def clear_form():## set name define with set name thaty we put here to set name
        set_name("")
        set_password("")
        set_age("")
        set_address("")
        set_email("")
    # looping data from alltodo to show on web
    list = [
        html.li(
            {},
            f"{b} => {i['name']} ; {i['password']} ; {i['age']}; {i[' address']};{i['email']}",  # Include age in display
        )
        for b, i in enumerate(alltodo.value)
    ]

    def handle_event(event):
        print(event)
        ##start point return mean return the out put 
        ##  html.div 
    return html.div(
        {
            "style": {
                "background-color": "#171819",  # Background color for the form
                "border": "3px solid #ced4da",  # Border for the form
                "padding": "40px 25px",              ## inside the box we want to increase padding use 
                "margin": "60px 550px",        ## out side of box it call margin 
                 "border-radius": "25px",
                 "box-shadow": "0 20px 25px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23)",
                "color": "green" # Padding for the form
            }
        },
     
        html.form(
            {"on_submit": mysubmit},   
            html.h2("Login Form - ReactPy connect to Mongodb"),
            html.hr(),
            html.br(),
            html.label(                    ####   in this line label name willl show
                {"for": "name", "style": {"margin-right": "20px"}},
                "Name:"
            ),
            html.input(                ##  input tag 
                {
                    "type": "text",
                    "id": "name",
                    "placeholder": "Name",
                    "on_change": lambda event: set_name(event["target"]["value"]),
                    "style": {
                        "width": "100%",
                        "padding": "25px 10px",
                         "margin-top": "8px",
                        "margin-bottom": "25px",
                        "border": "2px solid #ced4da",
                        "border-radius": "6px",
                        "box-sizing": "border-box",
                    },
                }
            ),
            html.br(),
            html.br(),
            html.label(
                {"for": "password", "style": {"margin-right": "20px"}},
                "Password:"
            ),
            html.input(
                {
                    "type": "password",
                    "id": "password",
                    "placeholder": "Password",
                    "on_change": lambda event: set_password(event["target"]["value"]),
                    "style": {
                        "width": "100%",
                       "padding": "25px 10px",
                         "margin-top": "8px",
                        "margin-bottom": "25px",
                        "border": "2px solid #ced4da",
                        "border-radius": "6px",
                        "box-sizing": "border-box",
                    },
                }
            ),
            html.br(),
            html.br(),
            html.label(
                {"for": "age", "style": {"margin-right": "20px"}},
                "Age:"
            ),
            html.input(
                {
                    "type": "number",
                    "id": "age",
                    "placeholder": "Age",
                    "on_change": handle_age_change,
                    "style": {
                        "width": "100%",
                       "padding": "25px 10px",
                         "margin-top": "8px",
                        "border": "2px solid #ced4da",
                        "border-radius": "6px",
                        "box-sizing": "border-box",
                    }
                }
            ),
            html.br(),
            html.br(),
            html.label(
                {"for": " address", "style": {"margin-right": "10px"}},
                " address:"
            ),
            html.input(
                {
                    "type": " address",
                    "id": " address",
                    "placeholder": " address",
                    "on_change": handle_address_change,
                    "style": {
                        "width": "100%",
                        "padding": "25px 10px",
                         "margin-top": "8px",
                        "border": "2px solid #ced4da",
                        "border-radius": "6px",
                        "box-sizing": "border-box",
                    }
                }
            ),
            html.input(
                {
                 "type": "email",  # Changed type to "email"
                    "id": "email",
                    "placeholder": "E-mail",
                    "on_change": handle_email_change,
                    "style": {
                        "width": "100%",
                        "padding": "15px 8px",
                        "margin-top": "5px",
                        "border": "1px solid #ced4da",
                        "border-radius": "4px",
                        "box-sizing": "border-box",

                    }
                }
            ),    
            html.div(                    ## this for button css.  in a single div there are to buttons
                {
                    "style": {
                        "display": "flex",
                        "justify-content": "space-between",
                        "margin-top": "25px",
                    }
                },
                html.button(
                    {
                        "type": "submit",
                        "on_click": event(lambda event: mysubmit(event), prevent_default=True),
                        "style": {
                            "background-color": "#007bff",
                            "color": "yellow",
                            "border": "none",
                            "border-radius": "6px",
                            "padding": "25px 30px",
                            "cursor": "pointer",
                        },
                    },
                    "Submit",
                ),
                html.button(
                    {
                        "type": "submit",
                         "on_click": clear_form,
                        "style": {
                            "background-color": "#dc3545",
                            "color": "yellow",
                            "border": "none",
                            "border-radius": "6px",
                            "padding": "25px 30px",
                            "cursor": "pointer",
                        },
                    },
                    "Clear",
                ),
            ),
        ),
    #    html.ul(list),
    )


app = FastAPI()

from pymongo.mongo_client import MongoClient 
from pymongo.server_api import ServerApi


#copy and paste the mongo DB URI
uri= "mongodb+srv://dilsathaus:dil1234@cluster0.brwfbp6.mongodb.net/"
client= MongoClient(uri, Server_api=ServerApi("1"))  #camel case 

#defining the Db name 
db= client ["react_py"]
collection=db["task1"]

#checking the connection 
try:
    client.admin.command("Ping")
    print("Successfully Connected MongoDB")

except Exception as e:
       print(e)

def login(
          login_data:dict,
):          #removed async,, since wait makes code execution pasuse for the promise to resolve anyway
    username = login_data["name"]
    password = login_data["password"]
    age = login_data["age"]  # Get the age from login_data
    address= login_data[" address"]

    document = {"name": username, "password": password, "age": age, " address":  address} 
    print(document)

    post_id = collection.insert_one(document).inserted_id   ##insert document
    print(post_id)

    return {"message":"Login successful"}

    

configure(app, MyCrud)