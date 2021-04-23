#define ARDUINOJSON_USE_DOUBLE 1

#include "config.h"
#include <Arduino.h>
#include <ArduinoHttpClient.h>
#include <ArduinoJson.h>
#include <MKRGSM.h>

// PIN number to unlock SIM-card
const char PINNUMBER[] = SIM_PINNUMBER;

// APN data
const char GPRS_APN[] = SIM_GPRS_APN;
const char GPRS_LOGIN[] = SIM_GPRS_LOGIN;
const char GPRS_PASSWORD[] = SIM_GPRS_PASSWORD;

// API
const int CAR_ID = API_CAR_ID;
const char TOKEN[] = API_TOKEN;

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

  struct request {
    String response;
    int code;
    bool success;
  };

  struct request api_request(String url, String json) {
    Serial.println("POST to " + url);
    http.beginRequest();
    http.post(url);
    http.sendHeader(HTTP_HEADER_CONTENT_TYPE, "application/json");
    http.sendHeader(HTTP_HEADER_CONTENT_LENGTH, json.length());
    http.sendHeader("Authorization", TOKEN);
    http.endRequest();
    http.write((const byte *)json.c_str(), json.length());
    // note: the above line can also be achieved with the simpler line below:
    // client.print(postData);

    // read the status code and body of the response
    int statusCode = http.responseStatusCode();
    String response = http.responseBody();

    Serial.print("POST Status code: ");
    Serial.println(statusCode);
    Serial.print("POST Response: ");
    Serial.println(response);

    return request{response, statusCode, true};
  }

  struct request start_trip() {
    // preperare data as JSON blob
    StaticJsonDocument<16> doc;
    doc["car_id"] = API_CAR_ID;

    // Serialize JSON document
    String json;
    serializeJson(doc, json);

    return api_request("/api/trip", json);
  };

  struct request send_position(int trip_id, float lat, float lon) {
    // preperare data as JSON blob
    StaticJsonDocument<48> doc;
    doc["lat"] = lat;
    doc["lon"] = lon;
    doc["trip_id"] = trip_id;

    // Serialize JSON document
    String json;
    serializeJson(doc, json);

    return api_request("/api/position", json);
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
