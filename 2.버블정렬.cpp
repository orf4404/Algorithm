#include<stdio.h> 

/*
�������� : ������ �ִ� �� ���ڳ��� ���� ���� �� ���� ���ڸ� ������ �����ִ� �� 
1 10 5 8 7 6 4 3 2 9 
1,10
  10,5 => 5, 10
  	
*/
int main(void){
	int i, j, temp;
	int array[10] = {1,10,5,8,7,6,4,3,2,9};
	for(i=0;i<10;i++){//�����ϴ� �ڸ� 
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

