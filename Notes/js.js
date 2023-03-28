/**let colors = ['red', 'teal', 'cyan','yellow']

for (let color of colors) {
    console.log(color)
}

for (let char of "PURPLE RAIN!") {
    console.log(char)
}

const chicken = {
    name: "Lady Gray",
    age: 4,
    color: "Black"
}

for (let prop in chicken) {
    console.log(`$(prop)->${chicken[prop]}`)
}
*/

function greet() {
    console.log("STARFISH LOVES YOU")
}

function diss(){
    console.log("NOT TODAY POTATO")
}
 

// setTimeout(function() {
//     console.log("MEOW");
//     console.log("Woof");
//     console.log("OINK");
// }, 3000);

// function doTwice(func) {
//     func();
//     func();
// }

// doTwice(function () {
//     console.log("STOP BOTHERING ME!");
//     console.log("PLEASE GO AWAY")
// })

// const printOne = function () {
//     console.log(1)
// }

// function printOne(){

// }

const funcs = [function () {}, function (){}]

/*single threaded*/
// greet();
// alert("I AM ALERT");
// diss();

// greet();
// setTimeout(diss, 3000);
// setTimeout(diss, 1000);
// greet();

// const id = setInterval(diss, 2000);



// function repeatThreeTimes(func){
//     func();
//     func();
//     func();
// }

// function repeat(num, func) {
//     for (let i=0; i < num; i++) {
//         func();
//     }
// }