// #include <LiquidCrystal.h>
// #include <SPI.h>
#include <SD.h>

File myFile;

void setup() {
  if (!SD.begin(10)) { //make sure sd card was found
    while (true);
  }
}

void loop() {
  myFile = SD.open("myfile.txt"); // open the file for reading

  if (myFile) { 
    while (myFile.available()) { //execute while file is available
      int[] = [];
      myFile.read(); //read next character from file
      delay(300);
    }

    myFile.close(); //close file
  }

  lcd.clear();
}