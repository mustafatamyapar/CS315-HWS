<?php
//1) What types are legal for subscripts?
//In PHP language, integer, float, string, boolean, charachter, null are allowed subscript types.

$arr = array("Hello", "From","the","Other","Side");
print_r($arr);

//Accessing elements in PHP arrays.
echo "Accessing elements :";
echo $arr[0];
echo $arr[1], "\n";

//2)Are subscripting expressions in element references range checked?
//echo $arr[5], "<br>"; //gives error due to arrays boun being 4

//4)When does allocation takes place?
//Allocation takes place in compile time because this code snippet is not compiling.
//echo $arr2[0], "<br>";

//5)Are ragged or rectangular multidimensional arrays allowed, or both?
//PHP allows ragged multidimensional arrays but not rectangular multidimensional arrays.
echo "Multdimensional Arrays \n";
$friends = array (
    array("Name" => "Mustafa", "Age" => 20),
    array("Name" => "Onat")
);
print_r($friends);

//6)Can array objects be initialized?
//Array objects can be initialized in php arrays.
echo "Object example ";
echo "\n";
$meal = array("Red lentil soup", "meatballs", "pasta", "yoghurt","grapes", "wine");
echo "Soup of the day is: " . $meal[0] . "\n";

//7)Are any kind of slices supported?
//Php supports slices.
$animals = array("cat","dog","fish","whale");
print_r(array_slice($animals,0,2));//[0] => cat [1] => dog

//8)Which operators are provided?
//In PHP  +(union) , ==(equality) , ===(identity) , !=(non equality) !==(non identity), <>(non equality) operators
//are provided.
$sum = array(1);
$sum2 = array(9, 9);
$sum3 = $sum + $sum2;//+(union)
echo "+ operation ";
echo "\n";
print_r($sum3);//[0] => 1 [1] => 9

echo "== (equality)operation ";
echo "\n";
var_dump($sum2 == $sum3);// ==(equality)

echo "=== (identity)operation ";
echo "\n";
var_dump($sum2 == $sum3);// ===(identity)

echo "!= (non equality)operation ";
echo "\n";
var_dump($sum2 != $sum3);//!=(non equality)

echo "!== (non identity)operation";
echo "\n";
var_dump($sum2 !== $sum3);//!==(non identity)

echo "<>(non equality)operation ";
echo "\n";
var_dump($sum2 <> $sum3);//<>(non equality)
  

?>
