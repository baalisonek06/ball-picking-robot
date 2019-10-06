#include <SoftwareSerial.h>
#include <Servo.h>

Servo L ;					//宣告左右馬達
Servo R ;

int s;
bool start = false;

int stop(){
   L.write(90) ;
   R.write(90) ;
}
void setup() {
  Serial.begin(9600);
  pinMode (8 , OUTPUT) ;		//設定接球刷、左右輪馬達之pin腳
  pinMode (9 , OUTPUT) ;
  pinMode (7 , OUTPUT) ;

  wait();
  L.attach(9) ;
  R.attach(7) ;
}

int wait(){
  delay(200);
  start = true;
}
void loop() {
  if( Serial.available() && start == true ){
     s = Serial.read();
     
     switch(s){				//判斷由樹梅派輸入之訊號
     case '1':
     Serial.println("Go Straight!");//直走
     L.write(180) ;
     R.write(0) ;
     digitalWrite(8, HIGH);
     
     delay(2000);
     stop();
     break;
    
    case '3':
    Serial.println("Turn right!") ;	//右轉
    L.write(180) ;
    R.write(180) ;
    delay(250);
    stop();
    break;
    
    case '2':
    Serial.println("Turn left!") ;	//左轉
    L.write(0) ;
    R.write(0) ;
    delay(250);
    stop();
    break;

    case '4':
    Serial.println("Stop!") ;	//停止
    stop();
    break;

       }    
   
   }else
   stop();
}
