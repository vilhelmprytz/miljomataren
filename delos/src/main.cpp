#include <Arduino.h>
#include <Network.h>
#include <Positioning.h>

Network network;
Positioning positioning;

void setup() {
  Serial.begin(9600);
  Serial.println("Miljömätaren - web client");

  // setup networking
  network.setup();

  // setup positioning (GPS)
  positioning.setup();
}

void loop() { network.send_position(12.34, 23.21); }
