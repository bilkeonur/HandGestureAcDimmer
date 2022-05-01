#define ZERO_CROSS_PIN 2
#define DIM_PIN 9

int dimLevel=120;

void zeroCrossInterrupt()
{ 
  delayMicroseconds(dimLevel*75);
  digitalWrite(DIM_PIN, LOW); //Turn On Triac
  delayMicroseconds(10);
  digitalWrite(DIM_PIN, HIGH); //Turn Off Triac
}

void setup() 
{
  pinMode(DIM_PIN, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  
  digitalWrite(DIM_PIN, HIGH); //Turn Off Triac

  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  
  attachInterrupt(digitalPinToInterrupt(ZERO_CROSS_PIN), zeroCrossInterrupt, RISING);
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available() > 0)
  {
    int recData = Serial.read();
    dimLevel = recData;
    Serial.println((char)recData);
  }
}
