# Title: api_daily.py
# Author: cwilliams
# Date: 2022/05/04
# Purpose: Explore API scripting with Python
# Date/Name/Change
# 05/10/2022 Version handles still and moving images.
# 05/23/2022 Added code to handle key error when no copyright is provided.
# 06/02/2022 Added exception handlers for errors we should not get like no title and no date. API errors?
# 08/27/22 renamed file internally and checking into version control

#import support modules
import nasapy
import os
import pandas as pd
#from datetime import datetime
#there is some distinction between the two packages
import datetime
import urllib.request
import requests
import json
from IPython.display import Image
from pprint import PrettyPrinter
#testing pkg to enable seperating API key from main Python code.
from dotenv import load_dotenv

#Set other variables
pp = PrettyPrinter()
var_name = "NASA_API_KEY"
fh_html = open(r"C:\Users\chuck\Documents\HTML\daily.html",'w+')
l_test = True
date = datetime.date.today()

#Retrieve values given a name from the local .env file
# in this way, you can protect your API key from your public published code
def get_env_var(var_name):
    load_dotenv()
    if var_name == "":
        var_name = "NASA_API_KEY"
    my_var = os.getenv(var_name)
    if l_test:
        print("Env variable: ",my_var)
    return my_var

def gen_HTML(response):
    #Write the HTML
    fh_html.write("<!DOCTYPE html>\r\n")
    fh_html.write("<html lang=\"en\">\r\n")
    fh_html.write("  <head>\r\n")
    fh_html.write("    <meta charset=\"UTF-8\">\r\n")
    fh_html.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\>\r\n")
    fh_html.write("    <meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge\">\r\n")
    fh_html.write("    <title>APOD</title>\r\n")
    fh_html.write("    <link rel=\"stylesheet\" href=\"style.css\">\r\n")
    fh_html.write("  </head>\r\n")
    fh_html.write("  <body>\r\n")

    fh_html.write("APOD Image of the Day<br>")
    try:
        apod_date = response['date']
    except KeyError:
        apod_date = 'n/a'
    fh_html.write(apod_date+"<p>")
    try:
        apod_title = response['title']
    except KeyError:
        apod_title = 'n/a'
    fh_html.write("<i>"+apod_title+"</i><br>")
    try:
        apod_copyright = response['copyright']
    except KeyError:
        apod_copyright = ' no copyright'
    fh_html.write("&copy"+apod_copyright+"<p><br>\r\n")

    #APOD can be a still image or an animated one so two different HTML tags
    try:
        l_media_type = response['media_type']
    except KeyError:
        l_media_type = 'unk'
    if l_test:
        print('Media type: ', l_media_type)
    if l_media_type == 'video':
        l_movie_url = response['url']
        fh_html.write("<src="+str(l_movie_url)+"&autoplay=1\"frameborder=\"0\"allowfullscreen>")
        fh_html.write("</iframe>")
    else:
        try:
            l_hd_url = response['hdurl']
        except KeyError:
            l_hd_url = 'n/a'
        fh_html.write("<img src="+"\""+str(l_hd_url)+"\"><p><br>")
    
    apod_descr = response['explanation']
    fh_html.write(apod_descr)
    #testing tables
    fh_html.write("    </td>")
    fh_html.write("</table>")
    fh_html.write("	<script src=\"index.js\"></script>\r\n")
    fh_html.write("  </body>\r\n")
    fh_html.write("</html>\r\n")

    fh_html.close

    return True

def main():
    #testing
    if l_test:
        print("Date: ", date)

    #get API key info
    api_key = get_env_var(var_name)

    URL_APOD = "https://api.nasa.gov/planetary/apod"
    #date set dynamically above
    params = {
        'api_key':api_key,
        'date':date,
        'hd':'True'
      }
    response = requests.get(URL_APOD,params=params).json()

    #for testing json payload
    #to debug error "KeyError: 'hdurl'"
    if l_test:
    #    pp.pprint(response)
        try:
            print('HD URL: ',response['hdurl'])
        except KeyError:
            print('HD URL n/a')
    gen_HTML(response)

    #for testing
    #to debug error "KeyError: 'hdurl'"
    if l_test:
        pp.pprint(response)
        #print('TestingUnoDosTres')

if __name__ == "__main__":
    main()