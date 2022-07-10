//20183026 류준호
#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include <Servo.h>

LiquidCrystal_I2C lcd(0x27,16,2);

Servo servo1;
Servo servo2;

int value = 0;

int debounce_time=10;
boolean lastButton_state2 = LOW;
boolean currentButton_state2 = LOW;

boolean lastButton_state3 = LOW;
boolean currentButton_state3 = LOW;

boolean lastButton_state4 = LOW;
boolean currentButton_state4 = LOW;

boolean lastButton_state5 = LOW;
boolean currentButton_state5 = LOW;

int money = 0;


void setup() {

  Serial.begin(9600);
  lcd.begin();
  lcd.print(money);

  servo1.attach(10);
  servo2.attach(4);
} 

void loop() { 
  currentButton_state2 = debounce_sw(lastButton_state2, 8);
  currentButton_state3 = debounce_sw(lastButton_state3, 9);
  currentButton_state4 = debounce_sw(lastButton_state4, 6);
  currentButton_state5 = debounce_sw(lastButton_state5, 7);

  //500원(오른쪽)
  if (lastButton_state4 != currentButton_state4 )
  {
    if (lastButton_state4 == HIGH && currentButton_state4 == LOW)
    {
      money = money + 500;
      lcd.clear();
      lcd.print(money);
     }
    lastButton_state4 = currentButton_state4; // 버튼 상태 갱신
   }

  //1000원(왼쪽)
  if (lastButton_state5 != currentButton_state5 )
  {
    if (lastButton_state5 == HIGH && currentButton_state5 == LOW)
    {
      money = money + 1000;
      lcd.clear();
      lcd.print(money);
     }
    lastButton_state5 = currentButton_state5; // 버튼 상태 갱신
   }


  //콜라
  if (lastButton_state2 != currentButton_state2 )
  {
    if (lastButton_state2 == HIGH && currentButton_state2 == LOW)
    {
      if (money > 600)
      {
        
        Serial.println("1");    //서버에 "1" 전송
        lcd.clear();
        money -= 600;           //금액 감소
        lcd.print(money);
        
        //모터 회전
        servo1.write(179);
        delay(1000);
        servo1.write(0);
      }
     }
    lastButton_state2 = currentButton_state2; // 버튼 상태 갱신
   }

  //치킨
  if (lastButton_state3 != currentButton_state3 )
  {
    if (lastButton_state3 == HIGH && currentButton_state3 == LOW)
    {
      if (money > 500)
      {
        Serial.println("2");
        lcd.clear();
        money -= 500;
        lcd.print(money);
        servo2.write(179);
        delay(1000);
        servo2.write(0);
      }

   }
   lastButton_state3 = currentButton_state3; // 버튼 상태 갱신
  }

}

boolean debounce_sw(boolean last, int button) // 사용자 정의 함수
{
  boolean current = digitalRead(button); // 입력 값을 감지(샘플링)
  if (last != current) // 상태 변경 감지
  {
    delay(debounce_time); // 신호가 안정될 때 까지 지연시킴
    current = digitalRead(button); // 신호 안정 후 읽은 값
  }
  return current; // 디바운스를 거친 입력 값
}
