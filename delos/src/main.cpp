#include <Arduino.h>
#include <Network.h>
#include <Positioning.h>

Network network;
Positioning positioning;

uint32_t timer = millis();

void setup() {
  // FIXME: remove this, when no serial is avaialble code will stall
  while (!Serial)
    ; // wait for Serial to be ready

  Serial.begin(9600);
  Serial.println("Miljömätaren - web client");

  // setup networking
  network.setup();

  // setup positioning (GPS)
  positioning.setup();
}

void loop() {
  struct Positioning::position currentPos;

  // if loop function is OK
  if (positioning.loop() == true) {
    // approximately every 2 seconds or so, print out the current stats
    if (millis() - timer > 2000) {
      timer = millis(); // reset timer

      // get current position
      currentPos = positioning.get_position();

      if (currentPos.success == true) {
        bool status = network.send_position(currentPos.lat, currentPos.lon);
      }
    }
  };
}
