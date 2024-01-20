
char Colors[] = {'O', 'R', 'B', 'G', 'Y', 'P', 'A', 'W'};
char finallights[4];
char light_sequence[10][4];
int n_sequences;
int binary_light_sequence[10][12];
int final_binary_light[12];
int esquerda = 0;
int direita = 0;


int billys(){

  // esta função existe em homenagem ao billy k esteve em call enquanto eu estava a acabar o projeto, contudo o codigo não funciona sem a função e não tenho a certeza do porque
  
  return millis();
  
}




// 0 é ligado e 1 é desligado



void make_binary_light_sequence() {
  
  //"traduz" a sequencia de cores de um grupo de letras para um grupo de 0 e 1.

  for (int j = 0; j < n_sequences - 1; ++j) {
    
  	for (int i = 0; i < 4; ++i){
   
    	if (light_sequence[j][i] == 'O') {
      		binary_light_sequence[j][3*i] = 1;
      		binary_light_sequence[j][3*i + 1] = 1;
      		binary_light_sequence[j][3*i + 2] = 1;
    	}
    
   	 	else if (light_sequence[j][i] == 'B') {
     	 	binary_light_sequence[j][3*i] = 1;
      		binary_light_sequence[j][3*i + 1] = 0;
      		binary_light_sequence[j][3*i + 2] = 1;
      
    	}
    
    	else if (light_sequence[j][i] == 'R') {
      		binary_light_sequence[j][3*i] = 0;
      		binary_light_sequence[j][3*i + 1] = 1;
      		binary_light_sequence[j][3*i + 2] = 1;
      
    	}
    
    	else if (light_sequence[j][i] == 'G') {
      		binary_light_sequence[j][3*i] = 1;
      		binary_light_sequence[j][3*i + 1] = 1;
      		binary_light_sequence[j][3*i + 2] = 0;
      
    	}
    
    	else if (light_sequence[j][i] == 'Y') {
      		binary_light_sequence[j][3*i] = 0;
      		binary_light_sequence[j][3*i + 1] = 1;
      		binary_light_sequence[j][3*i + 2] = 0;
      
    	}
    
    	else if (light_sequence[j][i] == 'P') {
      		binary_light_sequence[j][3*i] = 0;
      		binary_light_sequence[j][3*i + 1] = 0;
      		binary_light_sequence[j][3*i + 2] = 1;
    	}
    
    	else if (light_sequence[j][i] == 'A') {
      		binary_light_sequence[j][3*i] = 1;
      		binary_light_sequence[j][3*i + 1] = 0;
      		binary_light_sequence[j][3*i + 2] = 0;
    	}
    
    	else if (light_sequence[j][i] == 'W') {
     		binary_light_sequence[j][3*i] = 0;
      		binary_light_sequence[j][3*i + 1] = 0;
      		binary_light_sequence[j][3*i + 2] = 0;
    	}
    
  	}
    
  }
  
}

void make_final_binary_lights() {
  
//"traduz" a sequencia de cores de um grupo de letras para um grupo de 0 e 1, so que da ultima sequencia de cores

  for (int i = 0; i < 4; ++i){
   
    if (finallights[i] == 'O') {
      	final_binary_light[3*i] = 1;
      	final_binary_light[3*i + 1] = 1;
      	final_binary_light[3*i + 2] = 1;
    }
    
   	 else if (finallights[i] == 'B') {
  	 	final_binary_light[3*i] = 1;
      	final_binary_light[3*i + 1] = 0;
      	final_binary_light[3*i + 2] = 1;
      
    }
    
    else if (finallights[i] == 'R') {
      	final_binary_light[3*i] = 0;
      	final_binary_light[3*i + 1] = 1;
      	final_binary_light[3*i + 2] = 1;
      
    }
    
    else if (finallights[i] == 'G') {
      	final_binary_light[3*i] = 1;
      	final_binary_light[3*i + 1] = 1;
      	final_binary_light[3*i + 2] = 0;
      
    }
    
    else if (finallights[i] == 'Y') {
      	final_binary_light[3*i] = 0;
      	final_binary_light[3*i + 1] = 1;
      	final_binary_light[3*i + 2] = 0;
      
    }
    
    else if (finallights[i] == 'P') {
      	final_binary_light[3*i] = 0;
      	final_binary_light[3*i + 1] = 0;
      	final_binary_light[3*i + 2] = 1;
    }
    
    else if (finallights[i] == 'A') {
      	final_binary_light[3*i] = 1;
      	final_binary_light[3*i + 1] = 0;
      	final_binary_light[3*i + 2] = 0;
    }
   
    else if (finallights[i] == 'W') {
     	final_binary_light[3*i] = 0;
      	final_binary_light[3*i + 1] = 0;
      	final_binary_light[3*i + 2] = 0;
    }
    
  }
    
}
  




