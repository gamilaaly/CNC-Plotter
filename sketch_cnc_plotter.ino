#include <AFMotor.h>  // Adafruit Motor Shield library - Version: Latest 
#include <Servo.h>    // Servo
#include <SoftwareSerial.h>   // Bluetooth


/*************************************** Stepper ****************************************************/



int const X_MOTOR_PORTNUM = 2;    // Y-axis Stepper Port number
int const Y_MOTOR_PORTNUM = 1;    // X-axis Stepper Port number

int const NUM_STEPS_PER_REV = 48;   // Number of steps per stepper revolution

AF_Stepper x_stepper(NUM_STEPS_PER_REV, X_MOTOR_PORTNUM);   // X-axis Stepper Motor object
AF_Stepper y_stepper(NUM_STEPS_PER_REV, Y_MOTOR_PORTNUM);   // Y-axis Stepper Motor object

int const X_MOTOR_STEPS_PER_MM = 100;   // Calculated through trial and error
int const Y_MOTOR_STEPS_PER_MM = 100;   // Calculated through trial and error

int const X_MIN = 0;    // Minimum horizontal displacement
int const X_MAX = 260;    // Maximum horizontal displacement
int const Y_MIN = 0;    // Minimum vertical displacement
int const Y_MAX = 2;    // Maximum vertical displacement

int const SPEED = 2000;

int const NUM_OF_STEPS = 1;

/****************************************************************************************************/



/*************************************** Servo ****************************************************/

Servo pen_servo;   // Servo object
const int SERVO_PIN = 10;
int pos = 180;
const int SERVO_DELAY = 50;


/****************************************************************************************************/


/*************************************** Bluetooth ****************************************************/


const int rxPin = 0;  
const int txPin = 1;

SoftwareSerial bluetooth(rxPin, txPin);

String incomingMsg;


bool isReady;





/****************************************************************************************************/




/*************************************** Control ****************************************************/

bool ON = false;    // Power Flag
bool isLifted = true;   // Pen lifted flag

int const X_DEFAULT = 0;    // Default horizontal displacement
int const Y_DEFAULT = 0;    // Default vertical displacement

char shape;   // Shape Flag
int parameters[4];    // Parameters array

int current_x = 0;    // Current horizontal displacement
int current_y = 0;    // Current vertical displacement

/****************************************************************************************************/




void getParameters(String msg, char separator){
  char tmp1, tmp2, tmp3;
  int k = 0;
  for (int i = 0 ; i < msg.length() ; i++){
    if(msg[i] == separator){
      tmp1 = msg[i+1];
      tmp2 = msg[i+2];
      tmp3 = msg[i+3];
      char temp[3];
      temp[0] = tmp1;
      temp[1] = tmp2;
      temp[2] = tmp3;
      Serial.println(temp);
      parameters[k++] = atoi(temp);
    }
  }
}


/*****************************************/

void operate_plotter(){
  move_to(X_DEFAULT, Y_DEFAULT);
  switch(shape){
    case 'L':
      Serial.println("Drawing Line!");
      draw_line(parameters[0], parameters[1], parameters[2], parameters[3]);
      break;
    case 'R':
      Serial.println("Drawing Rectangle!");
      draw_rectangle(parameters[0], parameters[1], parameters[2], parameters[3]);
      break;
    case 'C':
      Serial.println("Drawing Circle");
      draw_circle(parameters[0], parameters[1], parameters[2]);
      break;
  }
}
/*****************************************/


/* 
  This function is responsible for populating our control instructions through bluetooth
  This 
*/

void receive_order(){
    if(bluetooth.available()){  
      incomingMsg = Serial.readString();
      Serial.println(incomingMsg);
      shape = incomingMsg[1];
      getParameters(incomingMsg, ',');
      
      isReady = true;
    
      Serial.print(shape);;
      Serial.print(" | ");
      Serial.print(parameters[0]);
      Serial.print(" | ");
      Serial.print(parameters[1]);
      Serial.print(" | ");
      Serial.print(parameters[2]);
      Serial.print(" | ");
      Serial.println(parameters[3]);
      }     
   delay(1); 
}

