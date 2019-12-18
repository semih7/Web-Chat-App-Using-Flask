from flask import Flask, render_template                  #flask kütüphanesi import edildi.
from flask_socketio import SocketIO, emit                 #soket kütüphanesi alındı.
from socket import *

host = "localhost"
port = 8080

addr = (host,port)
sck = socket(AF_INET, SOCK_DGRAM)


app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'FurkanOnerSemihSiyahdemir330202330206'      #şifreleme anahtarı oluşturuldu.
socketio = SocketIO( app )                                                #Flask ile soketlerin birlikte kullanılması sağlandı.

@app.route( '/' )
def index():
  return render_template( './index.html' )               #index.html dosyası döndürüldü

def messageRecived():
  print( 'message was received!!!' )                #mesaj geldiğinde çalışan fonksiyon

@socketio.on( 'my event' )    
def handle_my_custom_event( json ):         #olaylara göre çalışan fonksiyon
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )

if __name__ == '__main__':
  socketio.run( app, debug = True )