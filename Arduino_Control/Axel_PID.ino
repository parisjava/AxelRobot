#include <PinChangeInterrupt.h>
#include <Servo.h>
#include <PID_v1.h>

#define encA 10
#define encB 11

String inputString = "";         // a String to hold incoming data
boolean stringComplete = false;  // whether the string is complete

//ports
int motor_enA = 5;
int motor_in1 = 6;
int motor_in2 = 7;
int servo = 13;
int solOut = 50;

Servo myServo;

enum State {PLAYING, GOING, STOP};
enum ServoState {LEFT, RIGHT};
enum ServoState servoState = LEFT;
enum State state = GOING;
int index = 0;
long timer = 0;
long deadZoneTimer = 0;
boolean inDeadZone = false; 
double setpoint, input, output;

double kP = .1;
double kI = .01;
double kD = .01;

int countTick = 0;
int ctLast = 0;
int prevA = 0;
int tickA = 0;
int tickB = 0;
const int servoLeft = 103;
const int servoRight = 115;
int servoPos = servoLeft;
int notes[] = {-780,-1733,-1956, -1733, -1508, -1379,-1093, -780};
int noteTimes[] = {2, 2, 2, 1, 2, 2, 2, 1};
int numberOfNotes = 8;
int pidMode = 0; //0 is off, 1 is on, 2 is reading P, 3 is reading I, 4 is reading D, 5 is set setpoint

PID myPID(&input, &output, &setpoint, kP, kI, kD, DIRECT);

void setup() {

  pinMode(solOut, OUTPUT);
  
  pinMode(encA, INPUT_PULLUP);
  pinMode(encB, INPUT_PULLUP);

  attachPinChangeInterrupt(digitalPinToPinChangeInterrupt(encA), enc_a_change, CHANGE);
  attachPinChangeInterrupt(digitalPinToPinChangeInterrupt(encB), enc_b_change, CHANGE);
  
  pinMode(motor_enA, OUTPUT);
  pinMode(motor_in1, OUTPUT);
  pinMode(motor_in2, OUTPUT);
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  myPID.SetTunings(kP, kI, kD);
  myPID.SetOutputLimits(-1,1);
  myPID.SetMode(AUTOMATIC);
  setpoint = notes[index];
  myServo.attach(servo);
  myServo.write(servoPos);
}


void nextNote() {
  timer = 0;
  if (servoState == LEFT) {
    servoState = RIGHT;
  } else {
    servoState = LEFT;
  }
  noteTimes[index] -= 1;
  if (noteTimes[index] > 0) {
    delay(250);
    return; 
  }
  digitalWrite(solOut, LOW);
  index += 1;
  if (index == numberOfNotes) {
    state = STOP; //stop state
    return;
  }
  state = GOING;
  setpoint = notes[index];
}
void playNote() {
  if (timer == 0) {
    digitalWrite(solOut, HIGH);
    timer = millis();
  }
  if (millis() >= timer + 250) {
    playServo();
  }
  if (millis() >= timer + 2000) {
    nextNote();
  }
}

void playServo() {
  if (servoPos <= servoRight && servoState == LEFT) {
    myServo.write(servoPos++);
  }

  if (servoPos >= servoLeft && servoState == RIGHT) {
    myServo.write(servoPos--);
  }
}

