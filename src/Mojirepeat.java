
public class Mojirepeat {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(3|5);
		System.out.println(false && false);
		System.out.println(3^5);
		System.out.println("요것은 github 시험, test를 위한 것임");
		int num1 = 7, num2 = 7;
		int result1, result2;
		
		result1 = --num1 + 4;
		result2 = num2-- + 4;
		
		System.out.println("전위 감소 연산자에 의한 결과 : " + result1 + ", 변수의 값 : " + num1);
		System.out.println("후위 감소 연산자에 의한 결과 : " + result2 + ", 변수의 값 : " + num2);		
	}

}
