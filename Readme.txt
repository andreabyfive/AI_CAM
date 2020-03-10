<ARDUINO_Serial>
ESP32-CAM과 UART로 0~9 값을 전달받아 CLASS를 구분하도록 인터페이스 함. 
UART 속도 : 115200
STRING : 0~9 까지의 string 값 

<CameraWebServer>
ESP32-CAM 용 프로그램 
[코드 업로드하는 과정] 

1.       Tools> Board로 가서 ESP32 Wrover Module을 선택.

2.       도구> 포트로 이동하여 ESP32가 연결된 COM 포트를 선택.

3.       도구> 파티션 구성표에서 "거대한 APP (3MB No OTA)"를 선택.

4.       ESP32-CAM 온보드 RESET 버튼을 누릅니다.

5.       그런 다음 업로드 버튼을 클릭하여 코드를 업로드 해주세요.
