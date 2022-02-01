import "dart:io";
void main() { 

  //1) How are the boolean values represented?
  //In Dart true and false are the only boolean representations.
    bool big; 
    big = 10 > 1; 
    print(big);
    bool nom;
    nom = ("a" == "b");
    print(nom);
  //2)What operators are short-circuited?
  //Short circuit operators are && , || in dart.
  var elm = 20;
  var and = (elm < 25 && elm > 10);
  print("elm < 25 && elm > 10");
  print(and);

  var elm2 = 10;
  var or = (elm2 > 5 || elm2 < 8);
  print("elm2 > 5 || elm2 < 8");
  print(or);
  bool func1() {
    return true;
  }
  bool func22(){
    return false;
  }
  bool func3(){
    print("func3 executed");
    return true;
  }
  bool func4(){
    print("func4 executed");
    return false;
  }
    if(func1() && func22())
  {
    print("Short Circuit");
  }

  if(func3() || func4()) //shows that func 4 is not executed.
  {
    print("Short Circuit 2 ");
  }
  //3)How are the results of short-circuited operators computed? (Consider also function calls)
  //In and operations, if first expression is true both expressions are checked, but if false does not checks other.
  // if both are true turns true else turns false but in or operation if the first expression 
  //is true second one is not checked and if one of them is true turns true.
  bool func()
    {
    print("in func");
    return true;
    }
  bool func2()
  {
    print("in func2");
    return false;
  } 

print(true && func()); // executing both
print(func() && func2()); //executing both
print(func2() && func()); //executing just func2
print(true || func2()); //not executes func2
print(func() || func2()); // just executes func
print(func2() || func()); //executing both

//4)What are the advantages about short-circuit evaluation?
//Programs will be computed faster due to not computing second expression in the or,and expression. Also as shown below
//if there would not be short circuit operation our program will crash due to exceeding array size . 
var arr1 = ["tamyapar","mustafa","efe"];
var i = 0;
var arrLen = 3;
var key = "mustafa";
while((i < arrLen) && (arr1[i] != key))
{
  i = i + 1;
}
//5)What are the potential problems about short-circuit evaluation?
//If there is a side effect in the expression which is used with short circuit operation and if correctness of the program
//depends on the operation this would lead to a problem in the program.
var p = 12;
var q = 15;
while(((q = q-1) > 12) ||  (q == p) ) // it would print 3 times
{
  print("test");
}

}
