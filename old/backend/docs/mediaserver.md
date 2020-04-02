/etc/letsencrypt/live/dating-test.webmonstr.com/fullchain.pem
/etc/letsencrypt/live/dating-test.webmonstr.com/privkey.pem

openssl pkcs12 -export -name dating-club -in /etc/letsencrypt/live/dating-test.webmonstr.com/fullchain.pem -inkey /etc/letsencrypt/live/dating-test.webmonstr.com/privkey.pem -out p12keystore.p12


keytool -importkeystore -srckeystore p12keystore.p12 -srcstoretype pkcs12 -deststoretype pkcs12 -alias dating-club -destkeystore keystore.jks




java -jar -Dopenvidu.secret=SECRET -Dopenvidu.publicurl=https://51.91.57.23:4443/ openvidu-server-2.11.0.jar




java -jar -Dopenvidu.secret=SECRET -Dopenvidu.publicurl=https://51.91.57.23:4443/ openvidu-server-2.11.0.jar -Dopenvidu.server.ssl.key-store=/root/keystore.jks  -Dopenvidu.server.ssl.key-store-password=glorytoukraine -Dopenvidu.server.ssl.key-alias=dating-club


java  -Dopenvidu.secret=SECRET -Dopenvidu.publicurl=https://dating-test.webmonstr.com:4443/ -Dopenvidu.server.ssl.key-store=/root/keystore.jks  -Dopenvidu.server.ssl.key-store-password=glorytoukraine -Dopenvidu.server.ssl.key-alias=dating-club -jar openvidu-server-2.11.0.jar


java -jar -Dopenvidu.publicurl=https://dating-test.webmonstr.com:4443 -Dopenvidu.secret=SECRET -Dserver.ssl.key-store=/root/keystore.jks -Dserver.ssl.key-store-password=glorytoukraine -Dserver.ssl.key-alias=dating-club openvidu-server-2.11.0.jar


java -jar -Dopenvidu.secret=MY_SECRET -Dserver.ssl.key-store=/opt/openvidu/my_keystore.jks -Dserver.ssl.key-store-password=MY_KEYSTORE_SECRET -Dserver.ssl.key-alias=my_cert_alias openvidu-server-2.5.0.jar








