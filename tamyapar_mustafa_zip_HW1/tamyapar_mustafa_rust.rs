fn main() {
//1) What types are legal for subscripts?
//In rust language, integer Followed by its bit, boolean, charachter , String are allowed subscript types.
let arr: [i32; 5] = [1, 2, 3, 4, 5]; 
let names:[String; 4] = ["Beliz".to_string(),"Meleknaz".to_string(),"Doğa".to_string(),"Bengisu".to_string()];
println!("{:?}",arr);
println!("{:?}",names);

//Accessing elements in rust arrays.
let a: i32 = arr[0];
println!("First element is: {}", a);

//2)Are subscripting expressions in element references range checked?
//Yes it is checked in rust.
//let b = arr[5]; //gives error due to arrays boun being 4

//4)When does allocation takes place?
//Allocation takes place in compile time because this code snippet is not compiling.
//let b = arr46[0];

//5)Are ragged or rectangular multidimensional arrays allowed, or both?
//Rust allows rectangular multidimensional arrays but does not allows ragged multidimensional arrays.
println!("Rectangular arrays");
let mut rectangular = [[0u8; 4]; 3];
rectangular[0] = [72, 81 ,63,49]; 
println!("{:?}",rectangular);

//6)Can array objects be initialized?
//Array objects can be initialized in rust arrays.
println!("Object example ");
let grades:[i32; 4] = [30,40,25,20];
let g: i32 = grades[0];
println!("First grade is: {}" ,g);

//7)Are any kind of slices supported?
//Rust supports slices.
println!("Slice example: ");
let whole: [i32; 4] = [11, 22, 33, 44];

let slice: &[i32] = &whole;
println!("Whole array {:?}", slice);//Returns whole array

let slice2 = &whole[0..2];//[11,22]
println!("slice2 is {:?}", slice2);

let slice3: &[i32] = &whole[0..3];//[11,22,33]
println!("slice2 is {:?}", slice3);

//8)Which operators are provided?
//In Rust  [] , []= ,&[] operators
//are provided.

let op_arr =[3, 4]; // []
println!("[] operation ");
println!("{:?}",op_arr);

let op_arr2: [i32; 5] = [4, 8, 16, 32, 64]; 
let elmt = op_arr2[0]; // []=
println!("[]= operation ");
println!("{}",elmt);

let result = &op_arr2[..];// &[]
println!("&[] operation ");
println!("Result is {:?}", result);

}