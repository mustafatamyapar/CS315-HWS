import "dart:io";
void main() { 

  //1) What types are legal for subscripts?
  //In Dart char, integer, string, double, boolean are allowed for subcripting.
  var arr1 = ["tamyapar","mustafa","efe"];
  stdout.write("arr1: ");
  print(arr1);

  String name = 'ali'; 
  String name2 = 'ali';   
  bool b = (name == name2);
  var arr2 = [b];
  //Accessing elements in Dart arrays.
  String surname = arr1[0];

  var raggedArr = [[1],[2,3]];
  print(raggedArr);
  stdout.write("Accesing elements: ");
  print(surname);
  print(arr2[0]);

  //2)Are subscripting expressions in element references range checked?
  //Range check takes place in run time.
  // stdout.write("Range Check");
  //print(arr2[4]); //Gives an error due to range of the array being 0.

  //4)When does allocation takes place?
  //Allocation takes place in compile time because this code snippet is not compiling.
  //String me = arr4[0];

  //5)Are ragged or rectangular multidimensional arrays allowed, or both?
  //In Dart language, both ragged and rectangular multidimensional arrays are alloed.
  stdout.write("Multidimensional arrays: ");
  var multi = List.generate(3, (i) => List.generate(3, (j) => i + j));
  print("Rectangular : ");
  print(multi);

  stdout.write("Ragged : ");
  var ragged = [[1],[2,3]];
  print(ragged);
  

  //6)Can array objects be initialized?
  //In dart array objects are allowed.  
  var album = ["Hallo",1, "Easy",2]; //array of objects
  stdout.write("Objects of the album array: ");
  print(album[0]);
  print(album[2]);

  var album2 = [Single("Hallo",1), Single("Easy",2)]; //Array of Single objects
  print(album2[0].name);
  print(album2[1].name);

  //7)Are any kind of slices supported?
  //Dart supports slices.
  var kitchen = ["knife", "spoon", "fork", "cooker", "mixer"];
  stdout.write("Sublist examples: ");
  print(kitchen.sublist(0, 3)); // [knife, spoon, fork]
  print(kitchen.sublist(3)); // [cooker, mixer]

  //8)Which operators are provided?
  //In Dart +, -, [], []=, == operators are allowed.
  var arr3 = [1];
  var arr4 = [2, 2];
  var arr5 = arr3 + arr4;//+
  stdout.write("+ operation ");
  print(arr5);

  var arr7 = [1];
  arr7[0] = 120; // []
  stdout.write("[] operation ");
  print(arr7);

  var elmt = arr7[0]; // []=
  stdout.write("[]= operation ");
  print(elmt);

  stdout.write("== operation ");
  print(arr5 == arr7);//==
}
class Single
{
  String name;
  int length;
  Single(this.name,this.length);
}