// https://www.arduino.cc/en/Tutorial/LibraryExamples/HelloWorld
// https://www.electrokit.com/uploads/productfile/41014/JHD202C.pdf

#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

class Display {
public:
  void setup() {
    // setup the LCD's number of columns and rows
    lcd.begin(20, 2); // our is 20x2

    // setup message
    lcd.print("Miljömätaren - Initializing");
  };
  void loop() {
    // FIXME: todo this
    lcd.setCursor(0, 0);
    lcd.print("Miljömätaren");

    lcd.setCursor(0, 1); // 1 is the second line, index starts with 0
    lcd.print("Some interesting stats here");
  }
};
