void setup() {
  // put your setup code here, to run once:
pinMode(3,OUTPUT);           //Sends the values out for the LED
pinMode(5,INPUT);            //takes the values in for the switch
Serial.begin(9600);          //starts the serial monitor
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorvalue=digitalRead(5);        //sets the sensorvalue variable
if(sensorvalue == HIGH){                 //checks if the Switch is on
digitalWrite(3,HIGH);                    //if the switch is on it turns on the LED
}
else{
  digitalWrite(3,LOW);                    //if the switch is off it turns the off the LED
}
Serial.println(sensorvalue);              //displays the values on the serial monitor
}
