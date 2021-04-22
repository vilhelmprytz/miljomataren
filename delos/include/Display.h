// https://www.arduino.cc/en/Tutorial/LibraryExamples/HelloWorld
// https://www.electrokit.com/uploads/productfile/41014/JHD202C.pdf

#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

class Display {
public:
  String currentText[2]{"", ""};

  void setup() {
    // setup the LCD's number of columns and rows
    lcd.begin(16, 2); // our is 16x2
  };
  void print(String line1, String line2) {
    if (currentText[0] != line1 || currentText[1] != line2) {
      currentText[0] = line1;
      currentText[1] = line2;
      lcd.clear();

      // line 1
      lcd.setCursor(0, 0);
      lcd.print(line1);

      // line 2
      lcd.setCursor(0, 1);
      lcd.print(line2);
    }
  }
  void loop() {
    // FIXME: todo this
    lcd.setCursor(0, 0);
    lcd.print("107,2 kr");

    lcd.setCursor(0, 1); // 1 is the second line, index starts with 0
    lcd.print("2000 g CO2");
  }
};
