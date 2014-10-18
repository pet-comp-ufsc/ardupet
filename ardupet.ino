char incomingByte = 0;

const char lampCount = 4;
const unsigned short doorUnlockTime = 2000; // in miliseconds

bool lampStatus[lampCount];
bool doorStatus;
unsigned short doorUnlockTimer;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  
  for (int i = 0; i < lampCount; ++i)
    lampStatus[i] = false;
  doorStatus = false;
}

void loop() {
  if (Serial.available() > 2) {
    // Option can be 'r' (read) or 'w' (write)
    incomingByte = Serial.read();
    
    if (incomingByte == 'r') {  
      // Option can be 'l' (lamp) or 'd' (door)
      incomingByte = Serial.read();
      
      if (incomingByte == 'l') {
        // Option can be 0 to (lampCount-1) (lamp id)
        incomingByte = Serial.read();
        
        if (incomingByte < lampCount)
          Serial.write(lampStatus[incomingByte]);
      } else if (incomingByte == 'd') {
        // Discard last byte, since door does not have id and last byte has to be consumed
        Serial.read();
        
        Serial.write(doorStatus);
      }
    } else if (incomingByte == 'w') {
      // Option can be 'l' (lamp) or 'd' (door)
      incomingByte = Serial.read();
      
      if (incomingByte == 'l') {
        // Option can be 0 to (lampCount-1) (lamp id)
        incomingByte = Serial.read();
        
        if (incomingByte < lampCount) {
           // TODO: Logic to invert lamp status
          
          lampStatus[incomingByte] = !lampStatus[incomingByte];
        }
      } else if (incomingByte == 'd') {
        // Discard last byte, since door does not have id and last byte has to be consumed
        Serial.read();
        
        // TODO: Logic to unlock the door
        
        doorStatus = true;
        doorUnlockTimer = doorUnlockTime;
      }
    }
  }
  
  if (doorUnlockTimer > 0) {
    digitalWrite(13, HIGH);
    --doorUnlockTimer;
  } else {
     // TODO: Logic to lock the door?
    
    digitalWrite(13, LOW);
    doorStatus = false;
  }
  
  // Delay to make board timing predictable
  delay(1);
}
