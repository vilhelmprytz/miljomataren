#include <Arduino.h>
#include <Network.h>
#include <Positioning.h>

Network network;
Positioning positioning;

void setup() {
  // FIXME: remove this, when no serial is avaialble code will stall
  while (!Serial); // wait for Serial to be ready

  Serial.begin(9600);
  Serial.println("Miljömätaren - web client");

  // setup networking
  // network.setup();

  // setup positioning (GPS)
  positioning.setup();
}

void loop() { 
  // fuck
  positioning.get_position();
 }
