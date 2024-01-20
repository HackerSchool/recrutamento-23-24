
/* Define constants for timing and pin assignments */
#define smalltime 150
#define looptime 500
#define longtime 750


const int redled = 6;
const int yellowled = 7;
const int blueled = 8;
const int greenled = 9;

const int redbutton = 10;
const int yellowbutton = 11;
const int bluebutton = 12;
const int greenbutton = 13;

const int buzzer = 4;

/* Arrays to store button statuses, buzzer tones, and user/right sequences */
int button_status[] = {HIGH, HIGH, HIGH, HIGH};
int buzzer_tones[] = {262, 294, 330, 350};
int userseq[15];
int rightseq[15];

void singlelight(int pin, int freq[], int time);
void all_lights(int freq[], int time);
void loselights(int freq[], int time);

/* Setup function to initialize pin modes and seed for random number generation */
void setup() {

  randomSeed(analogRead(0));

  pinMode(redled, OUTPUT);
  pinMode(yellowled, OUTPUT);
  pinMode(blueled, OUTPUT);
  pinMode(greenled, OUTPUT);

  pinMode(redbutton, INPUT_PULLUP);
  pinMode(yellowbutton, INPUT_PULLUP);
  pinMode(bluebutton, INPUT_PULLUP);
  pinMode(greenbutton, INPUT_PULLUP);

  pinMode(buzzer, OUTPUT);

}



void loop() {
    // Generate a random sequence for the right LED pattern
    for(int i = 0; i < 15; i++){
        rightseq[i] = random(0, 100);
        if(rightseq[i]%4 == 0){
          rightseq[i] = 0;
        } else if(rightseq[i]%4 == 1){
          rightseq[i] = 1;
        } else if(rightseq[i]%4 == 2){
          rightseq[i] = 2;
        } else if(rightseq[i]%4 == 3){
          rightseq[i] = 3;
        }
    }

    int j = 0;
    int roundsnum = 1;
    int is_right = 0;
    int currentled = 0;
    int status_sum = 0;

    // Display initial lights and sound
    singlelight(redled, buzzer_tones, smalltime);
    singlelight(yellowled, buzzer_tones, smalltime);
    singlelight(blueled, buzzer_tones, smalltime);
    singlelight(greenled, buzzer_tones, smalltime);

    all_lights(buzzer_tones, longtime);

    // Main game loop
    while(1){
        // Display the sequence of lights
        for(j = 0; j < roundsnum; j++){
          currentled = rightseq[j];
          if(currentled == 0){

            singlelight(redled, buzzer_tones, looptime);

          } else if(currentled == 1){

            singlelight(yellowled, buzzer_tones, looptime);

          } else if(currentled == 2){
              
            singlelight(blueled, buzzer_tones, looptime);

          } else if(currentled == 3){

            singlelight(greenled, buzzer_tones, looptime);

          }
        }

        delay(longtime);

        // Get user input and compare with the right sequence
        for(j = 0; j < roundsnum; j++){

            while(1){
              // Read button statuses
              button_status[0] = digitalRead(redbutton);
              button_status[1] = digitalRead(yellowbutton);
              button_status[2] = digitalRead(bluebutton);
              button_status[3] = digitalRead(greenbutton);

              status_sum = 0;

              // Check for pressed buttons
              for(int i = 0; i < 4; i++){
                  if(button_status[i] == LOW){
                      singlelight(i+6, buzzer_tones, looptime);
                      status_sum++;
                  }
              }

              if(status_sum == 1) break;
            }

            // Record user input and check correctness
            for(int i = 0; i < 4; i++){

                if(button_status[i] == LOW){
                    userseq[j] = i;

                if(userseq[j] == rightseq[j]){
                    is_right = 1;
                } else {
                    is_right = 0;
                    break;
                }
                }
            }
            if(is_right == 0) break;
        }

        // Check game status and update rounds
        if(is_right == 1 && roundsnum < 15){
          roundsnum += 1;
          delay(longtime);
        } else if(is_right == 1 && roundsnum == 15){
          // Player won the game
          for(int i = 0; i < 3; i++){
            all_lights(buzzer_tones, smalltime);
          }

          delay(2000);
          break;
        } else if (is_right == 0){
          // Player lost the game
          for(int i = 0; i < 3; i++){
            loselights(buzzer_tones, smalltime);
          }

          delay(2000);
          break;
        }

    }
}

/* Function to display a single LED light with sound */
void singlelight(int pin, int freq[], int time){
    digitalWrite(pin, HIGH);
    tone(buzzer, freq[pin-6], time);
    delay(time);
    digitalWrite(pin, LOW);
    delay(time);

    return;
}

/* Function to display all LED lights with sound */
void all_lights(int freq[], int time){
    digitalWrite(redled, HIGH);
    digitalWrite(yellowled, HIGH);
    digitalWrite(blueled, HIGH);
    digitalWrite(greenled, HIGH);

    tone(buzzer, freq[redled-6], time);
    tone(buzzer, freq[yellowled-6], time);
    tone(buzzer, freq[blueled-6], time);
    tone(buzzer, freq[greenled-6], time);
    
    delay(time);

    digitalWrite(redled, LOW);
    digitalWrite(yellowled, LOW);
    digitalWrite(blueled, LOW);
    digitalWrite(greenled, LOW);
    delay(time);


  return;
}

/* Function to display losing lights and sound */
void loselights(int freq[], int time){

  digitalWrite(redled, HIGH);
  digitalWrite(blueled, HIGH);
  tone(buzzer, freq[redled-6], time);
  tone(buzzer, freq[blueled-6], time);

  delay(time);

  digitalWrite(redled, LOW);
  digitalWrite(blueled, LOW);

  digitalWrite(yellowled, HIGH);
  digitalWrite(greenled, HIGH);
  tone(buzzer, freq[yellowled-6], time);
  tone(buzzer, freq[greenled-6], time);

  delay(time);

  digitalWrite(yellowled, LOW);
  digitalWrite(greenled, LOW);

  delay(time);

  return;
}
