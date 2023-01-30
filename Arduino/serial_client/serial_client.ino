const byte ledPin = 13;
static char message[2];


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledPin,OUTPUT);
  message[1] = '\0';

}

void loop() {
  // put your main code here, to run repeatedly:
  if( Serial.available())
  {
    char inByte = Serial.read();
    if( inByte != '\n')
    {
      message[0] = inByte;
    }
    int show_bit = atoi(message) >= 1 ? HIGH:LOW;
    digitalWrite(ledPin,show_bit); 
  }

}
