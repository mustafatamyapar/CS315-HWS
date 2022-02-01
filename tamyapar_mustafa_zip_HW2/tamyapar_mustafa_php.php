<?php
//1) How are the boolean values represented?
//Boolean values in php are true and false . Also some other expressions such as 
//0 , 0.0 and -0.0 , empty string and string "0" , array with 0 elements and NULL type can be considered as false using type cast.
//Any other value can be used as true with type casting.

$arr = array("Hello", "From","the","Other","Side");
$arr2 = array();


var_dump((bool) 0);// bool(false)
var_dump((bool) 46);// bool(true)
var_dump((bool) -0.0);// bool(false)
var_dump((bool) "");// bool(false)
var_dump((bool) "abc");// bool(true)
var_dump((bool) $arr);// bool(true)
var_dump((bool) $arr2);// bool(false)
var_dump((bool) NULL);// bool(false)
var_dump((bool) true);// bool(true)
var_dump((bool) false);// bool(false)

//2)What operators are short-circuited?
//In PHP short circuit operators are 'and' , && , 'or' ||.
  $elm = 25;
  $and = ($elm < 30 && $elm > 20);
  $and2 = ($elm < 30 and $elm > 20);
  echo "elm < 25 && elm > 10";
  var_dump($and);
  echo "\n";
  var_dump($and2);
  
  $elm2 = 10;
  $or = ($elm2 > 5 || $elm2 < 8);
  $or2 = ($elm2 > 5 or $elm2 < 8);
  print("elm2 > 5 || elm2 < 8");
  var_dump($or);
  echo "\n";
  var_dump($or2);


//3)How are the results of short-circuited operators computed? (Consider also function calls)
//In and operations both expressions are checked if the first one is true but otherwise only first one is checked, if both are 
//true turns true else turns false but in or operation if the first expression is true second one is not checked and if one of them is true turns true.
//In xor operator two expressions must be different for returning true. If both expressions are same it turns false. It checks both expressions.
function fun() { //turns 1 as true
    echo "\n";
    echo "in fun : ";
    return true;
  }
  
  function soFun() {
    echo "\n";
    echo "in soFun : ";
    return false;
  } 
  
print(true && fun()); // executing both
print(fun() and soFun()); //executing both
print(soFun() && fun()); //just executes soFun
print(true || soFun()); //not executes soFun
print(fun() || soFun()); // just executes fun
print(soFun() or fun()); //executing both
print(true or soFun()); //executing non


//4)What are the advantages about short-circuit evaluation?
//Programs will be computed faster due to not computing second expression in the or,and expression. Also as shown below
//if there would not be short circuit operation our program will crash due to exceeding array size . 

$i = 0;
$arrLen = 5;
$key = "hello";
while(($i < $arrLen) && ($arr[$i] != $key))
{
  $i = $i + 1;
}
//5)What are the potential problems about short-circuit evaluation?
//If there is a side effect in the expression which is used with short circuit operation and if correctness of the program
//depends on the operation this would lead to a problem in the program.
$p = 12;
$q = 15;
while((($q = $q-1) > 12) ||  ($q == $p) ) // it would print 3 times
{
  echo "\n";
  echo "disadvantage";
  
}

?>