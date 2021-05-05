#include <Arduino.h>
#include <ArduinoJson.h>
#include <Display.h>
#include <Network.h>
#include <Positioning.h>

Network network;
Positioning positioning;
Display display;

uint32_t timer = millis();
uint32_t transition_timer = millis();

bool trip_started = false;
bool show_speed = false;
int trip_id = 0;

// statistics
double trip_cost = 0.0;
double co2_emissions = 0.0;
double speed = 0.0;

// initialize variables
struct Positioning::position currentPos;
struct Network::request positionRequest;
struct Network::request tripRequest;
DynamicJsonDocument position_response(1024);

void setup() {
  // we use the serial for debugging
  Serial.begin(9600);
  Serial.println("Miljömätaren");

  // setup display
  display.setup();

  // setup positioning (GPS)
  display.print("Initializing GPS", "");
  positioning.setup();

  // setup networking
  display.print("Initializing", "network");
  network.setup();
}

void loop() {
  currentPos.success = false;
  positionRequest.success = false;

  // if loop function is OK
  if (positioning.loop() == true) {
    // approximately every 8 seconds or so, get the current position
    if (millis() - timer > 8000) {
      timer = millis(); // reset timer

      // get current position
      currentPos = positioning.get_position();

      if (currentPos.success == true) {
        // we want to start the trip of this is the first request
        if (trip_started == false) {
          display.print("Starting trip", "");
          tripRequest = network.start_trip();

          StaticJsonDocument<384> response;
          deserializeJson(response, tripRequest.response);

          trip_id = response["response"]["id"];

          if (tripRequest.success == false) {
            display.print("Network fail", "Trip not started");
            delay(1000);
          } else {
            trip_started = true;
          }
        }

        positionRequest =
            network.send_position(trip_id, currentPos.lat, currentPos.lon);

        if (positionRequest.success == true) {
          if (positionRequest.code != 200) {
            String code = String(positionRequest.code);
            display.print("HTTP fail", "Status " + code);
          }
        } else {
          display.print("Network fail", "Retrying..");
        }
        // Deserialize the JSON document
        DeserializationError error =
            deserializeJson(position_response, positionRequest.response);

        // Test if parsing succeeds.
        if (error) {
          Serial.print(F("deserializeJson() failed: "));
          Serial.println(error.f_str());
          return;
        }

        trip_cost = position_response["response"]["statistics"]["trip_cost"];
        co2_emissions =
            position_response["response"]["statistics"]["co2_emissions"];
        speed = position_response["response"]["statistics"]["speed"];
      } else {
        display.print("No GPS signal", "Locating..");
      }
    }
  };

  // transition between showing CO2 and speed
  if (millis() - transition_timer > 10000) {
    show_speed = !show_speed;
    transition_timer = millis(); // reset timer
  }

  // update display information
  if (currentPos.success == true && positionRequest.success == true &&
      positionRequest.code == 200) {
    if (show_speed == true) {
      display.print("Trip: " + String(trip_cost) + " kr",
                    String(co2_emissions) + " g CO2");
    } else {
      display.print("Trip: " + String(trip_cost) + " kr",
                    String(speed) + " km/h");
    }
  }
}
