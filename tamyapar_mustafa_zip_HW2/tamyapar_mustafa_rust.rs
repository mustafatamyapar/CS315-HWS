fn main() {
//1) How are the boolean values represented?
//In rust true and false are boolean representations but with type casting 1 and 0 is also used.
let big; 
big = 10 > 1; 
println!("{}",big);
let nom;
nom = "a" == "b";
println!("{}",nom);

println!("{}", true as i32);//1
println!("{}", false as i32);//0
println!("{}",true);
println!("{}",false);
//2)What operators are short-circuited?
//Short circuit operators are && ,|| in rust.
let elm = 20;
let and = elm < 25 && elm > 10;
println!("elm < 25 && elm > 10");
println!("{}",and);

let elm2 = 10;
let or = elm2 > 5 || elm2 < 8;
println!("elm2 > 5 || elm2 < 8");
println!("{}",or);

fn func1() -> bool  {
  return true;
}
fn func22() -> bool {
  return false;
}
fn func3() -> bool {
  println!("func3 executed");
  return true;
}
fn func4() -> bool {
  println!("func4 executed");
  return false;
}
  if func1() && func22()
{
  println!("Short Circuit");
}

if func3() || func4() //shows that func 4 is not executed.
{
  println!("Short Circuit 2 ");
}
//3)How are the results of short-circuited operators computed? (Consider also function calls)
//In and operations both expressions are checked if the first one is not false,if false only first one is checked, if both are true turns true else turns false
//but in or operation if the first expression is true second one is not checked and if one of them is true turns true.
fn func() -> bool 
  {
  println!("in func");
  return true;
  }
  fn func2() -> bool 
{
  println!("in func2");
  return false;
} 

println!("{}",true && func()); // executing both
println!("{}",func() ^ func2()); //executing both
println!("{}",func2() && func()); //executing just func2
println!("{}",true || func2()); //not executes func2
println!("{}",func() || func2()); // just executes func
println!("{}",func2() || func()); //executing both

//4)What are the advantages about short-circuit evaluation?
//Programs will be computed faster due to not computing second expression in the or,and expression. Also as shown below
//if there would not be short circuit operation our program will crash due to exceeding array size . 
let arr1 = ["tamyapar","mustafa","efe"];
let mut i = 0;
let arr_len = 3;
let key = "mustafa";
while (i < arr_len) && (arr1[i] != key)
{
i = i + 1;
}
//5)What are the potential problems about short-circuit evaluation?
//If there is a side effect in the expression which is used with short circuit operation and if correctness of the program
//depends on the operation this would lead to a problem in the program.
let p = 9;
let mut q = 12;
while (q > 9) ||  (q == p) // it would print 4 times
{
    q = q-1;
println!("disadvantage");

}

}