#include "config.h"
#include <Arduino.h>
#include <ArduinoHttpClient.h>
#include <MKRGSM.h>

// PIN number to unlock SIM-card
const char PINNUMBER[] = SIM_PINNUMBER;

// APN data
const char GPRS_APN[] = SIM_GPRS_APN;
const char GPRS_LOGIN[] = SIM_GPRS_LOGIN;
const char GPRS_PASSWORD[] = SIM_GPRS_PASSWORD;

// Initialize library
GSMSSLClient client;
GPRS gprs;
GSM gsmAccess;

// URL, path and port
char server[] = API_HOST;
int port = 443; // port 443 is the default for HTTPS

// HTTP client library
HttpClient http = HttpClient(client, server, port);

class Network {
public:
  // connection state
  bool connected = false;

  void setup() {
    // Start GSM shield
    // pass SIM pin as parameter to begin
    // pass APN settings to attachGPRS (connect to network)
    while (!connected) {
      if ((gsmAccess.begin(PINNUMBER) == GSM_READY) &&
          (gprs.attachGPRS(GPRS_APN, GPRS_LOGIN, GPRS_PASSWORD) ==
           GPRS_READY)) {
        connected = true;
      } else {
        Serial.println("Not connected");
        delay(1000);
      }
    }

    Serial.println("GSM initialized and GPRS initialized");
  }

  void send_position(float lon, float lat) {
    char path[] = "/api/position";

    Serial.println("making POST request");
    String postData = "lon=" + String(lon) + "&lat=" + String(lat);
    http.beginRequest();
    http.post("/");
    http.sendHeader(HTTP_HEADER_CONTENT_TYPE,
                    "application/x-www-form-urlencoded");
    http.sendHeader(HTTP_HEADER_CONTENT_LENGTH, postData.length());
    http.sendHeader("X-CUSTOM-HEADER", "custom_value");
    http.endRequest();
    http.write((const byte *)postData.c_str(), postData.length());
    // note: the above line can also be achieved with the simpler line below:
    // client.print(postData);

    // read the status code and body of the response
    int statusCode = http.responseStatusCode();
    String response = http.responseBody();

    Serial.print("POST Status code: ");
    Serial.println(statusCode);
    Serial.print("POST Response: ");
    Serial.println(response);

    // Serial.println("Sending lon and lat current");
    // // if you get a connection, report back via serial:
    // if (client.connect(server, port)) {
    //   Serial.println("connected");
    //   // Make a HTTP request:
    //   client.print("GET ");
    //   client.print(path);
    //   client.println(" HTTP/1.1");
    //   client.print("Host: ");
    //   client.println(server);
    //   client.println("Connection: close");
    //   client.println();
    // } else {
    //   // if you didn't get a connection to the server:
    //   Serial.println("connection failed");
    // }
  }

  void loop() {
    // if there are incoming bytes available
    // from the server, read them and print them:
    if (client.available()) {
      char c = client.read();
      Serial.print(c);
    }

    // if the server's disconnected, stop the client:
    if (!client.available() && !client.connected()) {
      Serial.println();
      Serial.println("disconnecting.");
      client.stop();
    }
  }
};