/*****************************************/

void draw_line(int x1, int y1, int x2, int y2){
  Serial.println("In draw_line");
  move_to(x1, y1);
  lower_pen();
  move_to(x2,y2);
}


void draw_rectangle(int x1, int y1, int height, int width){
  Serial.println("In draw_rectangle");
  draw_line(x1, y1, x1+width, y1);
  draw_line(x1+width, y1, x1+width, y1+height);
  draw_line(x1+width, y1+height, x1, y1+height);
  draw_line(x1, y1+height, x1, y1);
}

void draw_circle(int x1, int y1, int r){
  Serial.println("In draw_circle");
  move_to(x1, y1+r);
  for(int t = 0; t < 360; t++){
    int y = r*sin(t) + y1;
    int x = r*cos(t) +x1;
    move_towards(x,y);
  }
}

/*****************************************/

void move_in_x(int direction){
  current_x = current_x + direction;
  
  if (direction == 1){
    Serial.print("Current location: ( ");
    Serial.print(current_x);
    Serial.print(" , ");
    Serial.print(current_y);
    Serial.println(" )");
    x_stepper.step(NUM_OF_STEPS, FORWARD, SINGLE);
  } else if (direction == -1){
    Serial.print("Current location: ( ");
    Serial.print(current_x);
    Serial.print(" , ");
    Serial.print(current_y);
    Serial.println(" )");
    x_stepper.step(NUM_OF_STEPS, BACKWARD, SINGLE);
  }
}

void move_in_y(int direction){
  current_y = current_y + direction;
  
  if (direction == 1){
    Serial.print("Current location: ( ");
    Serial.print(current_x);
    Serial.print(" , ");
    Serial.print(current_y);
    Serial.println(" )");
    y_stepper.step(NUM_OF_STEPS,FORWARD, SINGLE);
  } else if (direction == -1){
    Serial.print("Current location: ( ");
    Serial.print(current_x);
    Serial.print(" , ");
    Serial.print(current_y);
    Serial.println(" )");
    y_stepper.step(NUM_OF_STEPS,BACKWARD, SINGLE);
  }
}

void move_towards(int x, int y){
    if(current_x > x){
      move_in_x(-1);
    }
    else if(current_x < x){
      move_in_x(1);
    }
        
    if (current_y > y){
      move_in_y(-1);
    }
    else if (current_y < y){
      move_in_y(1);
    }
}

void move_to(int x, int y){
  while(current_x != x || current_y != y){
    move_towards(x,y);
  }
}


/*****************************************/
void reset(){
  /* Lift the pen with the servo
   return the base stand to its original location
   return the pen stand to its original location */
  lift_pen();
// move_to(X_DEFAULT, Y_DEFAULT);
  x_stepper.release();
  y_stepper.release();
  isReady = false;
}

void lower_pen(){
  if(isLifted){
    /* Servo Motor call */
    pen_servo.write(-1*pos);
    delay(SERVO_DELAY);
    isLifted = false;
  }
}

void lift_pen(){
  if(!isLifted){
    /* Servo Motor call */
    pen_servo.write(pos);
    delay(SERVO_DELAY);
    isLifted = true;
  }
}



// 1 step = 0.017 mm 

void setup() {
  Serial.begin(9600);   // initialize serial communication:
  Serial.println("Serial ready");  
  
  /** Bluetooth **/
  bluetooth.begin(9600);
  bluetooth.println("Bluetooth ready");
  
  
  /** Stepper **/
  x_stepper.setSpeed(SPEED);
  y_stepper.setSpeed(SPEED);
  
  isReady = false;
  
  
  /** Servo **/
  pen_servo.attach(SERVO_PIN);
  
}

void loop() {
  if(!isReady){
    receive_order();
  }
  else if(isReady){
    Serial.println("Operating now!");
    operate_plotter();
    reset();
  }
  
 
  

}

