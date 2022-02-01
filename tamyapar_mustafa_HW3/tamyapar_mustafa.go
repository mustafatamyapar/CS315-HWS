package main
import "fmt"

//Pass by value
func PassbyValue(y int) {
	fmt.Printf("Inside PassbyValue Function\n")
	y = 10
	fmt.Printf("test1 : %d\n", y)
}

// Pass By Reference
func PassbyRefernce(y *int) {
	fmt.Printf("Inside PassbyReference Function\n")
	*y = 10
	fmt.Printf("test2 : %d\n", *y)
}

//Passing parameters using another function as argument
func print(f func(int, int) int, a, b int) {
	fmt.Println(f(a, b))
}

func mult(a, b int) int {
	return a * b
}

//Struct example
type Grades struct {
	L int
	M int
}

func Calculate(in Grades) int {
	return in.L/10 + in.M*9/10
}

//Closure example
func Closure() func() int {
	num := 5
	return func() int {
		num = num * 5
		return num
	}
}


func main() {

//Nested Subprogram Definitions
//In Go language nested subprograms calls the inner program inside this function as shown in the first example.
//In the second example, as function being inside the main function, the outer function calls inner function using its argument.

funcOuter := func() {
	fmt.Println("Outer Function")
	funcInner := func() {
		fmt.Println("Inner Function")
	}
	funcInner()
}
funcOuter()

func(str string) {
	fmt.Println("The best cookie is", str)
}("Lotus")

funcNested := func(str string) {
	fmt.Println("No", str, "is the best cookie.")
} //funcNested calls func function using its input.

funcNested("Tutku")

//Scope of Local Variables
//In go language scope of local variables is the function or block they defined. They are 
//not accessible from outside of the function.Local variables can be accessed in nested loops 
//if the variable is declared in the outer loop.
var age int = 35

fmt.Printf("my age is : %d\n", age) //In the scope of main function

funcOut:=func(str string) {
	var myName string = " Mustafa"//In the scope of the funcOut
	fmt.Println(str, myName)
}
funcOut("Hello")

{
	var sc string = " In the block"//In the scope of the block
	fmt.Println(sc)
}
for a := 0; a < 3; a++ {
	var access string = "access"
	for b := 0; b < 2; b++ {
		fmt.Printf(access)//Nested for loop can access to the string which declared in the outer loop
		fmt.Printf("%d\n", b)
	}
	fmt.Printf("value of a: %d\n", a)
}

//Parameter Passing Methods
//Go supports two kinds of parameter passing. Pass by value and pass by reference. 
//Also in go we can pass parameters by calling a function inside the argument of the other function.
//The functions PassbyValue and PassbyReference are declared at the top of the program outside the main function.

var test1 int = 0
var test2 int = 0
fmt.Printf("test1: %d, test2: %d\n", test1, test2) // 0 0

// Pass by Value
PassbyValue(test1)

// Pass by Refernce
PassbyRefernce(&test2)

fmt.Printf("After the function calls")
fmt.Printf("test1: %d, test2: %d\n", test1, test2) // 0 10


//Using another function for parameter passing
print(mult, 2, 4) //mult function passes parameters to the function which prints 


//Keyword and Default Parameters
//In Go language keyword parameters are not supported as a design choice. But to get away from that struct is used as a parameter.
//Go also does not support default parameters as a design choice.  Also to get away from that struct is used.
c := Calculate(Grades{L: 100, M: 30})
	fmt.Printf("Struct example : %d\n", c)
	

//Closures
//In Golang closures are a type of an anonymous function that references variables declared outside of the function. 
//As Golang is a language which allows nested subprograms, closures are useful.

OrderFive := Closure()//Accesses Closure Function and the variable

fmt.Println(OrderFive()) //25
fmt.Println(OrderFive()) //125
fmt.Println(OrderFive()) //625

}