int Weighted_List_Selection_int(int elements[], int weights[], int size) {

//Escolhe um elemento "aleatorio" de uma lista, favorecendo mais certos elementos do que outros

    int Total_Weight = 100;
    int Random_Number = random(Total_Weight);
    int Cumulative_Weight = 0;

    for (int i = 0; i < size; ++i) {
        Cumulative_Weight += weights[i];
        if (Random_Number < Cumulative_Weight) {
            return i;
        }
    }

    return -1;
}




void generateRandomSequence(int n_sequence) {

//Gera uma sequencia aleatoria de cores, considerando que o "O" ou luz desligada , se pode repetir, enquanto que as outras cores não

    for (int i = 0; i < n_sequence - 1; ++i) {
        char lights[4];

        for (int j = 0; j < 4; ++j) {
            int randomIndex = random(8);
            char randomColor = Colors[randomIndex];

            bool colorExists = false;

            if (randomColor != 'O') {
                for (int k = 0; k < j; ++k) {
                    if (lights[k] == randomColor) {
                        colorExists = true;
                        break;
                    }
                }
            }

            if (!colorExists) {
                lights[j] = randomColor;
            } else {
                j -= 1;
            }
        }

        for (int j = 0; j < 4; ++j) {
            light_sequence[i][j] = lights[j];
        }
    }
}

void generatelastlights() {

//Gera a ultima sequencia de cores

    int randomIndex = random(1, 8);
    char Color = Colors[randomIndex];
    int finalcolorposition1 = random(4);
    int finalcolorposition2;

    do {
        finalcolorposition2 = random(4);
    } while (finalcolorposition1 == finalcolorposition2);

    int positionsToRemove[2] = {finalcolorposition1, finalcolorposition2};
    int count = 0;

    for (int i = 0; i < 4; ++i) {
        bool isToRemove = false;

        for (int j = 0; j < 2; ++j) {
            if (i == positionsToRemove[j]) {
                isToRemove = true;
                break;
            }
        }

        if (!isToRemove) {
            finallights[i] = Color;
        } else {
            finallights[i] = Colors[random(8)];
        }
    }
}


void setup() {

  // Setup dos pinos 
  
  Serial.begin(9600);
  randomSeed(analogRead(0));
  pinMode(13, OUTPUT); 
  pinMode(12, OUTPUT); 
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(A0, INPUT); 
  pinMode(A1, INPUT);
  pinMode(A2, OUTPUT);
  pinMode(A3, OUTPUT);
  
}

