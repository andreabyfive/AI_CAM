#define LED8 8
#define LED9 9

#include <SoftwareSerial.h>

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
SoftwareSerial mySerial(10, 11); // RX, TX


void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  Serial.begin(115200);   // 씨리얼 포트 열기 , 속도는 9600
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only

  }
  // set the data rate for the SoftwareSerial port
  mySerial.begin(115200);

  // pinMode(LED8, OUTPUT);
  // pinMode(LED9, OUTPUT);
}
char buffer[32];        // 씨리얼 입력 데이터 버퍼
int length = 31;        // 씨리얼로 읽어올 최대 데이터

int cls;  //

int aiGetClass(void) {
  return cls;
}

int aiInteraceLoop(void) {
  if (mySerial.available() > 0) {   // 데이터가 있으면
    char data = mySerial.read();      // 씨리얼 포트로 들어온 데이터를 버퍼에 저장
    buffer[0] = data;
    buffer[1] = 0;                    // 버퍼마지막데이터 끝을 0으로 만들기
//    Serial.write(buffer);
    int k =atoi(buffer) ;
    if(k > 0 && k<10){
      cls = atoi(buffer);  
      
    }
                 // int 로 변환
    //if (cls > 9) cls = 0;             // 0~9의 값만 사용함, 9보다 크면 0으로 초기화
    return 1;
  }
  return 0;
}

void loop() {
  int tmp = 0;
  if (aiInteraceLoop() == 1) {
    //Example
    if (aiGetClass() == 1) {
    //  if (tmp == 1) {
        myservo.write(0);
        tmp = 0;
    //  }

      Serial.println("B");                          // 들어온 데이터가 0이면
     
    }
    if (aiGetClass() == 2) {
   //   if (tmp == 0) {
        myservo.write(110);
        tmp = 1;
    //  }

      Serial.println("W");                          // 들어온 데이터가 1이면
    
    }
  }

}
