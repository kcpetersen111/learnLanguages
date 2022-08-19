#include <stdio.h>
#include <string.h>
//how to create a struct
struct theStruct{
	int structNum;
	char string[100];
};

void addone(int* num){

	(*num)++;
}

int main() {
	//comment 
	int age = 69;
	const float decimal = 4.20;
	char letter = 'd';
	int b = letter == decimal && !(age == decimal);
	int numbers[] = {5,10,15,20};
	int emptyarray[5];

	char string[] = "yeah";

	printf("Hello world\n");
	/*more
	comments*/
	age++;
	printf("%d is a number\nand this is a string %s\n",age,string);

	if(age>decimal){
		printf("yes\n");
	} else if(age<decimal){
		printf("maybe\n");
	} else {
		printf("no\n");
	}

	//terinary operator 
	int ter = (10<9) ? 1:0;
	// condition^^	   ^^ true and then false values

	switch(ter){
		case 0:
			//exicute some code
			break;
		case 1:
			// more code
			break;
		default:
			//code that runs if there was not the a true statment
			age = 420;
	}
	int i = 0;
	while(i<10){
		//this code will run until the condition is true
		i++;
	}

	do{
		//a do while loop

	} while(0);

	for(int j = 0; j<5;j++){
		if(j==2){
			continue;
		}
		printf("%i",j);
	}
	
	//get user input
	int number;
	scanf("%d",&number);

	printf("%i",number);

	//scan a string
	char s[30];
	scanf("%s",s);	
	printf("%s",s);

	//refrencing and derefrencing pointers are the same in c as in every other programming languages

	int n = 0;
	printf("%i",n);
	addone(&n);
	printf("%i",n);

	struct theStruct st;

	strcpy(st.string,"the text to copy");
	st.structNum = 299;

	struct theStruct newStruct = { 23, "string"}; 
	
	return 0;
}