void loop() {
  

  //lista com o numero possivel de sequencias que cada jogo pode ter
  int p_n_sequences[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
  
  //lista que faz com que certos numeros de sequencias sejam mais provaveis que outros
  int n_sequence_weights[] = {2, 5, 18, 25, 25, 16, 7, 2, 1};

  int Index_1 = Weighted_List_Selection_int(p_n_sequences, n_sequence_weights, 9);

  n_sequences = p_n_sequences[Index_1];

  //numero de segundos que cada luz ta ligada

  float* seconds_sequence = new float[n_sequences];

  for (int i = 0; i < n_sequences; ++i) {
    float randomFloat = map(random(0, 1000), 0, 1000, 400, 1200) / 1000.0;
    seconds_sequence[i] = randomFloat;
  }
      

  generateRandomSequence(n_sequences);

  generatelastlights();
      
  make_binary_light_sequence();
      
	make_final_binary_lights();
      
  int winner = 2;
  digitalWrite(A2, 0);
  digitalWrite(A3, 0);
    
          
          
          
          
  // COMEÇO DAS CENAS INTERATIVAS

  for (int i = 0; i < n_sequences - 1; ++i) {

    //Em cada ciclo muda as cores dos LED para as cores de cada sequencia, excepto a ultima
       
		int start_time = billys();
    digitalWrite(13, binary_light_sequence[i][0]);
    digitalWrite(12, binary_light_sequence[i][1]);
    digitalWrite(11, binary_light_sequence[i][2]);
    digitalWrite(10, binary_light_sequence[i][3]);
    digitalWrite(9, binary_light_sequence[i][4]);
    digitalWrite(8, binary_light_sequence[i][5]);
    digitalWrite(7, binary_light_sequence[i][6]);
    digitalWrite(6, binary_light_sequence[i][7]);
    digitalWrite(5, binary_light_sequence[i][8]);
    digitalWrite(4, binary_light_sequence[i][9]);
    digitalWrite(3, binary_light_sequence[i][10]);
    digitalWrite(2, binary_light_sequence[i][11]);
        

    while (billys() - start_time < seconds_sequence[i] * 1000){

      // Espera que o tempo da sequencia acabe, vendo se alguem clica no botão, sendo que se alguem clicar o oponente ganha

      int buttonA0 = digitalRead(A0); 
  		int buttonA1 = digitalRead(A1); 
    
  		if (buttonA0 == HIGH) {
      
				winner = 1;
      	Serial.println("Button 1 Pressed");
				break;
  		}

  		else if (buttonA1 == HIGH) {
      
      	winner = 0;      
      	Serial.println("Button 2 Pressed");
				break;
  		}
    }
    if (winner == 1 || winner == 0) {
      break;
    }
  }
      
  if (winner != 0 && winner != 1){

    //Muda as cores dos LED para as cores da ultima sequencia
        
    digitalWrite(13, final_binary_light[0]);
    digitalWrite(12, final_binary_light[1]);
    digitalWrite(11, final_binary_light[2]);
    digitalWrite(10, final_binary_light[3]);
    digitalWrite(9, final_binary_light[4]);
    digitalWrite(8, final_binary_light[5]);
    digitalWrite(7, final_binary_light[6]);
    digitalWrite(6, final_binary_light[7]);
    digitalWrite(5, final_binary_light[8]);
    digitalWrite(4, final_binary_light[9]);
    digitalWrite(3, final_binary_light[10]);
    digitalWrite(2, final_binary_light[11]);
        
    while (winner != 0 && winner != 1){

      //Fica neste cicli infinitamente ate que um jogador clique no butão e assim ganhe o jogo

      int buttonA0 = digitalRead(A0); 
  		int buttonA1 = digitalRead(A1); 
    
  		if (buttonA0 == HIGH) {
      
				winner = 0;
      	Serial.println("Button 1 Pressed");
				break;
  		}

  		else if (buttonA1 == HIGH) {

      	winner = 1;      
      	Serial.println("Button 2 Pressed");
				break;
  		}
    }
  }

      
  if (winner == 1){

    //Acende a luz do jogador 2, porque este ganhou e adiciona um ponto à contagem de vitorias desse jogador
        
    digitalWrite(A3, 1);
    direita += 1;

          
  }
      
  else if (winner == 0){

    //Acende a luz do jogador 1, porque este ganhou e adiciona um ponto à contagem de vitorias desse jogador
  
        
    digitalWrite(A2, 1);
    esquerda += 1;
          
  }
        
  Serial.print("esquerda");
  Serial.println(esquerda);
  Serial.print("direita");  
  Serial.println(direita);


  //Espera 5 segundos antes de começar o proximo jogo
  delay(5000);
      
          
          
       
      
  delete[] seconds_sequence;
	
      
}