void goToNote() {
  myPID.Compute();
  if (abs(input - setpoint) <= 6) {
    Serial.println("deadzone");
    output = 0;
    if (!inDeadZone) {
      deadZoneTimer = millis();
    }
    inDeadZone = true;
  } else {
    inDeadZone = false;
    deadZoneTimer = millis();
  }
  if (inDeadZone && deadZoneTimer <= millis() - 200) {
    Serial.println(setpoint);
    Serial.println("CHANGING STATE");
    state = PLAYING;
    inDeadZone = false;
  }
  runMotor(output);
}
void loop() {
  //encTick();
  input = countTick;
  //Serial.println(countTick);
  if (state == PLAYING) {
    playNote();
    return;
  }

  if (state == GOING) {
    goToNote();
    return;
  }

  //Serial.println(countTick);
  /*switch(pidMode) {
    case 1: //pid is on
      myPID.SetTunings(kP, kI, kD);
      input = countTick;
      if (abs(input - setpoint) <= 6) {
        output = 0;
      }
      else {
        myPID.Compute();
      }
      runMotor(output);
//      Serial.print("Setpoint: ");
//      Serial.print(setpoint);
//      Serial.print("\t Input: ");
//      Serial.print(countTick);
//      Serial.print("\t Output: ");
//      Serial.println(output);
      break;
    case 0:
      runMotor(0);
      if (ctLast != countTick) {
        Serial.print("tick: ");
        Serial.println(countTick);
        ctLast = countTick;
      }
      break;
    default: //setting pid or off
      runMotor(0);
      break;
  }

  // print the string when a newline arrives:
  if (stringComplete) {
    if (inputString.equals("")) {
      pidMode = 0;
      Serial.println("Stop");
    } else if (inputString.equals("start")) {
      pidMode = 2;
      Serial.println("Reading P");
    } else if (pidMode == 2) {
      kP = inputString.toDouble();
      pidMode = 3;
      Serial.print("P is set to ");
      Serial.print(kP);
      Serial.println("\nReading I");
    } else if (pidMode == 3) {
      kI = inputString.toDouble();
      pidMode = 4;
      Serial.print("I is set to ");
      Serial.print(kI);
      Serial.println("\nReading D");
    } else if (pidMode == 4) {
      kD = inputString.toDouble();
      pidMode = 1;
      Serial.print("D is set to ");
      Serial.print(kD);
      Serial.println("\nRunning PID");
    } else if (inputString.equals("setpoint")) {
      Serial.println("Reading Setpoint");
      pidMode = 5;
    } else if (pidMode == 5) {
      setpoint = inputString.toDouble();
      pidMode = 0;
      Serial.print("Setpoint is set to ");
      Serial.println(setpoint);
    } else if (inputString.equals("zero")) {
      countTick = 0;
      pidMode = 0;
      Serial.println("Zeroed");
    }
    // clear the string:
    inputString = "";
    stringComplete = false;
  }*/
}

void runMotor(int speed) {
  if (speed > 0) {
    digitalWrite(motor_in1, HIGH);
    digitalWrite(motor_in2, LOW);
    analogWrite(motor_enA, 255*speed);
  } else if (speed < 0) {
    digitalWrite(motor_in1, LOW);
    digitalWrite(motor_in2, HIGH);
    analogWrite(motor_enA, -255*speed);
  } else {
    digitalWrite(motor_in1, LOW);
    digitalWrite(motor_in2, LOW);
    analogWrite(motor_enA, 0);
  }
}

/*void encTick() {
  
  if(tickA != prevA && tickA == 1)
  {
    if(tickA != tickB)
    {
      countTick++;
    }
    else
    {
      countTick--;
    }
    if (pidMode == 0) {
        Serial.print("tick :");
        Serial.println(countTick);
    }
  }
  prevA = tickA;
}*/

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    if (inChar == '\n') {
      stringComplete = true;
      break;
    }
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
  }
}

void enc_a_change(void) {
  uint8_t trigger = getPinChangeInterruptTrigger(digitalPinToPCINT(encA));
  if(trigger == RISING) {
    tickA = 1;
  } else if (trigger == FALLING) {
    tickA = 0;
  }

  if(trigger == RISING && tickB == 1) {
    countTick++;
  } else if (trigger == RISING && tickB == 0) {
    countTick--;
  }
}
void enc_b_change(void) {
  uint8_t trigger = getPinChangeInterruptTrigger(digitalPinToPCINT(encB));
  if(trigger == RISING) {
    tickB = 1;
  } else if (trigger == FALLING) {
    tickB = 0;
  }
}
