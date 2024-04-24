#include <Servo.h>

#define LED 7
#define LED_2 6

#define trigPin 3
#define echoPin 4

Servo myservo;
int pos = 0; 

long duration;
int distance;

// Function prototype
int calculateDistance();

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  pinMode(LED_2, OUTPUT);
  myservo.attach(5);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  if (Serial.available() > 0) {
    int command = Serial.read(); // Read the incoming command

    if (command == '1') { // Check if the command is 1 (blink green)
      digitalWrite(LED, HIGH); // Turn on the green LED
      delay(1000); // Wait for a second
      digitalWrite(LED, LOW); // Turn off the green LED
      delay(1000); // Wait for a second
    } 
    else if (command == '2') { // Check if the command is 2 (blink blue)
      digitalWrite(LED_2, HIGH); // Turn on the blue LED
      delay(1000); // Wait for a second
      digitalWrite(LED_2, LOW); // Turn off the blue LED
      delay(1000); // Wait for a second
    }
    else if (command == '3') { // Check if the command is 3 (move servo)
      for (pos = 0; pos <= 180; pos += 1) { 
        myservo.write(pos); // Tell servo to go to position in variable 'pos'
        delay(15); // Waits 15ms for the servo to reach the position
      }
    }
    else if (command == '4') { // Check if the command is 4 (measure distance)
      distance = calculateDistance();
      Serial.println(distance);
    }
  }
}

int calculateDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH); // Reads the echoPin, returns the sound wave travel time in microseconds
  distance = duration * 0.034 / 2;
  return distance;
}
