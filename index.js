/* 
- document.getElementById("MyH1").textContent
Reference to the element with id MyH1 in this scope

- window.alert("")
Displays a popup using the quoted text

- ${Variable_Name}
References a variable when inside of ``

- console.log(typeof variable);
Prints the type of the given variable

- let myPrompt = window.prompt("Prompt Text");
Prompts the user with a popup and records the input to username
*/

let variable = "variable"
document.getElementById("variableP").textContent = variable
const constant = "constant"
document.getElementById("constP").textContent = constant

console.log(`${variable} is how you include a variable in backticks`)

// Accepting input

/* Window prompt is easiser
HTML Textbox looks/works better */

// Changes the heading to the inputted text
document.getElementById("mySubmit").onclick = function(){
    input = document.getElementById("myText").value
    document.getElementById("myH1").textContent = `${input}`
}