#include<stdio.h> 

/*
버블정렬 : 가까이 있는 두 숫자끼리 비교해 당장 더 작은 숫자를 앞으로 보내주는 것 
1 10 5 8 7 6 4 3 2 9 
1,10
  10,5 => 5, 10
  	
*/
int main(void){
	int i, j, temp;
	int array[10] = {1,10,5,8,7,6,4,3,2,9};
	for(i=0;i<10;i++){//시작하는 자리 
		for(j=0; j<9-i; j++){
		
			if(array[j]>array[j+1]){//j[0] j[1]
				temp = array[j];
				array[j] = array[j+1];
				array[j+1] = temp;
			} 
		}
	}
	for(i=0;i<10;i++){
		printf("%d ", array[i]);
	}
	return 0;
}
/*

*/

