#define LED8 8
#define LED9 9

#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX


void setup() {
  Serial.begin(115200);   // 씨리얼 포트 열기 , 속도는 9600
   while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  // set the data rate for the SoftwareSerial port
  mySerial.begin(115200);
 
  pinMode(LED8, OUTPUT);
  pinMode(LED9, OUTPUT);
}
char buffer[32];        // 씨리얼 입력 데이터 버퍼
int length = 31;        // 씨리얼로 읽어올 최대 데이터

int cls;  // 

int aiGetClass(void){
  return cls;
}

int aiInteraceLoop(void){
    if (mySerial.available() > 0) {   // 데이터가 있으면
    char data = mySerial.read();      // 씨리얼 포트로 들어온 데이터를 버퍼에 저장
    buffer[0] = data;
    buffer[1] = 0;                    // 버퍼마지막데이터 끝을 0으로 만들기
    Serial.write(buffer);

    cls = atoi(buffer);               // int 로 변환
    if(cls > 9) cls=0;                // 0~9의 값만 사용함, 9보다 크면 0으로 초기화
    
    }
}

void loop() {
  aiInteraceLoop();
//Example
  if(aiGetClass() == 1){
      Serial.println("CLASS1");                          // 들어온 데이터가 1이면
      digitalWrite(LED8, LOW);    
      digitalWrite(LED9, HIGH);                                                    
  }else if (aiGetClass() == 2){
      Serial.println("CLASS2");                          // 들어온 데이터가 2이면
      digitalWrite(LED8, HIGH);   
      digitalWrite(LED9, LOW);    
  }else{
                                                         // 정의되지 않은 CLASS의 경우 Error
  }
   
}
