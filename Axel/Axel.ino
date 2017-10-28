
const int pwm = 2 ;  //initializing pin 2 as pwm
const int in_1 = 8 ;
const int in_2 = 9 ;
const int CLOCKWISE = 0;
const int COUNTERCLOCKWISE = 1;

typedef struct _MotorRequest {
   int power;
   int forward;
   int reverse;
   int vel;
   int duration;
   int direct;
} MotorRequest;

void setup() {
  // put your setup code here, to run once:
  pinMode(pwm, OUTPUT);
  pinMode(in_1, OUTPUT);
  pinMode(in_2, OUTPUT);

}

void runMotorClockwise(MotorRequest* request) {
   digitalWrite(request->forward, HIGH);
   digitalWrite(request->reverse, LOW);
   analogWrite(request->power, request->vel);
}

void runMotorCounterClockwise(MotorRequest* request) {
   digitalWrite(request->forward, LOW);
   digitalWrite(request->reverse, HIGH);
   analogWrite(request->power, request->vel);
}

void stopMotor(MotorRequest* request) {
   digitalWrite(request->forward, HIGH);
   digitalWrite(request->reverse, HIGH);
}


void runMotorForDuration(MotorRequest* request) {
  if (request->direct == CLOCKWISE) {
    runMotorClockwise(request);
  } else if (request->direct == COUNTERCLOCKWISE) {
    runMotorCounterClockwise(request);
  } else {
    return;
  }

  delay(request->duration);
}



void loop() {
  MotorRequest request = {pwm, in_1, in_2, 255, 2000, CLOCKWISE};
  runMotorForDuration(&request);
  request.direct = COUNTERCLOCKWISE;
  runMotorForDuration(&request);
  stopMotor(&request);
  delay(request.duration);
}



