#include <Arduino.h>
#include <Display.h>
#include <Network.h>
#include <Positioning.h>

Network network;
Positioning positioning;
Display display;

uint32_t timer = millis();

bool trip_started = false;

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
  struct Positioning::position currentPos;
  struct Network::request positionRequest;
  struct Network::request tripRequest;

  currentPos.success = false;
  positionRequest.success = false;

  // if loop function is OK
  if (positioning.loop() == true) {
    // approximately every 2 seconds or so, get the current position
    if (millis() - timer > 2000) {
      timer = millis(); // reset timer

      // get current position
      currentPos = positioning.get_position();

      if (currentPos.success == true) {
        // we want to start the trip of this is the first request
        if (trip_started == false) {
          display.print("Starting trip", "");
          tripRequest = network.start_trip();

          if (tripRequest.success == false) {
            display.print("Network fail", "Trip not started");
            delay(1000);
          } else {
            trip_started = true;
          }
        }

        positionRequest = network.send_position(currentPos.lat, currentPos.lon);

        if (positionRequest.success == true) {
          if (positionRequest.code != 200) {
            String code = String(positionRequest.code);
            display.print("HTTP fail", "Status " + code);
          }
        } else {
          display.print("Network fail", "Retrying..");
        }
      } else {
        display.print("No GPS signal", "Locating..");
      }
    }
  };

  // update display information
  if (currentPos.success == true && positionRequest.success == true &&
      positionRequest.code == 200) {
    display.loop();
  }
}
