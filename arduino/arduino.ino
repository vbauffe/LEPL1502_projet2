// LEPL1502 - Projet 2
//
// Lecture du voltage grace a un Arduino Uno
//
// Vincent Bauffe, 2020

void setup()
{
  //  Permet de choisir la sortie (LED)
  pinMode(13, OUTPUT);
}

void loop()
{
  // Lit les differentes tensions
  int rouge = analogRead(A0);
  // Attends dans le cas ou le tag est trop eloigne
  delay(500);
  int verte = analogRead(A1);
  
  if (verte > 350) {
    // Allume la LED 3s
    digitalWrite(13, HIGH);
    delay(3000);
    digitalWrite(13, LOW);
  } else if (rouge > 350) {
    // Allume la LED 1s
    digitalWrite(13, HIGH);
    delay(1000);
    digitalWrite(13, LOW);
  }
  
  // Attends une seconde avant de recommencer
  delay(1000);
 
}