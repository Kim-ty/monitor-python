#include "Keyboard.h"
#include "Mouse.h"

char cmd;
//키 ascii매칭
int selectKeyboard(char key) {
  switch (key) {
    case '!': return 0xC2;
    case '@': return 0xC3;
    case '#': return 0xC4;
    case '$': return 0xC5;
    case '%': return 0xC6;
    case '^': return 49;
    case '&': return 50;
    case '*': return 51;
    case '(': return 40;
    case '~': return 126;
    default: return 0;
  }
}


//단순 키 매칭
void keyboardWrite(int key) {
  Keyboard.press(key);
  delay(5);
  Keyboard.releaseAll();
  Serial.println((String)">>|key");
  Serial.println((String) "keyboard press : " + key);
  delay(2);
}

//마법 특수키 매칭
void keyboardUsemagic(int key) {

  Keyboard.press(KEY_LEFT_CTRL);
  delay(5);
  Keyboard.press(key);
  Keyboard.release(key);
  delay(100);
  Keyboard.press(key);
  Keyboard.release(key);
  delay(100);
  Keyboard.press(key);
  Keyboard.releaseAll();
  Serial.println((String)">>|magic");
  Serial.println((String) "keyboard press : ctrl + " + key);
  delay(2);
}

void mouseMove(long x, long y) {
  
  // int x_move = abs(x/25);
  // int y_move = abs(y/25);
  // int r_x = 0;
  // int r_y = 0;
  // int r_loop = 0;
  // int l_data = 0;
  // int isNegX = (0>x)?-1:1;
  // int isNegY = (0>y)?-1:1;
  // int x_move_s = isNegX*25;
  // int y_move_s = isNegY*25;


  // if(x_move > y_move){
  //   r_x = 1;
  //   r_loop = x_move - y_move;
  //   l_data = y_move;
  // }else{
  //   r_y = 1;
  //   r_loop = y_move - x_move;
  //   l_data = x_move;
  // }

  // for(int i=0;i<l_data;i++){
  //   Mouse.move(x_move_s,y_move_s,0);
  //   delay(1);
  // }

  // for(int i=0;i<r_loop;i++){
  //   Mouse.move(x_move_s*r_x,y_move_s*r_y,0);
  //   delay(1);
  // }

  // Mouse.move(x%25,y%25,0);
  Mouse.move(x,y,0);
  delay(1);
  Serial.println((String) "mouse move : ["+ x + ","+y+"]");
  Serial.println((String)">>|move");
}

void mouseClick() {

  Mouse.click(MOUSE_LEFT);
  Serial.println((String) "mouse left click");
  Serial.println((String)">>|click");
}

void setup() {
  Keyboard.begin();
  Mouse.begin();
  // MouseTO.setCorrectionFactor(1)
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {

  if (Serial.available()) {  
    cmd = Serial.read();
    int key = selectKeyboard(cmd);
    if (key == 49 || key == 50 || key == 51) {
      Serial.println((String)"<<|magic");
      keyboardUsemagic(key);
    } else if (key == 0xC2 || key == 0xC3 || key == 0xC4 || key == 0xC5 || key == 0xC6) {
      Serial.println((String)"<<|key");
      keyboardWrite(key);
    } else if(key == 40){
      Serial.println((String)"<<|click");
      mouseClick();
    }else if(key == 126){
      Serial.println((String)"<<|move");
      long value1 = Serial.parseInt();
      long value2 = Serial.parseInt();
      Serial.setTimeout(50);
      mouseMove(value1,value2);
    }
  }
}
