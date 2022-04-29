#include <ESP8266WiFi.h>
#include <Hash.h>
#include <MySQL.h>
 
// Set WiFi credentials
#define WIFI_SSID "YOUR WIFI NETWORK SSID"
#define WIFI_PASS "YOUR WIFI PASSWORD"

// db credentials
char server_addr ="";
static char user[]="";
static char dbpassword[]="";
static char db[]="";


Connector my_conn;
 
void setup() {
  wifi_setup();

  if (my_conn.mysql_connect(server_addr,3306,user,dbpassword)){
    Serial.println("connection ok");
    delay(1000);
  }
  else{
    Serial.println("connection fail");
  }
}


void wifi_setup(){
  // Setup serial port
  Serial.begin(115200);
  Serial.println();
 
  // Begin WiFi
  WiFi.begin(WIFI_SSID, WIFI_PASS);
 
  // Connecting to WiFi...
  Serial.print("Connecting to ");
  Serial.print(WIFI_SSID);
  // Loop continuously while WiFi is not connected
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(100);
    Serial.print(".");
  }
 
  // Connected to WiFi
  Serial.println();
  Serial.print("Connected! IP address: ");
  Serial.println(WiFi.localIP());

}
  
void loop() {
  //use this to insert things to my sql
  my_conn.cmd_query(whatever I want) 
}
